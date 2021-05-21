from django.urls import path
from . import views


urlpatterns=[
    
    
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('question',views.question,name='question'),
    path('result',views.result,name='result'),
    path('start',views.start,name='start'),
    path('save_ans',views.save_ans,name='save_ans'),
]