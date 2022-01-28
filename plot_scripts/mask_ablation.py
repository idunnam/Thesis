import xarray as xr
import numpy as np
import pandas as pd

from functions import preprocess, preprocess_HAD

#str_monthly = "/mnt/mcc-ns9600k/shofer/Paper_CMIP6/MAR/monthly_all_072021/" ##jupyter new w/cc
str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"


# ==== Open CMIP5 models ==== 
ACCESS_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-ACCESS13-*.nc", 
                               decode_times= False, preprocess=preprocess, combine="by_coords") 

CSIRO_SEB = xr.open_mfdataset(str_monthly +"MARv3.9-CSIRO-*.nc", 
                              decode_times= False, preprocess=preprocess, combine="by_coords") 
#HADGEM_SEB = xr.open_mfdataset(str_monthly + "MARv3.9-HadGEM2-*.nc", decode_times=False, preprocess= preprocess_HAD, combine = 'by_coords')

# Add a copy of 2099 as 2100 in the HADGEM dataset. Last year is missing (2100)
#dates_small = pd.date_range('1950-01-01', '2099-12-01', freq='MS')
#HADGEM_SEB['TIME'] = dates_small
#HADGEM_SEB_2100 = HADGEM_SEB.sel(TIME='2099')
#HADGEM_SEB_2100['TIME'] = pd.date_range('2100-01-01', '2100-12-01', freq='MS')
#HADGEM_SEB = HADGEM_SEB.merge(HADGEM_SEB_2100) 



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


# ========== Calculate SW_net ===============    
#CMIP5
ACCESS_SW_net = ACCESS_SEB['SWD'] * ( 1- ACCESS_SEB['AL2'])
CSIRO_SW_net = CSIRO_SEB['SWD'] * ( 1- CSIRO_SEB['AL2']) 
#HADGEM_SW_net = HADGEM_SEB['SWD'] * ( 1- HADGEM_SEB['AL2']) 
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
#HADGEM_SEB = HADGEM_SEB.assign(SW_net = HADGEM_SW_net)
IPSL_SEB   = IPSL_SEB.assign(SW_net = IPSL_SW_net)
MIROC5_SEB = MIROC5_SEB.assign(SW_net = MIROC5_SW_net)
NORESM_SEB = NORESM_SEB.assign(SW_net = NORESM_SW_net)

CESM_SEB      = CESM_SEB.assign(SW_net = CESM_SW_net)
CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(SW_net = CNRM_ESM2_SW_net)
CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(SW_net = CNRM_ESM2_SW_net)
MRI_SEB       = MRI_SEB.assign(SW_net = MRI_SW_net)
UKMO_SEB      = UKMO_SEB.assign(SW_net = UKMO_SW_net)

# =========== Calculate Net energy flux ===============
ACCESS_net_flux = ACCESS_SEB['SW_net'] + ACCESS_SEB['LWD'] - ACCESS_SEB['LWU'] + ACCESS_SEB['SHF'] + ACCESS_SEB['LHF']
CSIRO_net_flux = CSIRO_SEB['SW_net'] + CSIRO_SEB['LWD'] - CSIRO_SEB['LWU'] + CSIRO_SEB['SHF'] + CSIRO_SEB['LHF']
#HADGEM_net_flux = HADGEM_SEB['SW_net'] + HADGEM_SEB['LWD'] - HADGEM_SEB['LWU'] + HADGEM_SEB['SHF'] + HADGEM_SEB['LHF']
IPSL_net_flux = IPSL_SEB['SW_net'] + IPSL_SEB['LWD'] - IPSL_SEB['LWU'] + IPSL_SEB['SHF'] + IPSL_SEB['LHF']
MIROC5_net_flux = MIROC5_SEB['SW_net'] + MIROC5_SEB['LWD'] - MIROC5_SEB['LWU'] + MIROC5_SEB['SHF'] + MIROC5_SEB['LHF']
NORESM_net_flux = NORESM_SEB['SW_net'] + NORESM_SEB['LWD'] - NORESM_SEB['LWU'] + NORESM_SEB['SHF'] + NORESM_SEB['LHF']

CESM_net_flux = CESM_SEB['SW_net'] + CESM_SEB['LWD'] - CESM_SEB['LWU'] + CESM_SEB['SHF'] + CESM_SEB['LHF']
CNRM_CM6_net_flux = CNRM_CM6_SEB['SW_net'] + CNRM_CM6_SEB['LWD'] - CNRM_CM6_SEB['LWU'] + CNRM_CM6_SEB['SHF'] + CNRM_CM6_SEB['LHF']
CNRM_ESM2_net_flux = CNRM_ESM2_SEB['SW_net'] + CNRM_ESM2_SEB['LWD'] - CNRM_ESM2_SEB['LWU'] + CNRM_ESM2_SEB['SHF'] + CNRM_ESM2_SEB['LHF']
MRI_net_flux = MRI_SEB['SW_net'] + MRI_SEB['LWD'] - MRI_SEB['LWU'] + MRI_SEB['SHF'] + MRI_SEB['LHF']
UKMO_net_flux = UKMO_SEB['SW_net'] + UKMO_SEB['LWD'] - UKMO_SEB['LWU'] + UKMO_SEB['SHF'] + UKMO_SEB['LHF']

# ===== Add Net energy to dataset =======
ACCESS_SEB = ACCESS_SEB.assign(NET_f = ACCESS_net_flux)
CSIRO_SEB  = CSIRO_SEB.assign(NET_f = CSIRO_net_flux)
#HADGEM_SEB = HADGEM_SEB.assign(NET_f = HADGEM_net_flux)
IPSL_SEB   = IPSL_SEB.assign(NET_f = IPSL_net_flux)
MIROC5_SEB = MIROC5_SEB.assign(NET_f = MIROC5_net_flux)
NORESM_SEB = NORESM_SEB.assign(NET_f = NORESM_net_flux)

CESM_SEB      = CESM_SEB.assign(NET_f = CESM_net_flux)
CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(NET_f = CNRM_ESM2_net_flux)
CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(NET_f = CNRM_ESM2_net_flux)
MRI_SEB       = MRI_SEB.assign(NET_f = MRI_net_flux)
UKMO_SEB      = UKMO_SEB.assign(NET_f = UKMO_net_flux)


# =========== Calculate Net Radiative energy flux ===============
ACCESS_net_rad_flux = ACCESS_SEB['SW_net'] + ACCESS_SEB['LWD'] - ACCESS_SEB['LWU']
CSIRO_net_rad_flux = CSIRO_SEB['SW_net'] + CSIRO_SEB['LWD'] - CSIRO_SEB['LWU'] 
#HADGEM_net_rad_flux = HADGEM_SEB['SW_net'] + HADGEM_SEB['LWD'] - HADGEM_SEB['LWU'] 
IPSL_net_rad_flux = IPSL_SEB['SW_net'] + IPSL_SEB['LWD'] - IPSL_SEB['LWU'] 
MIROC5_net_rad_flux = MIROC5_SEB['SW_net'] + MIROC5_SEB['LWD'] - MIROC5_SEB['LWU']
NORESM_net_rad_flux = NORESM_SEB['SW_net'] + NORESM_SEB['LWD'] - NORESM_SEB['LWU']


CESM_net_rad_flux = CESM_SEB['SW_net'] + CESM_SEB['LWD'] - CESM_SEB['LWU'] 
CNRM_CM6_net_rad_flux = CNRM_CM6_SEB['SW_net'] + CNRM_CM6_SEB['LWD'] - CNRM_CM6_SEB['LWU'] 
CNRM_ESM2_net_rad_flux = CNRM_ESM2_SEB['SW_net'] + CNRM_ESM2_SEB['LWD'] - CNRM_ESM2_SEB['LWU'] 
MRI_net_rad_flux = MRI_SEB['SW_net'] + MRI_SEB['LWD'] - MRI_SEB['LWU'] 
UKMO_net_rad_flux = UKMO_SEB['SW_net'] + UKMO_SEB['LWD'] - UKMO_SEB['LWU'] 

# ===== Add Net Radiative energy to dataset =======
ACCESS_SEB = ACCESS_SEB.assign(NET_rad_f = ACCESS_net_rad_flux)
CSIRO_SEB  = CSIRO_SEB.assign(NET_rad_f = CSIRO_net_rad_flux)
#HADGEM_SEB = HADGEM_SEB.assign(NET_rad_f = HADGEM_net_rad_flux)
IPSL_SEB   = IPSL_SEB.assign(NET_rad_f = IPSL_net_rad_flux)
MIROC5_SEB = MIROC5_SEB.assign(NET_rad_f = MIROC5_net_rad_flux)
NORESM_SEB = NORESM_SEB.assign(NET_rad_f = NORESM_net_rad_flux)

CESM_SEB      = CESM_SEB.assign(NET_rad_f = CESM_net_rad_flux)
CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(NET_rad_f = CNRM_ESM2_net_rad_flux)
CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(NET_rad_f = CNRM_ESM2_net_rad_flux)
MRI_SEB       = MRI_SEB.assign(NET_rad_f = MRI_net_rad_flux)
UKMO_SEB      = UKMO_SEB.assign(NET_rad_f = UKMO_net_rad_flux)


# =========== Calculate Net non-Radiative energy flux ===============
ACCESS_net_non_rad_flux = ACCESS_SEB['SHF'] + ACCESS_SEB['LHF']
CSIRO_net_non_rad_flux  = CSIRO_SEB['SHF'] + CSIRO_SEB['LHF']
#HADGEM_net_non_rad_flux = HADGEM_SEB['SHF'] + HADGEM_SEB['LHF']
IPSL_net_non_rad_flux   = IPSL_SEB['SHF'] + IPSL_SEB['LHF']
MIROC5_net_non_rad_flux = MIROC5_SEB['SHF'] + MIROC5_SEB['LHF']
NORESM_net_non_rad_flux = NORESM_SEB['SHF'] + NORESM_SEB['LHF']

CESM_net_non_rad_flux      = CESM_SEB['SHF'] + CESM_SEB['LHF']
CNRM_CM6_net_non_rad_flux  = CNRM_CM6_SEB['SHF'] + CNRM_CM6_SEB['LHF']
CNRM_ESM2_net_non_rad_flux = CNRM_ESM2_SEB['SHF'] + CNRM_ESM2_SEB['LHF']
MRI_net_non_rad_flux       = MRI_SEB['SHF'] + MRI_SEB['LHF']
UKMO_net_non_rad_flux      = UKMO_SEB['SHF'] + UKMO_SEB['LHF']

# ===== Add Net non-Radiative energy to dataset =======
ACCESS_SEB = ACCESS_SEB.assign(NET_non_rad_f = ACCESS_net_non_rad_flux)
CSIRO_SEB  = CSIRO_SEB.assign(NET_non_rad_f = CSIRO_net_non_rad_flux)
#HADGEM_SEB = HADGEM_SEB.assign(NET_non_rad_f = HADGEM_net_non_rad_flux)
IPSL_SEB   = IPSL_SEB.assign(NET_non_rad_f = IPSL_net_non_rad_flux)
MIROC5_SEB = MIROC5_SEB.assign(NET_non_rad_f = MIROC5_net_non_rad_flux)
NORESM_SEB = NORESM_SEB.assign(NET_non_rad_f = NORESM_net_non_rad_flux)

CESM_SEB      = CESM_SEB.assign(NET_non_rad_f = CESM_net_non_rad_flux)
CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(NET_non_rad_f = CNRM_ESM2_net_non_rad_flux)
CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(NET_non_rad_f = CNRM_ESM2_net_non_rad_flux)
MRI_SEB       = MRI_SEB.assign(NET_non_rad_f = MRI_net_non_rad_flux)
UKMO_SEB      = UKMO_SEB.assign(NET_non_rad_f = UKMO_net_non_rad_flux)


# ===== Calculate total precipitation ==== # 
ACCESS_PR = ACCESS_SEB['SF'] + ACCESS_SEB['RF']
CSIRO_PR  = CSIRO_SEB['SF'] + CSIRO_SEB['RF']
#HADGEM_PR = HADGEM_SEB['SF'] + HADGEM_SEB['RF']
IPSL_PR   = IPSL_SEB['SF'] + IPSL_SEB['RF']
MIROC5_PR = MIROC5_SEB['SF'] + MIROC5_SEB['RF']
NORESM_PR = NORESM_SEB['SF'] + NORESM_SEB['RF']

#CMIP6
CESM_PR      = CESM_SEB['SF'] + CESM_SEB['RF']
CNRM_CM6_PR  = CNRM_CM6_SEB['SF'] + CNRM_CM6_SEB['RF'] 
CNRM_ESM2_PR = CNRM_ESM2_SEB['SF'] + CNRM_ESM2_SEB['RF'] 
MRI_PR       = MRI_SEB['SF'] + MRI_SEB['RF'] 
UKMO_PR      = UKMO_SEB['SF'] + UKMO_SEB['RF'] 

# ===== Add precipitation to dataset =======
ACCESS_SEB = ACCESS_SEB.assign(PR = ACCESS_PR)
CSIRO_SEB  = CSIRO_SEB.assign(PR = CSIRO_PR)
#HADGEM_SEB = HADGEM_SEB.assign(PR = HADGEM_PR)
IPSL_SEB   = IPSL_SEB.assign(PR = IPSL_PR)
MIROC5_SEB = MIROC5_SEB.assign(PR = MIROC5_PR)
NORESM_SEB = NORESM_SEB.assign(PR = NORESM_PR)

CESM_SEB      = CESM_SEB.assign(PR = CESM_PR)
CNRM_CM6_SEB  = CNRM_CM6_SEB.assign(PR = CNRM_ESM2_PR)
CNRM_ESM2_SEB = CNRM_ESM2_SEB.assign(PR = CNRM_ESM2_PR)
MRI_SEB       = MRI_SEB.assign(PR = MRI_PR)
UKMO_SEB      = UKMO_SEB.assign(PR = UKMO_PR)




dates = pd.date_range('1950-01-01', '2100-12-01', freq='MS')

list_SEB_CMIP5 = [ACCESS_SEB, CSIRO_SEB, IPSL_SEB, MIROC5_SEB,NORESM_SEB]
list_SEB_CMIP6 = [CESM_SEB, CNRM_CM6_SEB, CNRM_ESM2_SEB, MRI_SEB, UKMO_SEB]


for ds in list_SEB_CMIP5:
    ds['TIME'] = dates

for ds in list_SEB_CMIP6:
    ds['TIME'] = dates
                             

        
    
# ==== create reference period ===
# CMIP5
ref_ACCESS = ACCESS_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
#ref_HADGEM = HADGEM_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_CSIRO  = CSIRO_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_IPSL   = IPSL_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_MIROC5 = MIROC5_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_NORESM = NORESM_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')


#CMIP6
ref_CESM      = CESM_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_CNRM_CM6  = CNRM_CM6_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_CNRM_ESM2 = CNRM_ESM2_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_MRI       = MRI_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')
ref_UKMO      = UKMO_SEB.sel(TIME=slice('1961','1990')).mean(dim='TIME')


mask_ablation_ACCESS = ref_ACCESS.where(ref_ACCESS.SMB < 0)
#mask_ablation_HADGEM = ref_HADGEM.where(ref_HADGEM.SMB < 0)
mask_ablation_CSIRO = ref_CSIRO.where(ref_CSIRO.SMB < 0)
mask_ablation_IPSL = ref_IPSL.where(ref_IPSL.SMB < 0)
mask_ablation_MIROC5 = ref_MIROC5.where(ref_MIROC5.SMB < 0)
mask_ablation_NORESM = ref_NORESM.where(ref_NORESM.SMB < 0)

mask_ablation_CESM = ref_CESM.where(ref_CESM.SMB < 0)
mask_ablation_CNRM_CM6 = ref_CNRM_CM6.where(ref_CNRM_CM6.SMB < 0)
mask_ablation_CNRM_ESM2 = ref_CNRM_ESM2.where(ref_CNRM_ESM2.SMB < 0)
mask_ablation_MRI = ref_MRI.where(ref_MRI.SMB < 0)
mask_ablation_UKMO = ref_UKMO.where(ref_UKMO.SMB < 0)
