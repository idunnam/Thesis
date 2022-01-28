"""
This code is used for plotting maps for the model mean CC over the Greenland ice sheet of CMIP5 and CMIP6.
"""
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import cartopy.crs as ccrs
import cartopy.feature


#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/ACCESS_JJA_2071_2100_anomaly.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/HADGEM_JJA_2071_2100_anomaly.nc') 
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CSIRO_JJA_2071_2100_anomaly.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/IPSL_JJA_2071_2100_anomaly.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/MIROC5_JJA_2071_2100_anomaly.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/NORESM_JJA_2071_2100_anomaly.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CESM_JJA_2071_2100_anomaly.nc')
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CNRM_CM6_JJA_2071_2100_anomaly.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/CNRM_ESM2_JJA_2071_2100_anomaly.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/MRI_JJA_2071_2100_anomaly.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_30yrs/UKMO_JJA_2071_2100_anomaly.nc')      

#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod)

CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

TT_CMIP5     = []
CC_CMIP5 = []

for i in range(len(CMIP5_models)):
    #TT_CM5  = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    #CC_CM5  = CMIP5_models[i].CC.mean(dim=["X10_105","Y21_199"])
    TT_CM5   = CMIP5_models[i].TT
    CC_CM5   = CMIP5_models[i].CC
    
    
    TT_CMIP5.append(TT_CM5)
    CC_CMIP5.append(CC_CM5)

TT_CMIP5     = model_mean(TT_CMIP5)
CC_CM5_modMean = model_mean(CC_CMIP5)

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
CC_CMIP6     = []


for i in range(len(CMIP6_models)):
    #TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    #CC_CM6      = CMIP6_models[i].CC.mean(dim=["X10_105","Y21_199"])
    
    #use when calculating model mean 
    TT_CM6      = CMIP6_models[i].TT
    CC_CM6      = CMIP6_models[i].CC
    TT_CMIP6.append(TT_CM6)
    CC_CMIP6.append(CC_CM6)
    
    

TT_CMIP6 = model_mean(TT_CMIP6)
CC_CM6_modMean = model_mean(CC_CMIP6)


ds = xr.open_dataset('/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all/MARv3.9-monthly-MIROC5-1997.nc', decode_times=False)


## ==== PLOT ==== ## 

proj = ccrs.LambertConformal(central_longitude=-35,
                             central_latitude=65,
                             standard_parallels=[35])
#fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(
#    8, 10), subplot_kw={'projection': proj})
fig, axes = plt.subplots( ncols=2, figsize=(
    8, 10), subplot_kw={'projection': proj})

ax = axes.ravel().tolist()

for i in [0,1]:
    ax[i].add_feature(cartopy.feature.OCEAN.with_scale(
                 '50m'), zorder=1, facecolor='white')           
    ax[i].add_feature(cartopy.feature.COASTLINE.with_scale(
                 '50m'), zorder=1, edgecolor='black')
    ax[i].set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())
    



   
    
cont = ax[0].pcolormesh(ds['LON'], ds['LAT'], CC_CM5_modMean.values*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin=-10, vmax=6)
cont2 = ax[1].pcolormesh(ds['LON'], ds['LAT'], CC_CM6_modMean.values*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin=-10, vmax=6)

ax[0].set_title('CMIP5 Model Mean', fontsize=16)
#ax[0].patch.set_visible(False)
ax[1].set_title('CMIP6 Model Mean', fontsize=16)
#ax[1].patch.set_visible(False)

#remove outer box of the plot 
fig.patch.set_visible(False)
ax[0].axis('off')
ax[1].axis('off')

fig.canvas.draw()
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)

plt.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.24)
cbar = fig.colorbar(cont2, ax=ax, shrink=0.7, orientation ='vertical')
cbar.set_label(
    'Cloud Cover anomalies [%]', fontsize=14)
fig.savefig('CC_map_plot_CMIP5_CMIP6_joint.png')   


"""
This figure shows the 2171-2100 seasonal (JJA) mean of cloud cover anomalies over the Greenland ice sheet for a model mean of CMIP5 and CMIP6 models. 
"""