# ==== CREATE A MASK for the Greenland Ice Sheet (GrIS) ==== 
import xarray as xr
import numpy as np
import pandas as pd

#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all/"
#str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/"
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all_072021/" ##jupyter new w/cc
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"
#test = xr.open_dataset(str_monthly + 'MARv3.9-monthly-ACCESS13-1954.nc', decode_times=False)
test = xr.open_dataset(str_monthly + 'MARv3.9-ACCESS13-1954.nc', decode_times=False)



mymask_test = test['MSK'] / 100
mymask_test.loc[dict(Y21_199=slice(1160, 1600),
                     X10_105=slice(-800, -420))] = np.nan
mymask_test.loc[dict(Y21_199=slice(1300, 1600),
                     X10_105=slice(-500, -330))] = np.nan
mymask_test.loc[dict(Y21_199=slice(1075, 1200),
                     X10_105=slice(-800, -710))] = np.nan
mymask_test.loc[dict(Y21_199=slice(1350, 1500),
                     X10_105=slice(-340, -300))] = np.nan

#new_GrIS
mymask_test = mymask_test.where(mymask_test > 0.1)
