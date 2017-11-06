from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.db.models import Q

import datetime

from quora.forms import RegisterForm, QuestionForm
from quora.models import Question, Answer

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'auth/login.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('home')
    else:
        return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
        return HttpResponse("register gagal")
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', { 'form': form })

def logout(request):
    auth_logout(request)
    return redirect('index')

def home(request):
    questions = Question.objects.order_by('-date', '-time')

    context = {
        'questions': questions
    }
    
    return render(request, 'home.html', context)

def ask_question(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'question': request.POST.get('question'),
            'user': request.user,
            'date': datetime.datetime.today(),
            'time': datetime.datetime.now().time()
        }
        question = Question.objects.create(**data)

    return HttpResponse("Ask question success")

def answer_question(request):
    question_id = request.POST.get('question_id')
    question = Question.objects.get(pk=question_id)
    data = {
        'question': question,
        'user': request.user,
        'answer': request.POST.get('answer'),
        'date': datetime.datetime.today(),
        'time': datetime.datetime.now().time()
    }
    answer = Answer.objects.create(**data)

    return HttpResponse("Answer question success")

def my_question(request):
    my_questions = Question.objects.filter(user=request.user)

    return render(request, 'my_question.html', { 'my_questions': my_questions })

def search(request):
    query = request.POST.get('keyword')
    search_questions = Question.objects.filter(Q(title__contains=query) | Q(question__contains=query))

    return render(request, 'search.html', { 'search_questions': search_questions })

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        answers = Answer.objects.filter(question=question)
        len_answer = len(answers)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'question.html', { 'question' : question, 'answers': answers, 'len_answer': len_answer })