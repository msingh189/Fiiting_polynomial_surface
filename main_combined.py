import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df_1 = pd.read_csv("data_ethanol.csv")
df_2 = pd.read_csv("data_methanol.csv")

cols = ["resonance frequency","Q factor","e\'","e''"]

df_1 = df_1[cols]
df_2 = df_2[cols]

df = pd.concat([df_1,df_2],ignore_index=True)
features = ["resonance frequency","Q factor"]
y1 = df["e\'"]
y2 = df["e''"]

data = df[features]

f = float(input('Enter the value of f ='))
Q = float(input('Enter the value of Q ='))

poly = PolynomialFeatures(degree=2)
poly_variables = poly.fit_transform(data.values)

print("======Predicting e'======")
regression = LinearRegression()
model = regression.fit(poly_variables, y1.values)
print("Coefficients:",model.coef_[:])
print("Constant:",model.intercept_)

test_var = poly.fit_transform([[f,Q]])
pred = model.predict(test_var)
print("predicted value of e' = "+str(pred[0]))

print("======Predicting e\"======")
poly = PolynomialFeatures(degree=2)
poly_variables = poly.fit_transform(data.values)
model = regression.fit(poly_variables, y2.values)
print("Coefficients:",model.coef_[:])
print("Constant:",model.intercept_)

test_var = poly.fit_transform([[f,Q]])
pred = model.predict(test_var)
print("predicted value of e\" = "+str(pred[0]))
