from django.contrib import admin

from .models import Quizname,Quiz_question

# Register your models here.

admin.site.register(Quiz_question)
admin.site.register(Quizname)

