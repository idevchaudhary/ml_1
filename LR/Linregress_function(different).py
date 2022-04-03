# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:58:07 2022

@author: Vanshika
"""
import numpy as np
import pandas as pd
from scipy import stats

dataset=pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,:1]
y=dataset.iloc[:,1:2]

slope, intercept, r, p, std_err = stats.mstats.linregress(x, y)

def predict(f):
    return slope*f+intercept


a=float(input("Enter Experience: "))
print("Salary for ", a ,"year experience is",predict(a))
