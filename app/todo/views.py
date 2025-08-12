from django.shortcuts import render
from django.http import HttpResponse

def todo_list(request,id):
    return render(request,'todo/todo_list.html',{'id' : id})

def login(request):
    return render(request,'todo/login.html')

def register(request):
    return render(request,'todo/register.html')

def home(request):
    return render(request,'todo/home.html')