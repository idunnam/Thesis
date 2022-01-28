import xarray as xr 
from mymask import *


#== import 30yr amonalies (2071-2100) ==#
#seasonal_anomaly/ACCESS_anomaly_JJA.nc
#CMIP5 models

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
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"  #NYEST



# ==== Open CMIP5 models ==== 
ACCESS_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-ACCESS13-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 

CSIRO_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-CSIRO-*.nc", 
                              decode_times= False, preprocess=preprocess, combine="by_coords") 

HADGEM_SEB = xr.open_mfdataset(str_monthly + "MARv3.9-HadGEM2-*.nc", decode_times=False, preprocess= preprocess_HAD, 
                               combine = 'by_coords')

# Add a copy of 2099 as 2100 in the HADGEM dataset. Last year is missing (2100)
dates_small = pd.date_range('1950-01-01', '2099-12-01', freq='MS')
HADGEM_SEB['TIME'] = dates_small
HADGEM_SEB_2100 = HADGEM_SEB.sel(TIME='2099')
HADGEM_SEB_2100['TIME'] = pd.date_range('2100-01-01', '2100-12-01', freq='MS')
HADGEM_SEB = HADGEM_SEB.merge(HADGEM_SEB_2100) 

IPSL_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-IPSL-CM5-*.nc", 
                             decode_times= False, preprocess=preprocess, combine="by_coords") 

MIROC5_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-MIROC5-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 

NORESM_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-NorESM1-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 



# ===== Open CMIP6 models ====
CESM_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-CESM2-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

CNRM_CM6_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-CNRM-CM6-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

CNRM_ESM2_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-CNRM-ESM2-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

MRI_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-MRI-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')

UKMO_SEB = xr.open_mfdataset(str_monthly +'MARv3.9-UKMO-*.nc'
                         ,decode_times=False,preprocess=preprocess, combine='by_coords')


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

"""

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
ACCESS_anomaly = (seas_ACCESS - seas_ref_ACCESS)  
HADGEM_anomaly = (seas_HADGEM - seas_ref_HADGEM)  
CSIRO_anomaly  = (seas_CSIRO - seas_ref_CSIRO) 
IPSL_anomaly   = (seas_IPSL - seas_ref_IPSL) 
MIROC5_anomaly = (seas_MIROC5 - seas_ref_MIROC5) 
NORESM_anomaly = (seas_NORESM - seas_ref_NORESM) 

#CMIP6
CESM_anomaly      = (seas_CESM - seas_ref_CESM) 
CNRM_CM6_anomaly  = (seas_CNRM_CM6 - seas_ref_CNRM_CM6) 
CNRM_ESM2_anomaly = (seas_CNRM_ESM2 - seas_ref_CNRM_ESM2) 
MRI_anomaly       = (seas_MRI - seas_ref_MRI) 
UKMO_anomaly      = (seas_UKMO - seas_ref_UKMO) 

## ===== ICE SHEET ===== ##
ACCESS_gris = ACCESS_anomaly *mymask_test  
HADGEM_gris = HADGEM_anomaly *mymask_test  
CSIRO_gris  = CSIRO_anomaly  *mymask_test
IPSL_gris   = IPSL_anomaly *mymask_test  
MIROC5_gris = MIROC5_anomaly *mymask_test
NORESM_gris = NORESM_anomaly *mymask_test


CESM_gris = CESM_anomaly *mymask_test     
CNRM_CM6_gris = CNRM_CM6_anomaly *mymask_test 
CNRM_ESM2_gris = CNRM_ESM2_anomaly *mymask_test
MRI_gris = MRI_anomaly *mymask_test      
UKMO_gris = UKMO_anomaly *mymask_test    


ACCESS = ACCESS_anomaly.where((ACCESS_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (ACCESS_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 
HADGEM = HADGEM_anomaly.where((HADGEM_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (HADGEM_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)  
                         


CSIRO  = CSIRO_anomaly.where((CSIRO_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                     (CSIRO_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
IPSL   = IPSL_anomaly.where((IPSL_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                    (IPSL_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 

MIROC5 = MIROC5_anomaly.where((MIROC5_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (MIROC5_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 

NORESM = NORESM_anomaly.where((NORESM_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (NORESM_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 

#CMIP6

CESM      = CESM_anomaly.where((CESM_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                       (CESM_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
CNRM_ESM2 = CNRM_ESM2_anomaly.where((CNRM_ESM2_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                            (CNRM_ESM2_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
CNRM_CM6  = CNRM_CM6_anomaly.where((CNRM_CM6_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                           (CNRM_CM6_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
MRI       = MRI_anomaly.where((MRI_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (MRI_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                         
UKMO      = UKMO_anomaly.where((UKMO_gris.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                       (UKMO_gris.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 
"""

"""

#CMIP5
ACCESS = ACCESS_anomaly.where((ACCESS_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (ACCESS_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 
HADGEM = HADGEM_anomaly.where((HADGEM_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (HADGEM_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)  
                         


CSIRO  = CSIRO_anomaly.where((CSIRO_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                     (CSIRO_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
IPSL   = IPSL_anomaly.where((IPSL_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                    (IPSL_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 

MIROC5 = MIROC5_anomaly.where((MIROC5_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (MIROC5_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 

NORESM = NORESM_anomaly.where((NORESM_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (NORESM_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True) 

#CMIP6

CESM      = CESM_anomaly.where((CESM_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                       (CESM_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
CNRM_ESM2 = CNRM_ESM2_anomaly.where((CNRM_ESM2_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                            (CNRM_ESM2_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
CNRM_CM6  = CNRM_CM6_anomaly.where((CNRM_CM6_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                           (CNRM_CM6_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          
MRI       = MRI_anomaly.where((MRI_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                      (MRI_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                         
UKMO      = UKMO_anomaly.where((UKMO_anomaly.TT.mean(dim=['X10_105','Y21_199']) >=4)&
                       (UKMO_anomaly.TT.mean(dim=['X10_105','Y21_199']) <= 5.), drop=True)                          

print('Year for each model with warming between 4-5deg')
print('ACCESS:', ACCESS.year.values)
print('HADGEM:', HADGEM.year.values)
#print('HADGEM_cloud:', HADGEM_cloud.year.values)
print('CSIRO:', CSIRO.year.values)
print('IPSL:', IPSL.year.values)
print('MIROC5:', MIROC5.year.values)
print('NORESM:', NORESM.year.values)

print('CESM:', CESM.year.values)
print('CNRM_ESM2:', CNRM_ESM2.year.values)
print('CNRM_CM6:', CNRM_CM6.year.values)
print('MRI:', MRI.year.values)
print('UKMO', UKMO.year.values)
"""
"""
Year for each model with warming between 4-5deg

ACCESS: [2060 2075 2076 2082 2083 2085 2088 2090 2091 2093 2097 2098 2099]
HADGEM: [2057 2059 2062 2064 2068 2070 2072 2074 2075 2076 2077 2082 2083 2087 2088]
CSIRO: [2073 2078 2079 2083 2088 2093 2096]
IPSL: [2060 2061 2062 2063 2064 2065 2066 2067 2069 2070 2071 2072 2073 2074 2079 2080 2082 2086 2089 2095]
MIROC5: [2056 2060 2065 2066 2067 2073 2076 2078 2079 2081 2084 2090]
NORESM: [2078 2081 2083 2085 2089 2092 2095]
CESM: [2033 2044 2046 2054 2055 2058 2061 2063 2067 2068 2070 2071 2072 2073 2074 2080]
CNRM_ESM2: [2059 2066 2068 2073 2074 2076 2077 2078 2079 2080 2086]
CNRM_CM6: [2066 2073 2074 2090]
MRI: [2053 2060 2063 2067 2068 2071 2072 2075 2076 2079 2080 2081 2082 2083 2084 2085 2086 2090 2092 2093 2095 2098]
UKMO [2038 2039 2040 2041 2043 2047 2048 2049 2050 2055 2056 2057]
"""
"""
ACCESS.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ACCESS_full_1_deg_anomalies.nc')
HADGEM.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/HADGEM_full_1_deg_anomalies.nc')
CSIRO.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/CSIRO_full_1_deg_anomalies.nc')
IPSL.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/IPSL_full_1_deg_anomalies.nc')
MIROC5.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/MIROC5_full_1_deg_anomalies.nc')
NORESM.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/NORESM_full_1_deg_anomalies.nc')

CESM.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/CESM_full_1_deg_anomalies.nc')
CNRM_ESM2.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/CNRM_ESM2_full_1_deg_anomalies.nc')
CNRM_CM6.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/CNRM_CM6_full_1_deg_anomalies.nc')
MRI.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/MRI_full_1_deg_anomalies.nc')
UKMO.mean(dim='year').to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/UKMO_full_1_deg_anomalies.nc')
"""



#### REF VALUES ###
seas_ref_ACCESS.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_ACCESS.nc')  
seas_ref_HADGEM.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_HADGEM.nc')  
seas_ref_CSIRO.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_CSIRO.nc') 
seas_ref_IPSL.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_IPSL.nc') 
seas_ref_MIROC5.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_MIROC5.nc')
seas_ref_NORESM.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_NORESM.nc') 

#CMIP6
seas_ref_CESM.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_CESM.nc')
seas_ref_CNRM_CM6.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_CNRM_CM6.nc') 
seas_ref_CNRM_ESM2.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_CNRM_ESM2.nc')
seas_ref_MRI.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_MRI.nc') 
seas_ref_UKMO.to_netcdf('/projects/NS9600K/idunnam/src/full_1_deg/ref/ref_UKMO.nc') 