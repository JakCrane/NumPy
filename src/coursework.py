import yfinance as yf
tickers = ["AAPL", "META", "GOOG", "AMZN", "MSFT", "TSLA" ]
df_all = yf.download(tickers, start = "2017-01-01", end = "2019-12-31")
df = df_all.loc[:,'Close']
for t in tickers:
    title1 = "{}_returns".format(t)
    title2 = "{}lag_1".format(t)

    df[title2] = df.loc[:,t].shift(periods = 1)
    df[title1] = df.loc[:,t].sub(df.loc[:,title2])