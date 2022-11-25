import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


SP500 = yf.download("^GSPC", start = "2012-01-01", end = "2022-09-06")
SP500 = SP500.Close.to_frame()

#SP500.plot()
#plt.show()

# ~~~~~ simple moving avg ~~~~~
# mean of rolling window

#SP500['sma50'] = SP500.rolling(window = 50, min_periods = 50).mean()
#SP500['sma200'] = SP500.Close.rolling(window = 200, min_periods = 20).mean() #min period is min number of data points to provide an answer and is set to window size by default

# ~~~~~~~ exponentially weighted moving avg ~~~~~~~
# avg but more weight on more recent data

#SP500['ema50'] = SP500.Close.ewm(span = 100).mean() #less sensitive to large spikes in close price



# ~~~~~~ mean reversion strategy ~~~~~~~
#assumes prices stay constant so when its far from mean then it will revert back to mean
#long when low and short when high then sell when it hits the mean
#using bollinger bands to decide when to sell
#3 bands middle (10 day moving avg) upper and lower (one std from the middle band)
k = 50

SP500[str(k) +'sma'] = SP500.rolling(window = k, min_periods = k).mean()
SP500['upper_band'] = SP500[str(k)+'sma'].add(SP500.Close.rolling(window = k).std().div(4))
SP500['lower_band'] = SP500[str(k)+'sma'].sub(SP500.Close.rolling(window = k).std().div(4))
#SP500['position'] = np.where(SP500.Close < SP500.lower_band, 1, np.nan)
#SP500['position'] = np.where(SP500.Close > SP500.upper_band, -1, np.nan)
#SP500['position'] = np.where(SP500.Close == SP500[str(k) +'sma'], 0, np.nan)
SP500['position'] = 0
SP500.iloc[0,4] = 0
SP500.iloc[2685,4] = 0

for i in range(0,2685):
    if SP500.Close[i] > SP500.upper_band[i]:
        SP500.position[i] = -1
    elif SP500.Close[i] < SP500.lower_band[i]:
        SP500.position[i] = 1
    elif SP500.Close[i] > SP500[str(k) +'sma'][i] and SP500.Close[i+1] < SP500[str(k) +'sma'][i+1]:
        SP500.position[i] = 0
    elif SP500.Close[i] < SP500[str(k) +'sma'][i] and SP500.Close[i+1] > SP500[str(k) +'sma'][i+1]:
        SP500.position[i] = 0
    else:
        SP500.position[i] = SP500.position[i-1]



print(SP500)

SP500.position.plot()
plt.show()