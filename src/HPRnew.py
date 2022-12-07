import numpy as np
import matplotlib.pyplot as plt
import pickle
import math as m
import pandas as pd
import sys
import components.DataProcessing as calculateAandVmax 

class DataManipulation():
    def __init__(self,data = None):
        self.data = data
    
    def save_data(self, filename):
        with open(filename, 'wb') as write_file: #defining as read file but dont need varname.close() after it
            pickle.dump(self.data, write_file)      

    def set_data(self, data):
        self.data = data

    def load_data(self, filename):
        try:
            with open(filename, 'rb') as read_file: 
                self.data = pickle.load(read_file)
        except IOError:
            print('error openning file')

    
# ~~~ data
datamanip = DataManipulation()
datamanip.load_data('Engine_Data.p')
enginf = datamanip.data #enginf = engines information

#~~~ parameters
M = 1
Cd = 0.75
D = 0.043
rho = 1.29 
g = 9.81

params = [M,Cd,D,rho,g]

#~~~ number crunching

info = calculateAandVmax.calculateAandVmax(params,enginf)

#~~~ plotting 

plt.figure(figsize=(40,40))
print(info)
plt.scatter(info['Max Force'], info['V max'], color = 'red')
params[1] = 0.9
info = calculateAandVmax.calculateAandVmax(params,enginf)
print(info)
plt.scatter(info['Max Force'], info['V max'], color = 'blue')
plt.show()


