import numpy as np
import yfinance as yf #y for yahoo
import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use("seaborn") #old so not used anymore

# ------ initialising the data and simple datafram manipulation --------

ticker = ["AAPL", "BA", "KO", "GOOGL", "DIS", "XOM" ] #names of stocks u wanna download

stocks = yf.download(ticker, start = "2012-01-01", end = "2022-09-06")

#pandas package
#print(type(stocks)) # a dataframe from pandas package

#print(stocks.head()) # the head fun gets the first 5 rows and as many columns as it can

#print(stocks.tail()) # same as head but last 5

#np.savetxt('data.txt', stocks.head()) #only gives values not indexing

#print(stocks.swaplevel(1,0, axis=1)) #axis is like a boolian for rows or columns and the first two numbers are the rows that are getting swapped.
#this only works for 'index' (table titles) not for data values

#print(stocks.swaplevel(1,0, axis=1).sort_index(axis=1)) #first swaps the titles of the columns then groups the data by company not parameter looked at

stocks.index = pd.to_datetime(stocks.index) #changes (dict-like container) dataframe type to datetime object

#print(type(stocks.index))

#print(stocks.describe()) # describe spits out alot of simple numerical analysis of the dataset like mean std quartiles ect

# ------ close price analysis -------

close = stocks.loc[:,'Close'] #ignores all subcategories of information and only takes closing price. loc takes values from a dataset using the index arugment passed in
#closing price is the most accurate & standard in determining value over time
#the closing price doesnt reflect the impact of cash dividends, stock dividends or stock splits
#most volume traded in the closing auction so best guess at price
#close.plot()

#plt.legend()
#plt.show()

#print(close)

#---- normalising the prices. ----

#Dividing all the values by the starting one so we get percentage change
#close.iloc[0,0] #i stands for intiger and loc stands for location MUST BE [] NOT ()

#print(close.AAPL.div(close.iloc[0,0])) #normalising the apple data with the first datapoint using .div() fun

#norm = close.div(close.iloc[0,:]) #can use [0,:] or [0]
#norm.plot()
#plt.legend()
#plt.show()

# ---- the shift method -----
aapl = close.AAPL.copy().to_frame() #copy coppies, to_frame turns the series object into a dataframe type
aapl['lag1'] = aapl.shift(periods = 1)  # df[] adds a new column to a dataframe ~ shift() is only for dataframes periods is spaces axis 0/1 is axis
aapl['diff'] = aapl.AAPL.sub(aapl.lag1)
#print(aapl.loc[:,'diff'])
aapl["pct_change"] = aapl.AAPL.div(aapl.lag1).sub(1).mul(100) # %change from day to day
aapl.dropna() #dropna means it removes all rows with N/As in them
#print(aapl)
ret = aapl.loc[:,'pct_change'].dropna() #return is percentage change day by day
#print(ret)
ret.plot(kind = "hist",bins=100)
plt.legend()
plt.show()
daily_mean_return = ret.mean() #mean percentage change of stock price in a day
daily_var_return = ret.var() #variance of percentage change of stock price
daily_std_return = ret.std() #standard deviation of percentage change of stock price

#print(daily_mean_return)
#print(daily_std_return)

#to find annual return multiply by 252 as thats the number of days the stock market is open

descr = pd.DataFrame()

for a in ticker:
    #print(a)
    print(type(a))
    b = close.loc[:,a].copy().to_frame()
    descr[a + '_c_p'] = b
    b['lag1'] = b.shift(periods = 1)
    descr[a + '_lag'] = b.loc[:,'lag1']
    b['pct_change'] = b[a].div(b.lag1).sub(1).mul(100)
    descr[a + '_p_c'] = b.loc[:,'pct_change']

print(descr)

mean_std = pd.DataFrame(index=['Mean','STD'])
for a in ticker:
    b = descr[a+'_p_c'].mean()
    c = descr[a+'_p_c'].std()
    mean_std[a] = [b,c]

print(mean_std)

#basically cba doing the rest but rolling(k) is very important. it takes window of k size and can then .sum or.mean to find the avg

