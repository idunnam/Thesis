"""
This code is used for creating new netCDF files for seasonal (JJA) mean of COD, CC and TT, for each of the CMIP5 and CMIP6 models.
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc

# ===== FUNCTIONS ====
#import neseccary functions 
from functions import seasonal_mean, ref_seasonal_mean
from mymask import *

str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/"

cloud_prep = ['COD','CC' ,'TT']
def preprocess(ds):
    ds_new = ds[cloud_prep]
    return ds_new
def preprocess_HAD(ds):
    ds_new = ds[cloud_prep]
    ds_new['Y21_199'] = test['Y21_199']
    ds_new['X10_105'] = test['X10_105']
    return ds_new


# ==== Open CMIP5 models ==== 
ACCESS_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-monthly-ACCESS13-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 

CSIRO_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-monthly-CSIRO-*.nc", 
                              decode_times= False, preprocess=preprocess, combine="by_coords") 

HADGEM_SEB = xr.open_mfdataset(str_monthly + "MARv3.9-monthly-HadGEM2-*.nc", decode_times=False, preprocess= preprocess_HAD, 
                               combine = 'by_coords')

# Add a copy of 2099 as 2100 in the HADGEM dataset. Last year is missing (2100)
dates_small = pd.date_range('1950-01-01', '2099-12-01', freq='MS')
HADGEM_SEB['TIME'] = dates_small
HADGEM_SEB_2100 = HADGEM_SEB.sel(TIME='2099')
HADGEM_SEB_2100['TIME'] = pd.date_range('2100-01-01', '2100-12-01', freq='MS')
HADGEM_SEB = HADGEM_SEB.merge(HADGEM_SEB_2100) 

IPSL_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-monthly-IPSL-CM5-*.nc", 
                             decode_times= False, preprocess=preprocess, combine="by_coords") 

MIROC5_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-monthly-MIROC5-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 

NORESM_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-monthly-NorESM1-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 

# ===== Open CMIP6 models ====
CESM_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-monthly-CESM2-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

CNRM_CM6_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-monthly-CNRM-CM6-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

CNRM_ESM2_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-monthly-CNRM-ESM2-*.nc'
                                  ,decode_times=False,preprocess=preprocess, combine='by_coords')

MRI_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-monthly-MRI-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

UKMO_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-monthly-UKMO-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')


# === Set Datetime ===
dates = pd.date_range('1950-01-01', '2100-12-01', freq='MS')

list_SEB_CMIP5 = [ACCESS_SEB, HADGEM_SEB, CSIRO_SEB, IPSL_SEB, MIROC5_SEB, NORESM_SEB]
list_SEB_CMIP6 = [CESM_SEB, CNRM_CM6_SEB, CNRM_ESM2_SEB, MRI_SEB, UKMO_SEB]

for ds in list_SEB_CMIP5:
    ds['TIME'] = dates

for ds in list_SEB_CMIP6:
    ds['TIME'] = dates
CESM_SEB['TIME'] = dates


# =========== SEASONAL MEAN ==================
# CMIP5
seas_ACCESS = seasonal_mean(ACCESS_SEB, 'JJA')
seas_HADGEM = seasonal_mean(HADGEM_SEB, 'JJA')
seas_CSIRO  = seasonal_mean(CSIRO_SEB, 'JJA')
seas_IPSL   = seasonal_mean(IPSL_SEB, 'JJA')
seas_MIROC5 = seasonal_mean(MIROC5_SEB, 'JJA')
seas_NORESM = seasonal_mean(NORESM_SEB, 'JJA')

#CMIP6
seas_CESM      = seasonal_mean(CESM_SEB, 'JJA')
seas_CNRM_CM6  = seasonal_mean(CNRM_CM6_SEB, 'JJA')
seas_CNRM_ESM2 = seasonal_mean(CNRM_ESM2_SEB, 'JJA')
seas_MRI       = seasonal_mean(MRI_SEB, 'JJA')
seas_UKMO      = seasonal_mean(UKMO_SEB, 'JJA')


seas_ACCESS.to_netcdf('seas_ACCESS.nc')
seas_HADGEM.to_netcdf('seas_HADGEM.nc')
seas_CSIRO.to_netcdf('seas_CSIRO.nc')
seas_IPSL.to_netcdf('seas_IPSL.nc')
seas_MIROC5.to_netcdf('seas_MIROC5.nc')
seas_NORESM.to_netcdf('seas_NORESM.nc')

seas_CESM.to_netcdf('seas_CESM.nc')
seas_CNRM_CM6.to_netcdf('seas_CNRM_CM6.nc')
seas_CNRM_ESM2.to_netcdf('seas_CNRM_ESM2.nc')
seas_MRI.to_netcdf('seas_MRI.nc')
seas_UKMO.to_netcdf('seas_UKMO.nc')