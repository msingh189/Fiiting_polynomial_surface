# Fitting_polynomial_surface

## Paper Link: https://doi.org/10.1007/s11664-021-09099-w

## Paper Title: Metamaterial-Inspired Complementary Split Ring Resonator Sensor with Second-Order Approximation for Dielectric Characterization of Fluids (Springer - Journal of Electronic Materials)
A metamaterial-based Complementary Split Ring Resonator (CSRR) structure is used to develop a sensor for dielectric
characterization of fluids. The fluid present in the vertical column interacts with the fields around the CSRR causing
a shift in the transmission coefficient curve (S21). An empirical relationship can be established between the dielectric
properties and the resonance frequency and Q-factor. This relationship is used for the dielectric characterization of the
fluid. A second-order polynomial function was employed for a better curve fitting of the data to achieve higher accuracy
in the prediction of complex permittivity (ε' and ε''). The design is very simple and the fluid can be easily changed by
replacing the glass tube. The sensor has very high sensitivity and requires a very little volume of the sample.

## Pseudo-code
1. Import Libraries [for python • Pandas • Numpy • sklearn]
2. Read data from csv (comma separated values) file and
convert it into a dataframe (say df)
df = pandas.read_csv(“filename_with_extension”)
3. There are 2 training data columns of 2 target columns to
be predicted. Extract only required columns from dataframe.
train_features = [‘column1’, ‘column2’]
target_column_1 = df[‘target1’]
target_column_2 = df[‘target2’]
data = df[‘train_features’]
4. Take the input of two train_features values (f and Q) to
predict target values (e0 and e00)
f = float(input(Enter the value of first input
feature))
Q = float(input(Enter the value of second
input feature))
5. Generate polynomial and interaction features. The
degree-2 polynomial features are [1, a, b, a2, ab, b2]. [Use
PolynomialFeatures class from sklearn.preprocessing library
for python]
poly = sklearn.preprocessing.PolynomialFeatures(degree
= DEGREE OF POLYNOMIAL YOU WANT TO CREATE)
poly_variables = poly.fit_transform(array of
values of input features)
6. Repeat the above process for test values for which we
are predicting output values:
test_variables = poly.fit_transform(an array
of array of input values f and Q)
7. To create model, use simple linear regression. [Use LinearRegression from library sklearn.linear_model for python]
regression = sklearn.linear_model.LinearRegression()
model = regression.fit(poly_variables,target_column_1)
Obtain the coefficients and intercept of fitted equation.
print(coefficients of fitted/learned equation)
print(intercept of fitted/learned equation)
9. Predict the model. [Use model.predict() for python]
prediction = model.predict(test_variables)
print(prediction)
10. Repeat step 8 and 9 for second target column to predict
another target value. We have to use 2 separate models for
training, as it is multi-target regression problem.

## How to use?
1. Download the code by clicking on Download Zip button under Code green button.
2. Extract the zip.
3. Make sure you have python, pandas, numpy and sklearn libraries installed.
4. Now, open cmd (Command Prompt) and go to folder where the zip is extracted and opened.
5. Now type *python main_ethanol/methanol/combined (as per your need).py* command
6. Put the value of *f* and *Q*.
7. DONE!!
