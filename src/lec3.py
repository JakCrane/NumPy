# ~~~~ google ~~~~
#gradient descent algorithm
#polynomial regression still using gradient descent
#pros and cons of linear vs polynomial
#overfitting/underfitting
#technical indicators can be incorporated
#classification [logisitc regression]
#sigmoid function and logisitic function
#decision boundary [linear/non-linear]
#simplified cost function
#multiclass classification
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import yfinance as yf


#   revenue = np.array([2.6, 19. , 23.8, 26.9, 41.1, 58.3, 40.3, 58.7, 73.1, 69.7])
#   budget = np.array([5, 10, 17, 27, 35, 40, 42, 49, 54, 60])
#   df = pd.DataFrame(data = {"revenue":revenue, "budget":budget})
#   
#   plt.figure( figsize = (12, 8))
#   plt.scatter(df.budget, df.revenue, 50)
#   plt.xlabel("Budget", fontsize = 13)
#   plt.ylabel("Revenue", fontsize = 13)
#   #plt.show()
#   plt.clf()
#   
#   
#   #linear regression is the least squares method which places more weight on having a low std of error instead of just low avg error
#   #it is also easy to itterate through to get a value but that value maynot always be the lowest error
#   
#   #can converge to local minima instead of global minima but 
#   lm = LinearRegression(fit_intercept = True) #if false data is expected to be centred (centred data has a mean of 0)
#   #initialised lm as an empty LinearRegression class with methods like fit, get_params, predict ect
#   lm.fit(X = df.budget.to_frame(), y = df.revenue) #method that fits a linear model (X = traning data, y = target values)
#   slope = lm.coef_
#   intercept = lm.intercept_
#   df['pred'] = lm.predict(df.budget.to_frame()) #taking the independant variable and trying to predict
#   plt.scatter(df.budget, df.revenue, 50)
#   plt.plot(df.budget, df.pred) #this line and the one below vv are absolutely identical
#   plt.plot(np.array([0, 50]), intercept + slope *([0, 50])) #    ^^
#   plt.show()


#  simple linear model to predict financial returns
#  GBPUSD = yf.download('GBPUSD=x','2022-10-06','2022-11-26',interval='5m')
#  data = pd.DataFrame(index = GBPUSD.index)
#  data['price'] = GBPUSD["Close"]
#  data["returns"] = np.log(data.div(data.shift(1)))
#  data["lag1"] = data.returns.shift(1)
#  data.dropna(inplace = True)
#  print(data.iloc[:, -2])
#  data.iloc[:, -2:].plot(kind = "scatter", x = "lag1", y = "returns")
#  #plt.show()
#  lm = LinearRegression(fit_intercept = True)
#  lm.fit(data.lag1.to_frame(), data.returns)
#  slope = lm.coef_
#  intercept = lm.intercept_
#  data["pred"] = lm.predict(data.lag1.to_frame())
#  plt.plot(data.lag1, data.pred, c = "red", label = "Linear Regression")
#  data[["returns", "pred"]].plot(figsize = (12, 8))
#  plt.show()
#  fails to predict magnitude of returns
#  fails to predict market directions

# A Multiple Regression Model to predict Financial Returns

GBPUSD = yf.download('GBPUSD=x','2022-10-07','2022-11-27',interval='5m')
data = pd.DataFrame(index = GBPUSD.index)
data['price'] = GBPUSD["Close"]
data["returns"] = np.log(data.div(data.shift(1)))
lags = 5
cols = []
for lag in range(1, lags + 1):
    col = "lag{}".format(lag) #format is applied to strings and adds what ever is in the brackets to what ever is in the curly brackets
    data[col] = data.returns.shift(lag)
    cols.append(col)

data.dropna(inplace = True)

lm = LinearRegression(fit_intercept = True)
lm.fit(data[cols], data.returns) #cols is list containing all lag collumns
print(lm.coef_, lm.intercept_)
data["pred"] = lm.predict(data[cols].values)
data.pred = np.sign(data.pred)
data.pred.value_counts()
hit = np.sign(data.returns * data.pred).value_counts()
hit_ratio = hit[1.0] / sum(hit) #
