from rest_framework import viewsets

from .serializer import QuestionSerializer, QuizSerializer, ResultSerializer, UserSignupSerializer
from .models import question, quiz, result, userSignup
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .froms import questionForm, quizForm, userSignupForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


class questionViewset(viewsets.ModelViewSet):
    queryset = question.objects.all()
    serializer_class = QuestionSerializer


class quizViewset(viewsets.ModelViewSet):
    queryset = quiz.objects.all()
    serializer_class = QuizSerializer


class resultViewset(viewsets.ModelViewSet):
    queryset = result.objects.all()
    serializer_class = ResultSerializer

class userSignupViewset(viewsets.ModelViewSet):
    queryset = userSignup.objects.all()
    serializer_class = UserSignupSerializer


def web_view(request):
    return render(request, "myquizapi/index_login.html", {})


def web_List_Quiz(request):
    return render(request, "myquizapi/ListQuiz.html", {})


def web_Signup(request):
    form = userSignup()
    if request.method == "POST":
        form = userSignup(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('Username')
            # messages.success(request, f'Account for {username} created successfully')
            return redirect('./My_Quiz_web_app_profile')

    return render(request, "myquizapi/signup.html", {'form':form})

# def register(request):
#     if request.method =='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username} created successfully!')
#             form.save()
#             return redirect('./My_Quiz_web_app_profile')
#     else:
#         form =  UserCreationForm
#     return render(request, "myquizapi/register.html", {'form':form})


def web_profile(request):
    return render(request, "myquizapi/Profile.html", {})


def web_Attend_quiz(request):
    return render(request, "myquizapi/AttendQuiz.html", {})


def web_Create_quiz(request):
    form = quizForm
    if request.method == "POST":
        form = quizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./My_Quiz_web_app_admin')
    return render(request, "myquizapi/create_quiz.html", {'form': form})


def web_Create_question(request):
    form = questionForm
    if request.method == "POST":
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./My_Quiz_web_app_create_quiz')

    return render(request, "myquizapi/create_question.html", {'form': form})


def admin_page(request):
    return render(request, "myquizapi/AdminPannel.html", {})


def web_home(request):
    return render(request, "myquizapi/index.html", {})
