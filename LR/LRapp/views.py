from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import math

# Create your views here.
def home(request):
    return render(request,'LRapp/home.html')
def result(request):
    dataset=pd.read_csv('Salary_Data.csv')
    x=dataset.iloc[:,:1]
    y=dataset.iloc[:,1:2]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
    regressor=LinearRegression()
    regressor.fit(x_train,y_train)
    y_pred=regressor.predict(x_test)
    x=(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

    lis=[]
    lis.append(request.POST.get('r1'))
    fl=[]
    for x in lis:
        fl.append(int(x))

    temp_ans=regressor.predict([fl])
    ans=temp_ans[0][0]

    return render(request,'LRapp/result.html',{'ans':ans,'fl':fl[0]})