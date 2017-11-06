from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    user = models.ForeignKey('auth.User')
    date = models.DateField()
    time = models.TimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    date = models.DateField()
    time = models.TimeField()