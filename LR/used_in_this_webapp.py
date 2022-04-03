import numpy as np
import pandas as pd
 
dataset=pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,:1]
y=dataset.iloc[:,1:2]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)


from sklearn.linear_model import LinearRegression 

regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

from sklearn import metrics
import math

print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

a=int(input("Enter Value: "))
l=[]
l.append(a)
b=regressor.predict([[a]])
print(b[0][0])
