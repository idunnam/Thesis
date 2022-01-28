"""
This code is used for calculating the annual SEB component anomalies, with a reference period from 1961-1990, for monthly MAR data from 6 CMIP5 models and 5 CMIP6 models. The data is stored in new netCDF-files for each model.  
"""

# import packages
import xarray as xr
import numpy as np
import pandas as pd 

# ===== FUNCTIONS ====
#import neseccary functions 
from functions import annual_mean, ref_seasonal_mean
from mymask import *
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all/" ##Use this path for JupyterNotebook OLD !
#str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/" ##Use this path for .py  OLD!
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all_072021/" ##jupyter new w/cc
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"  #NYEST


#== from functions.py ==#
#list_var_preprocess = ['LWU', 'LWD','LHF','MSK', 'SWD','SHF', 'TT','AL2', 'ST', 'SF', 'RF', 'LON', 'LAT','SMB','RU', 'ME']#,'CU', 'CD', 'CM', 'ZZP', 'VVP', 'UUP', 'TTP'] 
#cloud
list_var_preprocess = ['MSK', 'TT','CC', 'COD', 'SF', 'RF', 'LON', 'LAT','CU', 'CD', 'CM', 'QQP', 'VVP', 'UUP', 'TTP','ME','SH'] 
#SMB
#list_var_preprocess = ['MSK', 'TT', 'SF', 'RF', 'LON', 'LAT','ME','SH','SMB','RU', 'ME','SU', 'RF'] 


def preprocess_HAD(ds):
    ds_new = ds[list_var_preprocess]
    ds_new['Y21_199'] = test['Y21_199']
    ds_new['X10_105'] = test['X10_105']
    return ds_new


HADGEM_SEB = xr.open_mfdataset(str_monthly + "MARv3.9-HadGEM2-*.nc", decode_times=False,
                               preprocess= preprocess_HAD, combine = 'by_coords')

# Add a copy of 2099 as 2100 in the HADGEM dataset. Last year is missing (2100)
dates_small = pd.date_range('1950-01-01', '2099-12-01', freq='MS')
HADGEM_SEB['TIME'] = dates_small
HADGEM_SEB_2100 = HADGEM_SEB.sel(TIME='2099')
HADGEM_SEB_2100['TIME'] = pd.date_range('2100-01-01', '2100-12-01', freq='MS')
HADGEM_SEB = HADGEM_SEB.merge(HADGEM_SEB_2100) 



"""
HADGEM_SW_net = HADGEM_SEB['SWD'] * ( 1- HADGEM_SEB['AL2']) 
HADGEM_SEB = HADGEM_SEB.assign(SW_net = HADGEM_SW_net)

HADGEM_LW_net = HADGEM_SEB['LWD'] - HADGEM_SEB['LWU'] 
HADGEM_SEB = HADGEM_SEB.assign(LW_net = HADGEM_LW_net)

HADGEM_net_flux = HADGEM_SEB['SW_net'] + HADGEM_SEB['LWD'] - HADGEM_SEB['LWU'] + HADGEM_SEB['SHF'] + HADGEM_SEB['LHF']
HADGEM_SEB = HADGEM_SEB.assign(NET_f = HADGEM_net_flux)

HADGEM_net_rad_flux = HADGEM_SEB['SW_net'] + HADGEM_SEB['LWD'] - HADGEM_SEB['LWU'] 
HADGEM_SEB = HADGEM_SEB.assign(NET_rad_f = HADGEM_net_rad_flux)

HADGEM_net_non_rad_flux = HADGEM_SEB['SHF'] + HADGEM_SEB['LHF']
HADGEM_SEB = HADGEM_SEB.assign(NET_non_rad_f = HADGEM_net_non_rad_flux)
#"""
"""
HADGEM_PR = HADGEM_SEB['SF'] + HADGEM_SEB['RF']
HADGEM_SEB = HADGEM_SEB.assign(PR = HADGEM_PR)

#Refreezing
HADGEM_RZ = (HADGEM_SEB['ME'] + HADGEM_SEB['RF']) - (HADGEM_SEB['RU'])
HADGEM_SEB = HADGEM_SEB.assign(RZ = HADGEM_RZ)
#"""


# ==== create reference period ===
# CMIP5
ref_HADGEM = HADGEM_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')


# ===========  MEAN ==================
# CMIP5
annual_HADGEM = annual_mean(HADGEM_SEB)

# ====== ANOMALIES ======
# CMIP5
HADGEM_anomaly = (annual_HADGEM - ref_HADGEM) *mymask_test.values 

# ====== create new netCDF files for storing anomalies for each model =====
# CMIP5
#HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_annual.nc')
HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_cloud_annual.nc')
#HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_SMB_annual.nc')