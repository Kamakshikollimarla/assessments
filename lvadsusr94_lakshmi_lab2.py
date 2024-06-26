# -*- coding: utf-8 -*-
"""LVADSUSR94_lakshmi_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SYSp3wvSg1_iQ7toK2gPX_mzPNHvNeSg
"""

import pandas as pd
import numpy as np
import seaborn as sns


data = pd.read_csv("/content/booking.csv")
data = pd.DataFrame(data)
data.isna().count()

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values= 0 ,strategy="mean")
d = np.array(data["average price"])
data["average price"] = imputer.fit_transform(d.reshape(-1,1))


imputer = SimpleImputer(missing_values= 0 ,strategy="median")
d = np.array(data["number of adults"])
data["number of adults"] = imputer.fit_transform(d.reshape(-1,1))

d = np.array(data["number of children"])
data["number of children"] = imputer.fit_transform(d.reshape(-1,1))

d = np.array(data["number of weekend nights"])
data["number of weekend nights"] = imputer.fit_transform(d.reshape(-1,1))

d = np.array(data["number of week nights"])
data["number of week nights"] = imputer.fit_transform(d.reshape(-1,1))


imputer = SimpleImputer(missing_values= np.NaN ,strategy="most_frequent")

data[:6:12] = imputer.fit_transform(data[:6:12])

imputer = SimpleImputer(missing_values= 0 ,strategy="most_frequent")

data[:-1:] = imputer.fit_transform(data[:-1:])

data.info()

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

da = data[:5:13]
le = LabelEncoder()

data["booking status"] = le.fit_transform(data["booking status"])
data["type of meal"] = le.fit_transform(data["type of meal"])
data["room type"] = le.fit_transform(data["room type"])

data["market segment type"] = le.fit_transform(data["market segment type"])

sns.boxplot(data)

from scipy import stats
zscores = stats.zscore(data)
abs = np.abs(zscores)
f = (abs > 0.0052).all(axis = 1)
filterd_d= data[f]
print(d.shape)
print(filterd_d.shape)

data.head()

c = filterd_d
a = c.corr()
print(a)
sns.heatmap(a)

remove = ["type of meal","car parking space","repeated","P-C"]
c.drop(remove,axis='columns')

X = c.iloc[:,:-1]
y = c.iloc[:,-1:]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=10000)
model = clf.fit(X_train,y_train)
pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score,mean_squared_error,mean_absolute_error, r2_score

mse = mean_squared_error(pred,y_test)
mae = mean_absolute_error(pred,y_test)
rmse = np.sqrt(mse)
r2 = r2_score(pred,y_test)
print("mse:" , mse)
print("mae:" , mae)
print("r2:",r2)
print("rmse:",rmse)
print("accuracy:",accuracy_score(pred,y_test))

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
model = clf.fit(X_train,y_train)
pred = clf.predict(X_test)

mse = mean_squared_error(pred,y_test)
mae = mean_absolute_error(pred,y_test)
rmse = np.sqrt(mse)
r2 = r2_score(pred,y_test)
print("mse:" , mse)
print("mae:" , mae)
print("r2:",r2)
print("rmse:",rmse)
print("accuracy:",accuracy_score(pred,y_test))