import numpy as np
def R_square(x, y, coeff):
    """
    coeff = coeff_CM.. 
    x= x_CM6                 
    y= y1_CM6
    """
    p = np.poly1d(coeff)                  
    curve = np.polyval(coeff, x)
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssres = np.sum((y - curve)**2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    R_square = 1 - ssres / sstot
    return np.round(R_square,2)