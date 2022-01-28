import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc

from SEB_rad_flux_JJA import *
"""

#r-squared 
p = np.poly1d(coeff_CM6)
yhat = p(x_CM6)
ybar= np.sum(y1_CM6)/len(y1_CM6)
ssres = np.sum((y1_CM6 - curve_y1_CM6)**2)
sstot = np.sum((y1_CM6-ybar)**2)
print(1- ssres/ sstot)



coeff_CM6 = np.polyfit(x_CM6, y1_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)
curve_y1_CM6 = poly1_CM6(curve_x_CM6)
"""
#x = x_CM5
x = x_CM6
#y = [y1_CM5,y2_CM5,y3_CM5,y4_CM6,y5_CM5, y6_CM5]
y = [y1_CM6,y2_CM6,y3_CM6,y4_CM6,y5_CM6, y6_CM6]
degree = 2

for i in range(len(y)):
    coeffs = np.polyfit(x, y[i], degree)
    curve = np.polyval(coeffs, x)




 # r-squared
    p = np.poly1d(coeffs)
# fit values, and mean

    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y[i])/len(y[i])          # or sum(y)/len(y)
    ssres = np.sum((y[i] - curve)**2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y[i] - ybar)**2)
    print('R2:',1- ssres/ sstot)

#print(np.std(SWD_CMIP6))

