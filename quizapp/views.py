from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
#from django.contrib.auth import authenticate
from django.core.mail import send_mail
import smtplib
from interview_project.settings import EMAIL_HOST_USER
from django.conf import settings
from django.core.mail import EmailMessage
import math,random
from .models import Quizname,Quiz_question
from django.core.paginator import Paginator
# Create your views here.
lst=[]
answers = Quiz_question.objects.all()
anslist = []
for i in answers:
    anslist.append(i.ans)
#this fun is used for print the result
def result(request):
        score =0
        res="fail"
        print("li",len(lst))
        for i in range(len(lst)):
            print("hii")
            if lst[i]==anslist[i]:
                
                score +=1
            if score>=5:
                res="pass"
        return render(request,'result.html',{'score':score,'lst':lst,'res':res})
#this fun is used for save answers
def save_ans(request):
        ans = request.GET['ans']
        print("kii",ans)
        lst.append(ans)
#this fun is used for start quiz
def start(request):
    lst.clear()
    data=Quizname.objects.all()
            
            
    return render(request,'start.html',{'data':data})
#this fun is used for print the questions
def question(request):
    
        count = Quiz_question.objects.all().count()
        q=Quiz_question.objects.all()
        print(q)
        paginator =Paginator(q,1)
        print(paginator.num_pages)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page=1
        try:
            quest=paginator.page(page)
        except:
            quest=paginator.page(paginator.num_pages)
        
        print(quest)
        
        return render(request,'quizpage.html',{'q':q,'quest':quest,'count':count})
#this fun is used for user login
def login(request):
    
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        print(name)
        print(password)
        q=User.objects.all()
        print(q)
        s=User.objects.filter(password=password)
        print(s)
        user=auth.authenticate(username=name,password=password)
        print(user)
        
        if user is not None:
            auth.login(request,user)
            data=Quizname.objects.all()
            
            
            return render(request,'homepage.html',{'data':data})
        else:
            messages.info(request,'invalid password or username')
            return redirect('login')
    else:
        return render(request,'login.html')    
#this fun is used for user register
def register(request):
    if request.method == 'POST':
        
        
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print("hii")
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("me")
                messages.info(request,'username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
               with smtplib.SMTP('smtp.gmail.com',587 ) as server:
                    digits="0123456789"
                    result=" "
                    for i in range(4):
                        otp=digits[math.floor(random.random()*7)]
                        
                        print(otp,end="")
                        result=result+otp
                    print()
                    print(result)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login('nk4556138@gmail.com','naveennk')
                    subject='welcome'
                    body='hii'
                    msg=f"subject:{subject}\n\n{body}\n\n{result}"
                    server.sendmail(
                        'nk4556138@gmail.com',
                        email,
                        msg
                    )
                    print("sent")
                    
                
                    print("bye")
                
                    return render(request,'check.html',{'result':result,'email':email,'username':username,'password':password1,'password2':password2})

        else:
             messages.info(request,'password not created')
             return redirect('/')
    else:

         return render(request,'register.html')