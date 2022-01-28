# import packages
import xarray as xr
import numpy as np
import pandas as pd 

# ===== FUNCTIONS ====
#import neseccary functions 
from functions import preprocess, preprocess_HAD, seasonal_mean, ref_seasonal_mean
from mymask import *
#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all/"
#str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/"
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"

# ==== Open CMIP5 models ==== 
#ACCESS_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-ACCESS13-*.nc", 
#                               decode_times= False, preprocess=preprocess, combine="by_coords") 

#CSIRO_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-CSIRO-*.nc", 
#                              decode_times= False, preprocess=preprocess, combine="by_coords") 

HADGEM_SEB = xr.open_mfdataset(str_monthly + "MARv3.9-HadGEM2-*.nc", decode_times=False, preprocess= preprocess_HAD, 
                               combine = 'by_coords')

# Add a copy of 2099 as 2100 in the HADGEM dataset. Last year is missing (2100)
dates_small = pd.date_range('1950-01-01', '2099-12-01', freq='MS')
HADGEM_SEB['TIME'] = dates_small
HADGEM_SEB_2100 = HADGEM_SEB.sel(TIME='2099')
HADGEM_SEB_2100['TIME'] = pd.date_range('2100-01-01', '2100-12-01', freq='MS')
HADGEM_SEB = HADGEM_SEB.merge(HADGEM_SEB_2100) 

#IPSL_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-IPSL-CM5-*.nc", 
#                             decode_times= False, preprocess=preprocess, combine="by_coords") 

#MIROC5_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-MIROC5-*.nc", 
#                               decode_times= False, preprocess=preprocess, combine="by_coords") 

#NORESM_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-NorESM1-*.nc", 
#                               decode_times= False, preprocess=preprocess, combine="by_coords") 



# ===== Open CMIP6 models ====
#CESM_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-CESM2-*.nc'
#                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

#CNRM_CM6_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-CNRM-CM6-*.nc'
#                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

#CNRM_ESM2_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-CNRM-ESM2-*.nc'
#                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

#MRI_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-MRI-*.nc'
#                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

#UKMO_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-UKMO-*.nc'
#                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

# ========== Calculate SW_net ===============    
#CMIP5
#ACCESS_SW_net = ACCESS_SEB['SWD'] * ( 1- ACCESS_SEB['AL2'])
#CSIRO_SW_net = CSIRO_SEB['SWD'] * ( 1- CSIRO_SEB['AL2']) 
HADGEM_SW_net = HADGEM_SEB['SWD'] * ( 1- HADGEM_SEB['AL2']) 
#IPSL_SW_net = IPSL_SEB['SWD'] * ( 1- IPSL_SEB['AL2'])
#MIROC5_SW_net = MIROC5_SEB['SWD'] * ( 1- MIROC5_SEB['AL2']) 
#NORESM_SW_net = NORESM_SEB['SWD'] * ( 1- NORESM_SEB['AL2'])

#CMIP6
#CESM_SW_net = CESM_SEB['SWD'] * ( 1- CESM_SEB['AL2']) 
#CNRM_CM6_SW_net = CNRM_CM6_SEB['SWD'] * ( 1- CNRM_CM6_SEB['AL2']) 
#CNRM_ESM2_SW_net = CNRM_ESM2_SEB['SWD'] * ( 1- CNRM_ESM2_SEB['AL2']) 
#MRI_SW_net = MRI_SEB['SWD'] * ( 1- MRI_SEB['AL2']) 
#UKMO_SW_net = UKMO_SEB['SWD'] * ( 1- UKMO_SEB['AL2']) 


# ==== ADD SW_net to dataset === 
#ACCESS_SEB = ACCESS_SEB.assign(SW_net = ACCESS_SW_net)
#CSIRO_SEB  = CSIRO_SEB.assign(SW_net = CSIRO_SW_net)
HADGEM_SEB = HADGEM_SEB.assign(SW_net = HADGEM_SW_net)
#IPSL_SEB   = IPSL_SEB.assign(SW_net = IPSL_SW_net)
#MIROC5_SEB = MIROC5_SEB.assign(SW_net = MIROC5_SW_net)
#NORESM_SEB = NORESM_SEB.assign(SW_net = NORESM_SW_net)

#CESM_SEB      = CESM_SEB.assign(SW_net = CESM_SW_net)
#CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(SW_net = CNRM_ESM2_SW_net)
#CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(SW_net = CNRM_ESM2_SW_net)
#MRI_SEB       = MRI_SEB.assign(SW_net = MRI_SW_net)
#UKMO_SEB      = UKMO_SEB.assign(SW_net = UKMO_SW_net)

# =========== Calculate Net energy flux ===============
#ACCESS_net_flux = ACCESS_SEB['SW_net'] + ACCESS_SEB['LWD'] - ACCESS_SEB['LWU'] + ACCESS_SEB['SHF'] + ACCESS_SEB['LHF']
#CSIRO_net_flux = CSIRO_SEB['SW_net'] + CSIRO_SEB['LWD'] - CSIRO_SEB['LWU'] + CSIRO_SEB['SHF'] + CSIRO_SEB['LHF']
HADGEM_net_flux = HADGEM_SEB['SW_net'] + HADGEM_SEB['LWD'] - HADGEM_SEB['LWU'] + HADGEM_SEB['SHF'] + HADGEM_SEB['LHF']
#IPSL_net_flux = IPSL_SEB['SW_net'] + IPSL_SEB['LWD'] - IPSL_SEB['LWU'] + IPSL_SEB['SHF'] + IPSL_SEB['LHF']
#MIROC5_net_flux = MIROC5_SEB['SW_net'] + MIROC5_SEB['LWD'] - MIROC5_SEB['LWU'] + MIROC5_SEB['SHF'] + MIROC5_SEB['LHF']
#NORESM_net_flux = NORESM_SEB['SW_net'] + NORESM_SEB['LWD'] - NORESM_SEB['LWU'] + NORESM_SEB['SHF'] + NORESM_SEB['LHF']

#CESM_net_flux = CESM_SEB['SW_net'] + CESM_SEB['LWD'] - CESM_SEB['LWU'] + CESM_SEB['SHF'] + CESM_SEB['LHF']
#CNRM_CM6_net_flux = CNRM_CM6_SEB['SW_net'] + CNRM_CM6_SEB['LWD'] - CNRM_CM6_SEB['LWU'] + CNRM_CM6_SEB['SHF'] + CNRM_CM6_SEB['LHF']
#CNRM_ESM2_net_flux = CNRM_ESM2_SEB['SW_net'] + CNRM_ESM2_SEB['LWD'] - CNRM_ESM2_SEB['LWU'] + CNRM_ESM2_SEB['SHF'] + CNRM_ESM2_SEB['LHF']
#MRI_net_flux = MRI_SEB['SW_net'] + MRI_SEB['LWD'] - MRI_SEB['LWU'] + MRI_SEB['SHF'] + MRI_SEB['LHF']
#UKMO_net_flux = UKMO_SEB['SW_net'] + UKMO_SEB['LWD'] - UKMO_SEB['LWU'] + UKMO_SEB['SHF'] + UKMO_SEB['LHF']

# ===== Add Net energy to dataset =======
#ACCESS_SEB = ACCESS_SEB.assign(NET_f = ACCESS_net_flux)
#CSIRO_SEB  = CSIRO_SEB.assign(NET_f = CSIRO_net_flux)
HADGEM_SEB = HADGEM_SEB.assign(NET_f = HADGEM_net_flux)
#IPSL_SEB   = IPSL_SEB.assign(NET_f = IPSL_net_flux)
#MIROC5_SEB = MIROC5_SEB.assign(NET_f = MIROC5_net_flux)
#NORESM_SEB = NORESM_SEB.assign(NET_f = NORESM_net_flux)

#CESM_SEB      = CESM_SEB.assign(NET_f = CESM_net_flux)
#CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(NET_f = CNRM_ESM2_net_flux)
#CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(NET_f = CNRM_ESM2_net_flux)
#MRI_SEB       = MRI_SEB.assign(NET_f = MRI_net_flux)
#UKMO_SEB      = UKMO_SEB.assign(NET_f = UKMO_net_flux)



# ===== Calculate total precipitation ==== # 
#ACCESS_PR = ACCESS_SEB['SF'] + ACCESS_SEB['RF']
#CSIRO_PR  = CSIRO_SEB['SF'] + CSIRO_SEB['RF']
HADGEM_PR = HADGEM_SEB['SF'] + HADGEM_SEB['RF']
#IPSL_PR   = IPSL_SEB['SF'] + IPSL_SEB['RF']
#MIROC5_PR = MIROC5_SEB['SF'] + MIROC5_SEB['RF']
#NORESM_PR = NORESM_SEB['SF'] + NORESM_SEB['RF']

#CMIP6
#CESM_PR      = CESM_SEB['SF'] + CESM_SEB['RF']
#CNRM_CM6_PR  = CNRM_CM6_SEB['SF'] + CNRM_CM6_SEB['RF'] 
#CNRM_ESM2_PR = CNRM_ESM2_SEB['SF'] + CNRM_ESM2_SEB['RF'] 
#MRI_PR       = MRI_SEB['SF'] + MRI_SEB['RF'] 
#UKMO_PR      = UKMO_SEB['SF'] + UKMO_SEB['RF'] 

# ===== Add precipitation to dataset =======
#ACCESS_SEB = ACCESS_SEB.assign(PR = ACCESS_PR)
#CSIRO_SEB  = CSIRO_SEB.assign(PR = CSIRO_PR)
HADGEM_SEB = HADGEM_SEB.assign(PR = HADGEM_PR)
#IPSL_SEB   = IPSL_SEB.assign(PR = IPSL_PR)
#MIROC5_SEB = MIROC5_SEB.assign(PR = MIROC5_PR)
#NORESM_SEB = NORESM_SEB.assign(PR = NORESM_PR)

#CESM_SEB      = CESM_SEB.assign(PR = CESM_PR)
#CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(PR = CNRM_ESM2_PR)
#CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(PR = CNRM_ESM2_PR)
#MRI_SEB       = MRI_SEB.assign(PR = MRI_PR)
#UKMO_SEB      = UKMO_SEB.assign(PR = UKMO_PR)




# === Set Datetime ===
#dates = pd.date_range('1950-01-01', '2100-12-01', freq='MS')

#list_SEB_CMIP5 = [ACCESS_SEB, CSIRO_SEB, IPSL_SEB, MIROC5_SEB, NORESM_SEB]
#list_SEB_CMIP6 = [CESM_SEB, CNRM_CM6_SEB, CNRM_ESM2_SEB, MRI_SEB, UKMO_SEB]


#for ds in list_SEB_CMIP5:
#    ds['TIME'] = dates

#for ds in list_SEB_CMIP6:
#    ds['TIME'] = dates
    
    
# ===== Create Reference period for JJA 1961-1990 =====

# CMIP5
#ref_seasonal_ACCESS = ACCESS_SEB.sel(TIME=slice('1961','1990'))
ref_seasonal_HADGEM = HADGEM_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_CSIRO  = CSIRO_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_IPSL   = IPSL_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_MIROC5 = MIROC5_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_NORESM = NORESM_SEB.sel(TIME=slice('1961','1990'))

#seas_ref_ACCESS =ref_seasonal_mean(ref_seasonal_ACCESS, 'JJA')
seas_ref_HADGEM =ref_seasonal_mean(ref_seasonal_HADGEM, 'JJA')
#seas_ref_CSIRO =ref_seasonal_mean(ref_seasonal_CSIRO, 'JJA')
#seas_ref_IPSL =ref_seasonal_mean(ref_seasonal_IPSL, 'JJA')
#seas_ref_MIROC5 =ref_seasonal_mean(ref_seasonal_MIROC5, 'JJA')
#seas_ref_NORESM =ref_seasonal_mean(ref_seasonal_NORESM, 'JJA')



#CMIP6
#ref_seasonal_CESM = CESM_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_CNRM_CM6 = CNRM_CM6_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_CNRM_ESM2 = CNRM_ESM2_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_MRI = MRI_SEB.sel(TIME=slice('1961','1990'))
#ref_seasonal_UKMO = UKMO_SEB.sel(TIME=slice('1961','1990'))

#seas_ref_CESM      = ref_seasonal_mean(ref_seasonal_CESM, 'JJA')
#seas_ref_CNRM_CM6  = ref_seasonal_mean(ref_seasonal_CNRM_CM6, 'JJA')
#seas_ref_CNRM_ESM2 = ref_seasonal_mean(ref_seasonal_CNRM_ESM2, 'JJA')
#seas_ref_MRI       = ref_seasonal_mean(ref_seasonal_MRI, 'JJA')
#seas_ref_UKMO      = ref_seasonal_mean(ref_seasonal_UKMO, 'JJA')


# ============ Pick 30 year period for further anomaly calcuation ======
#seasonal_2071_2100_ACCESS = ACCESS_SEB.sel(TIME=slice('2071','2100'))
seasonal_2071_2100_HADGEM = HADGEM_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_CSIRO  = CSIRO_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_IPSL   = IPSL_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_MIROC5 = MIROC5_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_NORESM = NORESM_SEB.sel(TIME=slice('2071','2100'))

#seas_2071_2100_ACCESS =ref_seasonal_mean(seasonal_2071_2100_ACCESS, 'JJA')
seas_2071_2100_HADGEM =ref_seasonal_mean(seasonal_2071_2100_HADGEM, 'JJA')
#seas_2071_2100_CSIRO =ref_seasonal_mean(seasonal_2071_2100_CSIRO, 'JJA')
#seas_2071_2100_IPSL =ref_seasonal_mean(seasonal_2071_2100_IPSL, 'JJA')
#seas_2071_2100_MIROC5 =ref_seasonal_mean(seasonal_2071_2100_MIROC5, 'JJA')
#seas_2071_2100_NORESM =ref_seasonal_mean(seasonal_2071_2100_NORESM, 'JJA')



#CMIP6
#seasonal_2071_2100_CESM = CESM_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_CNRM_CM6 = CNRM_CM6_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_CNRM_ESM2 = CNRM_ESM2_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_MRI = MRI_SEB.sel(TIME=slice('2071','2100'))
#seasonal_2071_2100_UKMO = UKMO_SEB.sel(TIME=slice('2071','2100'))

#seas_2071_2100_CESM      = ref_seasonal_mean(seasonal_2071_2100_CESM, 'JJA')
#seas_2071_2100_CNRM_CM6  = ref_seasonal_mean(seasonal_2071_2100_CNRM_CM6, 'JJA')
#seas_2071_2100_CNRM_ESM2 = ref_seasonal_mean(seasonal_2071_2100_CNRM_ESM2, 'JJA')
#seas_2071_2100_MRI       = ref_seasonal_mean(seasonal_2071_2100_MRI, 'JJA')
#seas_2071_2100_UKMO      = ref_seasonal_mean(seasonal_2071_2100_UKMO, 'JJA')

# ====== ANOMALIES ======
# CMIP5
#ACCESS_anomaly = (seas_2071_2100_ACCESS - seas_ref_ACCESS) *mymask_test.values 
HADGEM_anomaly = (seas_2071_2100_HADGEM - seas_ref_HADGEM) *mymask_test.values 
#CSIRO_anomaly  = (seas_2071_2100_CSIRO - seas_ref_CSIRO) *mymask_test.values
#IPSL_anomaly   = (seas_2071_2100_IPSL - seas_ref_IPSL) *mymask_test.values
#MIROC5_anomaly = (seas_2071_2100_MIROC5 - seas_ref_MIROC5) *mymask_test.values
#NORESM_anomaly = (seas_2071_2100_NORESM - seas_ref_NORESM) *mymask_test.values

#CMIP6
#CESM_anomaly      = (seas_2071_2100_CESM - seas_ref_CESM) *mymask_test.values
#CNRM_CM6_anomaly  = (seas_2071_2100_CNRM_CM6 - seas_ref_CNRM_CM6) *mymask_test.values
#CNRM_ESM2_anomaly = (seas_2071_2100_CNRM_ESM2 - seas_ref_CNRM_ESM2) *mymask_test.values
#MRI_anomaly       = (seas_2071_2100_MRI - seas_ref_MRI) *mymask_test.values
#UKMO_anomaly      = (seas_2071_2100_UKMO - seas_ref_UKMO) *mymask_test.values



# ====== create new netCDF files for storing anomalies for each model =====
# CMIP5
#ACCESS_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/ACCESS_JJA_2071_2100_anomaly.nc')
HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/HADGEM_JJA_2071_2100_anomaly.nc')
#CSIRO_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CSIRO_JJA_2071_2100_anomaly.nc')
#IPSL_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/IPSL_JJA_2071_2100_anomaly.nc')
#MIROC5_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/MIROC5_JJA_2071_2100_anomaly.nc')
#NORESM_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/NORESM_JJA_2071_2100_anomaly.nc')


#CMIP6
#CESM_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CESM_JJA_2071_2100_anomaly.nc')
#CNRM_CM6_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CNRM_CM6_JJA_2071_2100_anomaly.nc')
#CNRM_ESM2_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CNRM_ESM2_JJA_2071_2100_anomaly.nc')
#MRI_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/MRI_JJA_2071_2100_anomaly.nc')
#UKMO_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/UKMO_JJA_2071_2100_anomaly.nc')



