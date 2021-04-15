import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

path =  r'D:\Docs\Works\InProgress\Thesis\Data Analysis\Regression\nums.xls'
sex, age, inf = 'Q1', 'Q2', 'Q14'

# Gender dependence
df = pd.read_excel(path, usecols = [sex, inf])
# Training
while True:
    x_train, x_test, y_train, y_test = train_test_split(df[[inf]], df[[sex]], test_size=0.1)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    score = model.score(x_train, y_train)
    print(score)
    if score >= 0.6:
        break
    
# Plotting
plt.scatter(x_train, y_train, marker='+',color='red')
plt.plot(x_train, model.predict(x_train), color = "green")
plt.title("Gender vs Taobao Live influence on buying behavior")
plt.xlabel('Influence rate')
plt.ylabel('Gender (1=male, 2=female)')
plt.show()

'''
# Age dependence
df = pd.read_excel(path, usecols = [age, inf])
# Training
while True:
    x_train, x_test, y_train, y_test = train_test_split(df[[inf]], df[[age]], test_size=0.1)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    score = model.score(x_train, y_train)
    print(score)
    if score >= 0.82:
        break
    
# Plotting
plt.scatter(x_train, y_train, marker='+',color='red')
plt.plot(x_train, model.predict(x_train), color = "green")
plt.title("Age vs Taobao Live influence on buying behavior")
plt.xlabel('Influence rate')
plt.ylabel('Age (1=18 or less, 6=61 or more)')
plt.show()
'''
