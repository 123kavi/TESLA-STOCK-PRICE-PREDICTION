import datetime

from matplotlib import pyplot as plt
# Machine Learning Libraries
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
import numpy as np  # Import the NumPy module with alias 'np'
import warnings

from sklearn.tree import DecisionTreeRegressor
warnings.filterwarnings("ignore")

import pandas as pd
file_path = "../dataset/TSLA.csv"

options = " TESLA STOCK LINEAR REGRESSION PREDICTION , " \
          "TESLA STOCK svm  REGRESSION PREDICTION, " \
          " TESLA STOCK DECISION TREE  PREDICTION, TESLA STOCK BAYESIAN RIDGE REGRESSION  PREDICTION, Exit".split(",")

# Input Start Date
def start_date():
    date_entry = input('Enter a starting date in MM/DD/YYYY format: ')
    start = datetime.datetime.strptime(date_entry,'%m/%d/%Y')
    start = start.strftime('%Y-%m-%d')
    return start
