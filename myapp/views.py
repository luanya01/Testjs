from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    remember = forms.BooleanField(required=False)

def first_view(request):
    return render(request, 'first_view.html') 

@api_view(['GET', 'POST'])
def pop_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'pop_view.html' , context={'form':form})
    else:
        return redirect(reverse('myapp:login_consent'))

@api_view(['GET'])
def callback(request):
    return Response({'access_token':'hello-token'})

def login_consent_view(request):
    return redirect(reverse('myapp:callback'))