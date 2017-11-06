from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from quora.models import Question

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label="Password Confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'question', 'user', 'date', 'time', )