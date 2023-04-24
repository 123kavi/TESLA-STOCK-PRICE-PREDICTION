import datetime

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
import numpy as np



import warnings

warnings.filterwarnings("ignore")

# yahoo finance used to fetch data
import yfinance as yf

yf.pdr_override()

options = " TESLA STOCK LINEAR REGRESSION PREDICTION , " \
          "TESLA STOCK svm  REGRESSION PREDICTION, " \
          " TESLA STOCK DECISION TREE  PREDICTION, TESLA STOCK BAYESIAN RIDGE REGRESSION  PREDICTION, Exit".split(",")


# Input Start Date
def start_date():
    date_entry = input('Enter a starting date in MM/DD/YYYY format: ')
    start = datetime.datetime.strptime(date_entry, '%m/%d/%Y')
    start = start.strftime('%Y-%m-%d')
    return start


# Input End Date
def end_date():
    while True:
        try:
            date_entry = input("Enter end date (MM/DD/YYYY): ")
            end = datetime.datetime.strptime(date_entry, '%m/%d/%Y')
            return end.date()
        except ValueError:
            print("Error: Please enter a valid date in the format MM/DD/YYYY")


# Input Symbols
def input_symbol():
    symbol = input("Enter symbol: ").upper()
    return symbol


# Support Vector Regression


def stock_linear_regression():
    s = start_date()
    e = end_date()
    sym = input_symbol()
    df = yf.download(sym, s, e)
    n = len(df.index)
    X = np.array(df['Open']).reshape(n, -1)
    Y = np.array(df['Adj Close']).reshape(n, -1)
    lr = LinearRegression()
    lr.fit(X, Y)
    lr.predict(X)
    print('_____________Summary:_____________')
    print('Estimate intercept coefficient:', lr.intercept_)
    print('Number of coefficients:', len(lr.coef_))
    print('Accuracy Score:', lr.score(X, Y))
    print("")
    plt.figure(figsize=(12, 8))
    plt.scatter(df['Adj Close'], lr.predict(X))
    plt.plot(X, lr.predict(X), color='red')
    plt.xlabel('Prices')
    plt.ylabel('Predicted Prices')
    plt.grid()
    plt.title(sym + ' Prices vs Predicted Prices')
    plt.show()
    print('_____________Summary:_____________')
    print('Estimate intercept coefficient:', lr.intercept_)
    print('Number of coefficients:', len(lr.coef_))
    print('Accuracy Score:', lr.score(X, Y))
    print("")
    ans = ['1', '2']
    user_input = input("""                  
What would you like to do next? Enter option 1 or 2.  
1. Menu
2. Exit
Command: """)
    while user_input not in ans:
        print("Error: Please enter a valid option 1-2")
        user_input = input("Command: ")
    if user_input == "1":
        menu()
    elif user_input == "2":
        exit()


# Decision Tree Regression




# ***********************************************************************************************************************#
# ******************************************************* Menu **********************************************************#
# ***********************************************************************************************************************#
def menu():
    ans = ['1', '2', '3', '4', '5', '0']
    print(""" 

                                                                            MENU
         *********************************************MACHINE LEARNING STOCK PRICE PREDICTION*********************************************     


                  1.TESLA STOCK LINEAR REGRESSION PREDICTION 
                  2.TESLA STOCK SVM  REGRESSION PREDICTION
                  3.TESLA STOCK DECISION TREE  PREDICTION
                  4.TESLA STOCK BAYESIAN RIDGE REGRESSION  PREDICTION
                  5.BEGINNING MENU
                  0.EXIT 
                  """)
    user_input = input("Command (0-5): ")
    while user_input not in ans:
        print("Error: Please enter a valid option 0-5")
        user_input = input("Command: ")

    # ***********************************************************************************************************************#


# *************************************************** Start of Program **************************************************#
# ***********************************************************************************************************************#
def beginning():
    print()
    print("----------WELCOME TO SUPERVISED  LEARNING  STOCK PRICE PREDICTION--------")
    print("""
Please choose option 1 or 2

1. Menu
2. Exit Program 

---------------------------------------------""")
    ans = ['1', '2']
    user_input = input("What is your Option?: ")
    while user_input not in ans:
        print("Error: Please enter a a valid option 1-2")
        user_input = input("Command: ")
    if user_input == "1":
        menu()
    elif user_input == "2":
        exit()


# ***********************************************************************************************************************#
beginning()
