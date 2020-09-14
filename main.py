import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")

features = ["resonance frequency","Q factor"]
y1 = df["e\'"]
y2 = df["e''"]

data = df[features]

f = float(input('Enter the value of f ='))
Q = float(input('Enter the value of Q ='))

poly = PolynomialFeatures(degree=2)
poly_variables = poly.fit_transform(data.values)

regression = linear_model.LinearRegression()
model = regression.fit(poly_variables, y1.values)

test_var = poly.fit_transform([[f,Q]])
pred = model.predict(test_var)
print("predicted value of e' = "+str(pred[0]))

poly = PolynomialFeatures(degree=2)
poly_variables = poly.fit_transform(data.values)
model = regression.fit(poly_variables, y2.values)

test_var = poly.fit_transform([[f,Q]])
pred = model.predict(test_var)
print("predicted value of e\" = "+str(pred[0]))
