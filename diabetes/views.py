from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.metrics import accuracy_score
import pandas as pd




def home(request):
    
    
    return render(request, "home.html")



def predict(request):
    
    return render(request, "predict.html")

def result(request):
    
    data = pd.read_csv("diabetes.csv")
    
    x = data.drop(['Outcome'], axis = 1)
    y = data["Outcome"]
    
    x_train, x_test, y_train, y_test= train_test_split(x , y , test_size=0.2,random_state=1)
    
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
    
    pred = model.predict([[var1,var2,var3,var4,var5,var6,var7,var8]])
    
    result2 = ''
    if pred==[1]:
        result2="diabetes"
    else:
        result2="no diabetes"
        
        
    return render(request, "result.html", {"result2":result2})

