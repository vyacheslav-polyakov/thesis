import pandas as pd
from statsmodels.formula.api import ols
from scipy import stats
import statsmodels.api as sm
import patsy

path =  r'D:\Docs\Works\InProgress\Thesis\Data Analysis\Regression\test.xls'
df = pd.read_excel(path, usecols = ['Q1_性别', 'Q2_您的年龄是？', 'Q14_淘宝直播会鼓励您进行网上购物吗？'])
df_dummy = pd.get_dummies(df["Q1_性别"])
df_dummy = pd.concat([df, df_dummy], axis = 1)
df_dummy.drop(["Q1_性别", "女"], inplace = True, axis = 1)
reg = ols("Q14_淘宝直播会鼓励您进行网上购物吗？ ~ Q2_您的年龄是？", df_dummy).fit()
print(reg.summary())
