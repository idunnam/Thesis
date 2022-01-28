"""
This code is used for plotting induvidual timelines of seasonal CC for each CMIP5 and CMIP6 model
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd


#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_ACCESS.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_HADGEM.nc') 
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_CSIRO.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_IPSL.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_MIROC5.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_NORESM.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_CESM.nc')      
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_CNRM_CM6.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_CNRM_ESM2.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_MRI.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/seas_UKMO.nc') 

fig, axs = plt.subplots(1,2, sharey = True, figsize=(30, 10))
axs[0].plot(ACCESS.CC.year, ACCESS.CC.mean(dim=["X10_105","Y21_199"]), label='ACCESS')
axs[0].plot(HADGEM.CC.year, HADGEM.CC.mean(dim=["X10_105","Y21_199"]),label='HADGEM')
axs[0].plot(IPSL.CC.year, IPSL.CC.mean(dim=["X10_105","Y21_199"]),label='IPSL')
axs[0].plot(MIROC5.CC.year, MIROC5.CC.mean(dim=["X10_105","Y21_199"]),label='MIROC5')
axs[0].plot(NORESM.CC.year, NORESM.CC.mean(dim=["X10_105","Y21_199"]),label='NORESM')
axs[0].plot(CSIRO.CC.year, CSIRO.CC.mean(dim=["X10_105","Y21_199"]),label='CSIRO')
axs[0].legend(loc='upper left')
axs[0].set_xlabel('year')
axs[0].set_ylabel('CC')
axs[0].set_title('Cloud Cover - CMIP5 Models')

axs[1].plot(CESM.CC.year, ACCESS.CC.mean(dim=["X10_105","Y21_199"]), label='CESM')
axs[1].plot(CNRM_CM6.CC.year, CNRM_CM6.CC.mean(dim=["X10_105","Y21_199"]),label='CNRM_CM6')
axs[1].plot(CNRM_ESM2.CC.year, CNRM_ESM2.CC.mean(dim=["X10_105","Y21_199"]),label='CNRM_ESM2')
axs[1].plot(MIROC5.CC.year, MIROC5.CC.mean(dim=["X10_105","Y21_199"]),label='MRI')
axs[1].plot(UKMO.CC.year, UKMO.CC.mean(dim=["X10_105","Y21_199"]),label='UKMO')
axs[1].legend(loc='upper left')
axs[1].set_xlabel('year')
axs[1].set_ylabel('CC')
axs[1].set_title('Cloud Cover - CMIP5 Models')

sns.set_palette('colorblind')
plt.savefig('CC_test_2.png')
plt.show()

