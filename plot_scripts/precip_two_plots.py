import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc

season= input('Enter season [MAM,JJA,SON]:')

ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_'+season+'.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_SMB.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CSIRO_anomaly_'+season+'.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/IPSL_anomaly_'+season+'.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MIROC5_anomaly_'+season+'.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/NORESM_anomaly_'+season+'.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CESM_anomaly_'+season+'.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_'+season+'.nc')
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_'+season+'.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_'+season+'.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_'+season+'.nc')      

#dataset for choosing coordinates
ds = xr.open_dataset('/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/MARv3.9-ACCESS13-2074.nc', decode_times=False)


from function_two_plots import two_plots

#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod)

CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

TT_CMIP5     = []
PR_CMIP5    = []
SF_CMIP5    = [] 
RF_CMIP5    = []
RZ_CMIP5    = []


for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT 
    PR_CM5     = CMIP5_models[i].PR  
    SF_CM5     = CMIP5_models[i].SF  
    RF_CM5     = CMIP5_models[i].RF 
    RZ_CM5     = CMIP5_models[i].RZ 
    
    TT_CMIP5.append(TT_CM5)
    RF_CMIP5.append(RF_CM5)
    PR_CMIP5.append(PR_CM5)
    SF_CMIP5.append(SF_CM5)
    RZ_CMIP5.append(RZ_CM5)
    
TT_CMIP5     = model_mean(TT_CMIP5)
RF_CMIP5    = model_mean(RF_CMIP5)
PR_CMIP5    = model_mean(PR_CMIP5)
SF_CMIP5    = model_mean(SF_CMIP5)
RZ_CMIP5    = model_mean(RZ_CMIP5)

SEB_var_CMIP5 = [PR_CMIP5, SF_CMIP5, RF_CMIP5, SW_net_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
PR_CMIP6    = []
SF_CMIP6    = [] 
RF_CMIP6    = []
RZ_CMIP6    = []
SW_net_CMIP6 = []
LW_net_CMIP6 = []
Net_rad_f_CMIP6  = []

for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT 
    PR_CM6     = CMIP6_models[i].PR  
    SF_CM6     = CMIP6_models[i].SF  
    RF_CM6     = CMIP6_models[i].RF 
    RZ_CM6     = CMIP6_models[i].RZ 
    
    TT_CMIP6.append(TT_CM6)
    RF_CMIP6.append(RF_CM6)
    PR_CMIP6.append(PR_CM6)
    SF_CMIP6.append(SF_CM6)
    RZ_CMIP6.append(RZ_CM6)
    
TT_CMIP6     = model_mean(TT_CMIP6)
RF_CMIP6    = model_mean(RF_CMIP6)
PR_CMIP6    = model_mean(PR_CMIP6)
SF_CMIP6    = model_mean(SF_CMIP6)
RZ_CMIP6    = model_mean(RZ_CMIP6)

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})




#=== Total precipitation ===#
diff_plot(PR_CMIP6, PR_CMIP5, ds['LON'], ds['LAT'],
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Total precipitation anomalies [mmWE]',
          title_plot='(CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_PR')

#=== Snowfall ===#
diff_plot(SF_CMIP6, SF_CMIP5, ds['LON'], ds['LAT'],
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Snowfall anomalies [mmWE]',
          title_plot='(CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_SF')

#=== Rainfall ===#
diff_plot(RF_CMIP6, RF_CMIP5, ds['LON'], ds['LAT'],
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Rainfall anomalies [mmWE]',
          title_plot='(CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_RF')

#=== Rainfall ===#
diff_plot(RZ_CMIP6, RZ_CMIP5, ds['LON'], ds['LAT'],
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Rrefreezing anomalies [mmWE]',
          title_plot='(CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_RZ')