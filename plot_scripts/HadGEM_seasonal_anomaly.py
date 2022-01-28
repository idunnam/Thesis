# import packages
import xarray as xr
import numpy as np
import pandas as pd 

# ===== FUNCTIONS ====
#import neseccary functions 
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all/"
#str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/"
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"  #NYEST

season = 'JJA'

#== from mymask.py ==#
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
#======================#


#== from functions.py ==#
#list_var_preprocess = ['LWU', 'LWD','LHF','MSK', 'SWD','SHF', 'TT','AL2', 'ST', 'SF', 'RF', 'LON', 'LAT','SMB','RU', 'ME']#,'CU', 'CD', 'CM', 'ZZP', 'VVP', 'UUP', 'TTP'] 
#cloud
list_var_preprocess = ['MSK', 'TT','CC', 'COD', 'SF', 'RF', 'LON', 'LAT','CU', 'CD', 'CM', 'ZZP', 'QQP', 'VVP', 'UUP', 'TTP','ME','SH'] 

#list_var_preprocess = ['MSK', 'TT', 'SF', 'RF', 'LON', 'LAT','ME','SH','SMB','RU', 'ME','SU', 'RF'] 

def preprocess_HAD(ds):
    ds_new = ds[list_var_preprocess]
    ds_new['Y21_199'] = test['Y21_199']
    ds_new['X10_105'] = test['X10_105']
    return ds_new

def seasonal_mean(data, season):
    seasonal_mean = data.where(data['TIME.season'] == season).groupby(
        'TIME.year').mean(dim='TIME')
    return seasonal_mean


def ref_seasonal_mean(data, season):
    seasonal_mean = data.where(data['TIME.season'] == season).groupby(
        'TIME.year').mean(dim='TIME').mean(dim='year')
    return seasonal_mean

#========================#


HADGEM_SEB = xr.open_mfdataset(str_monthly + "MARv3.9-HadGEM2-*.nc", decode_times=False, preprocess= preprocess_HAD, 
                               combine = 'by_coords')

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

#Total Preciptation
HADGEM_PR = HADGEM_SEB['SF'] + HADGEM_SEB['RF']
HADGEM_SEB = HADGEM_SEB.assign(PR = HADGEM_PR)

#Refreezing
HADGEM_RZ = (HADGEM_SEB['ME'] + HADGEM_SEB['RF']) - (HADGEM_SEB['RU'])
HADGEM_SEB = HADGEM_SEB.assign(RZ = HADGEM_RZ)
#"""

ref_seasonal_HADGEM = HADGEM_SEB.sel(TIME=slice('1961','1990'))
seas_ref_HADGEM =ref_seasonal_mean(ref_seasonal_HADGEM, season)
seas_HADGEM = seasonal_mean(HADGEM_SEB, season)

HADGEM_anomaly = (seas_HADGEM - seas_ref_HADGEM) *mymask_test.values 

#HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'.nc')

HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_cloud.nc')

#HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_SMB.nc')
