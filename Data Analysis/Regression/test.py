import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import pylab
import math
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats import diagnostic as diag
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Load the data into Pandas
data_df = pd.read_excel('test.xls')
data_df = data_df.replace("..","nan")

# Set the index equal to the age column
data_df.index = data_df['Age']
data_df = data.df.drop('Age', axis = 1)


