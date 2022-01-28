import xarray as xr

import numpy as np
import pandas as pd 
from ablation_JJA_calculation import mean_mask 
from HadGEM_1_deg_ablation import HADGEM_anomaly

str_monthly = "/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/"  #NYEST


HADGEM_anomaly = HADGEM_anomaly.where(mean_mask.SMB < 0, drop=False)

HADGEM_anomaly.to_netcdf('/projects/NS9600K/idunnam/src/ablation_new/HADGEM_anomaly_ablation_JJA.nc')
