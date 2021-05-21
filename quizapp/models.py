from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Quizname(models.Model):
    quiz_name=models.CharField(max_length=1000,unique=False)
class Quiz_question(models.Model):
    quiz_quest=models.ManyToManyField(Quizname)
    question=models.CharField(max_length=1000,unique=False)
    option1=models.CharField(max_length=100,unique=False)
    option2=models.CharField(max_length=100,unique=False)
    option3=models.CharField(max_length=100,unique=False)
    option4=models.CharField(max_length=100,unique=False)
    ans=models.CharField(max_length=100,unique=False)
