
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_as
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import NoReverseMatch

from .forms import LoginForm, RegisterForm
########################
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import mean_squared_error
#############


#@login_required(login_url="login")
def home(request):
    
    
    return render(request, "home.html")


@login_required(login_url="login")
def predict(request):
    
    return render(request, "predict.html")

@login_required(login_url="login")
def result(request):
    
    data = pd.read_csv("I:/django-ml/diabetesV2/diabetes/diabetes.csv")
    
    x = data.drop(['Outcome'], axis = 1)
    y = data["Outcome"]
    x_train, x_test, y_train, y_test= train_test_split(x , y , test_size=0.2,random_state=42)
    
    model = LogisticRegression()
    
    model.fit(x_train,y_train)
    
    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    var6 = float(request.GET['n6'])
    var7 = float(request.GET['n7'])
    var8 = float(request.GET['n8'])
    
    result22 = [var1,var2,var3,var4,var5,var6,var7,var8]
    
    pred = model.predict([result22])[0]
    
    score = np.max(model.predict_proba([result22]))*100
    
    
    result2 = ''
    if pred==[1]:
        result2="diabetes"
    else:
        result2="no diabetes"
        
        
    return render(request, "result.html", {"result2":result2,"score":score})

@login_required(login_url="login")
def guide(request):
    
    return render(request, "guide.html")


def login(request):
    
    if request.method == "GET":
        next_url = request.GET.get("next")
        if request.user.is_authenticated:
            return redirect("account")
        form = LoginForm()
        return render(request, "login.html", {"form": form, "next": next_url})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        next_url = request.POST.get("next")
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login_as(request, user)
                try:
                    return redirect(next_url)
                except NoReverseMatch:
                    return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("login")

def register(request):
    
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            codemeli = form.cleaned_data["codemeli"]
            number = form.cleaned_data["number"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("register")

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("register")

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            login_as(request, user)
            messages.success(request, "Account created successfully")
            return redirect("home")
        
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("home")