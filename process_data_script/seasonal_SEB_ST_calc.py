# import packages
import xarray as xr
import numpy as np
import pandas as pd 

# ===== FUNCTIONS ====
#import neseccary functions 
from functions import seasonal_mean, ref_seasonal_mean
from mymask import *
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all/"
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/"

list_var_preprocess = ['LWU', 'LWD','LHF','MSK', 'SWD','SHF', 'TT','AL2', 'ST']
def preprocess(ds):
    ds_new = ds[list_var_preprocess]
    return ds_new
def preprocess_HAD(ds):
    ds_new = ds[list_var_preprocess]
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

# ========== Calculate SW_net ===============    
#CMIP5
ACCESS_SW_net = ACCESS_SEB['SWD'] * ( 1- ACCESS_SEB['AL2'])
CSIRO_SW_net = CSIRO_SEB['SWD'] * ( 1- CSIRO_SEB['AL2']) 
HADGEM_SW_net = HADGEM_SEB['SWD'] * ( 1- HADGEM_SEB['AL2']) 
IPSL_SW_net = IPSL_SEB['SWD'] * ( 1- IPSL_SEB['AL2'])
MIROC5_SW_net = MIROC5_SEB['SWD'] * ( 1- MIROC5_SEB['AL2']) 
NORESM_SW_net = NORESM_SEB['SWD'] * ( 1- NORESM_SEB['AL2'])

#CMIP6
CESM_SW_net = CESM_SEB['SWD'] * ( 1- CESM_SEB['AL2']) 
CNRM_CM6_SW_net = CNRM_CM6_SEB['SWD'] * ( 1- CNRM_CM6_SEB['AL2']) 
CNRM_ESM2_SW_net = CNRM_ESM2_SEB['SWD'] * ( 1- CNRM_ESM2_SEB['AL2']) 
MRI_SW_net = MRI_SEB['SWD'] * ( 1- MRI_SEB['AL2']) 
UKMO_SW_net = UKMO_SEB['SWD'] * ( 1- UKMO_SEB['AL2']) 


# ==== ADD SW_net to dataset === 
ACCESS_SEB = ACCESS_SEB.assign(SW_net = ACCESS_SW_net)
CSIRO_SEB  = CSIRO_SEB.assign(SW_net = CSIRO_SW_net)
HADGEM_SEB = HADGEM_SEB.assign(SW_net = HADGEM_SW_net)
IPSL_SEB   = IPSL_SEB.assign(SW_net = IPSL_SW_net)
MIROC5_SEB = MIROC5_SEB.assign(SW_net = MIROC5_SW_net)
NORESM_SEB = NORESM_SEB.assign(SW_net = NORESM_SW_net)

CESM_SEB      = CESM_SEB.assign(SW_net = CESM_SW_net)
CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(SW_net = CNRM_ESM2_SW_net)
CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(SW_net = CNRM_ESM2_SW_net)
MRI_SEB       = MRI_SEB.assign(SW_net = MRI_SW_net)
UKMO_SEB      = UKMO_SEB.assign(SW_net = UKMO_SW_net)


# === Set Datetime ===
dates = pd.date_range('1950-01-01', '2100-12-01', freq='MS')

list_SEB_CMIP5 = [ACCESS_SEB, CSIRO_SEB, IPSL_SEB, MIROC5_SEB, NORESM_SEB]
list_SEB_CMIP6 = [CESM_SEB, CNRM_CM6_SEB, CNRM_ESM2_SEB, MRI_SEB, UKMO_SEB]


for ds in list_SEB_CMIP5:
    ds['TIME'] = dates

for ds in list_SEB_CMIP6:
    ds['TIME'] = dates


# ===== Create Reference period for JJA 1961-1990 =====

# CMIP5
ref_seasonal_ACCESS = ACCESS_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_HADGEM = HADGEM_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_CSIRO  = CSIRO_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_IPSL   = IPSL_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_MIROC5 = MIROC5_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_NORESM = NORESM_SEB.sel(TIME=slice('1961','1990'))

seas_ref_ACCESS =ref_seasonal_mean(ref_seasonal_ACCESS, 'JJA')
seas_ref_HADGEM =ref_seasonal_mean(ref_seasonal_HADGEM, 'JJA')
seas_ref_CSIRO =ref_seasonal_mean(ref_seasonal_CSIRO, 'JJA')
seas_ref_IPSL =ref_seasonal_mean(ref_seasonal_IPSL, 'JJA')
seas_ref_MIROC5 =ref_seasonal_mean(ref_seasonal_MIROC5, 'JJA')
seas_ref_NORESM =ref_seasonal_mean(ref_seasonal_NORESM, 'JJA')



#CMIP6
ref_seasonal_CESM = CESM_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_CNRM_CM6 = CNRM_CM6_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_CNRM_ESM2 = CNRM_ESM2_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_MRI = MRI_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_UKMO = UKMO_SEB.sel(TIME=slice('1961','1990'))

seas_ref_CESM      = ref_seasonal_mean(ref_seasonal_CESM, 'JJA')
seas_ref_CNRM_CM6  = ref_seasonal_mean(ref_seasonal_CNRM_CM6, 'JJA')
seas_ref_CNRM_ESM2 = ref_seasonal_mean(ref_seasonal_CNRM_ESM2, 'JJA')
seas_ref_MRI       = ref_seasonal_mean(ref_seasonal_MRI, 'JJA')
seas_ref_UKMO      = ref_seasonal_mean(ref_seasonal_UKMO, 'JJA')

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

# ====== ANOMALIES ======
# CMIP5
ACCESS_anomaly = (seas_ACCESS - seas_ref_ACCESS) *mymask_test.values 
HADGEM_anomaly = (seas_HADGEM - seas_ref_HADGEM) *mymask_test.values 
CSIRO_anomaly  = (seas_CSIRO - seas_ref_CSIRO) *mymask_test.values
IPSL_anomaly   = (seas_IPSL - seas_ref_IPSL) *mymask_test.values
MIROC5_anomaly = (seas_MIROC5 - seas_ref_MIROC5) *mymask_test.values
NORESM_anomaly = (seas_NORESM - seas_ref_NORESM) *mymask_test.values

#CMIP6
CESM_anomaly      = (seas_CESM - seas_ref_CESM) *mymask_test.values
CNRM_CM6_anomaly  = (seas_CNRM_CM6 - seas_ref_CNRM_CM6) *mymask_test.values
CNRM_ESM2_anomaly = (seas_CNRM_ESM2 - seas_ref_CNRM_ESM2) *mymask_test.values
MRI_anomaly       = (seas_MRI - seas_ref_MRI) *mymask_test.values
UKMO_anomaly      = (seas_UKMO - seas_ref_UKMO) *mymask_test.values

# ====== create new netCDF files for storing anomalies for each model =====
# CMIP5
ACCESS_anomaly.to_netcdf('ACCESS_anomaly_JJA_inc_ST.nc')
HADGEM_anomaly.to_netcdf('HADGEM_anomaly_JJA_inc_ST.nc')
CSIRO_anomaly.to_netcdf('CSIRO_anomaly_JJA_inc_ST.nc')
IPSL_anomaly.to_netcdf('IPSL_anomaly_JJA_inc_ST.nc')
MIROC5_anomaly.to_netcdf('MIROC5_anomaly_JJA_inc_ST.nc')
NORESM_anomaly.to_netcdf('NORESM_anomaly_JJA_inc_ST.nc')


#CMIP6
CESM_anomaly.to_netcdf('CESM_anomaly_JJA_inc_ST.nc')
CNRM_CM6_anomaly.to_netcdf('CNRM_CM6_anomaly_JJA_inc_ST.nc')
CNRM_ESM2_anomaly.to_netcdf('CNRM_ESM2_anomaly_JJA_inc_ST.nc')
MRI_anomaly.to_netcdf('MRI_anomaly_JJA_inc_ST.nc')
UKMO_anomaly.to_netcdf('UKMO_anomaly_JJA_inc_ST.nc')