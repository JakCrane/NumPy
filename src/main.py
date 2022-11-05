import numpy as np
import yfinance as yf #y for yahoo
import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use("seaborn")

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

close = stocks.loc[:,'Close'] #ignores all subcategories of information and only takes closing price. loc takes values from a dataset using the index arugment passed in
#closing price is the most accurate & standard in determining value over time
#the closing price doesnt reflect the impact of cash dividends, stock dividends or stock splits
close.plot()

plt.legend()
plt.savefig('plot1.png')

#print(close)

#normalising the prices. Dividing all the values by the starting one so we get percentage change
close.iloc(0,0) #i stands for intiger and loc stands for location
print(close.APPL.div(close.iloc(0,0)))