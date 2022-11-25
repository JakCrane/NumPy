#basic machine learning and linear regression
#machine acts like function
#needs training data to act like a function
#supervised learning: regression
# labelled training data is used to predict other data


# ~~~~ google ~~~~
#linear regression the equ 
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

revenue = np.array([2.6, 19. , 23.8, 26.9, 41.1, 58.3, 40.3, 58.7, 73.1, 69.7])
budget = np.array([5, 10, 17, 27, 35, 40, 42, 49, 54, 60])
df = pd.DataFrame(data = {"revenue":revenue, "budget":budget})
print(df)
plt.scatter(df.budget, df.revenue, 50)
plt.show()

