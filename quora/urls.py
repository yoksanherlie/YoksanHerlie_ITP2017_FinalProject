from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^home', views.home, name='home'),
    url(r'^ask-question', views.ask_question, name='ask-question'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^answer-question', views.answer_question, name='answer-question'),
    url(r'^my-question', views.my_question, name='my-question'),
    url(r'^search-question', views.search, name='search')
]