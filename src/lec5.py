#limit order books
#ask and spread orders

#limit order is executed if the price is desirable (set your limit) but may never execute
#market orders execute regardless upon arrival so arent stored
#information leakage selling large volumes signals there is a reason why they should sell (more a case of market orders than limit orders)
#only limit orders are 
#execution algorithms use both orders 
#large orders split into smaller orders is known as metaorders
#4 pieces of info on order: ticker/id price of limit size and time ordered
#markets only pair buyers and sellers and charge a fee for joining the market
#bacheliers model
#arithmetic brownian motion
#martingales
#stochastic
#central limit theorem
#limitations of bacheliers models based on gausian random walks grossly underestimate extreme fluctuations like -50% is 10^-30 chance of happening
#prices follow fat tailed power law distributions , market volatility isnt constant, markets dont reflect headlines 
#auto correlation function
#bacheliers first law
#volatility signature plots
#mean reversion and momentum

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import scienceplots

data = pd.read_csv("INTC_2015-01-02_34200000_57600000_orderbook_10.csv",
            names = list(itertools.chain(*[[f"{i}th best bid price", f"{i}th best bid volume", 
                                                   f"{i}th best ask price",f"{i}th best ask volume"]
                                            for i in range(1,11)])))
df = pd.DataFrame(index = data.index)
df['mid_price'] = data['1th best bid price'] - data['1th best ask price']
print(df.tail())
plt.plot(df)
plt.show()