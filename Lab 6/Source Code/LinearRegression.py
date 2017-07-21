# Required Packages
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

date_row = []
price_row = []

def get_data(file_name):
    with open(file_name, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:

            date_row.append(int(row[0]))
            price_row.append(float(row[1]))
    return




def show_plot(dates, prices):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates, (len(dates), 1))
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)
    plt.scatter(dates, prices, color='red')
    plt.plot(dates, linear_mod.predict(dates), color='green', linewidth=3)
    plt.show()
    return

def predict_price_value(dates, prices, x):
    linear_mod = linear_model.LinearRegression()  # defining the linear regression model
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)  # fitting the data points in the model
    predicted_price = linear_mod.predict(x)
    return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]

get_data('google.csv')  # calling get_data method by passing the csv file to it
print
date_row
print
price_row
print
"\n"

show_plot(date_row, price_row)
# image of the plot will be generated. Save it if you want and then Close it to continue the execution of the below code.

print("predicted values are:")
(predicted_price, coefficient, constant) = predict_price_value(date_row, price_row, 1)
print("The stock open price for 1 July is: $", str(predicted_price))
print("The regression coefficient is ", str(coefficient), ", and the constant is ", str(constant))
print("the relationship equation between dates and prices is: price = ", str(coefficient), "* date + ", str(constant))




