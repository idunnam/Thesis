"""
Set of functions. 

preprocess: used to select variable names to import when importing the MAR data files
prepocess_HAD: used specifically for HADGEM import, duplicates the last year to get a full timeseries ending at year 2100

annual_sum: calculates the sum of all years in the data
seasonal_sum: calculates the summ of every season in the data

annual_mean  : calculates the mean of every year in the data 
seasonal_mean: calculates the mean of each season in every year in the data 
annual_mean  : calculates the mean of each season in every year in the reference period
"""

import xarray as xr
import numpy as np

#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all_072021/" ##jupyter new w/cc
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"  #NYEST
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all/"

#test = xr.open_dataset(str_monthly + 'MARv3.9-monthly-ACCESS13-1954.nc', decode_times=False)
test = xr.open_dataset(str_monthly + 'MARv3.9-ACCESS13-1954.nc', decode_times=False)



#======== Preprocess ==============
# list of variables must be defined before using these functions
list_var_preprocess = ['LWU', 'LWD','LHF','MSK', 'SWD','SHF', 'TT','AL2', 'ST', 'CC', 'COD', 'SF', 'RF', 'LON', 'LAT','CU', 'CD', 'CM','QQP', 'ZZP', 'VVP', 'UUP', 'TTP', 'SH', 'ME', 'SMB', 'RU','RF','SU'] 

def preprocess(ds):
    ds_new = ds[list_var_preprocess]
    return ds_new
def preprocess_HAD(ds):
    ds_new = ds[list_var_preprocess]
    ds_new['Y21_199'] = test['Y21_199']
    ds_new['X10_105'] = test['X10_105']
    return ds_new


# ======== SUM ================

def annual_sum(data):
    annual_sum = data.groupby('TIME.year').sum(dim='TIME')
    return annual_sum


def seasonal_sum(data, season):
    seasonal_sum = data.where(data['TIME.season'] == season).groupby(
        'TIME.year').sum(dim='TIME')
    return seasonal_sum


#======= MEAN =================
def annual_mean(data):
    annual_mean = data.groupby('TIME.year').mean(dim='TIME')
    return annual_mean


def seasonal_mean(data, season):
    seasonal_mean = data.where(data['TIME.season'] == season).groupby(
        'TIME.year').mean(dim='TIME')
    return seasonal_mean


def ref_seasonal_mean(data, season):
    seasonal_mean = data.where(data['TIME.season'] == season).groupby(
        'TIME.year').mean(dim='TIME').mean(dim='year')
    return seasonal_mean



