from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_roc_curve
import pandas as pd

path =  r'D:\Docs\Works\InProgress\Thesis\Data Analysis\Regression\nums.xls'
sex, age, inf = 'Q1', 'Q2', 'Q14'
df = pd.read_excel(path, usecols = [sex, age, inf])

# Sex influence on buying behavior
x_train, x_test, y_train, y_test = train_test_split(df[[sex]],df[[inf]], test_size=0.1)
model = LogisticRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test) # Predict class labels for samples in X

plt.scatter(x_train, y_train, color = "red")
plt.plot(x_train, model.predict(x_train), color = "green")
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(x_test, y_test, color = "red")
plt.plot(x_train, model.predict(x_train), color = "green")
plt.title("Salary vs Experience (Testing set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

'''
conf = model.decision_function(X_test) # Predict confidence scores for samples
score = model.score(X_test, y_test) # Returns the mean accuracy on the given test data and labels
proba = model.predict_proba(X_test)
params = model.get_params(deep=True)

# Plotting the graph
plot = plot_roc_curve()

plt.plot(X_test, model.coef_ * X_test + model.intercept_, linewidth=1)
plt.axhline(.5, color='.5')
plt.ylabel('y')
plt.xlabel('x')
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.ylim(-.25, 1.25)
plt.xlim(-4, 10)
plt.legend(('Logistic regression model', 'Linear Regression Model'),
                    loc = 'lower right', fontsize='small')
plt.tight_layout()
plt.show()
'''
