"""
This code is used for plotting annual anomalies of SEB components
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd


#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/ACCESS_anomaly_annual.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/HADGEM_anomaly_annual.nc') 
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/CSIRO_anomaly_annual.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/IPSL_anomaly_annual.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/MIROC5_anomaly_annual.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/NORESM_anomaly_annual.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/CESM_anomaly_annual.nc')      
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/CNRM_CM6_anomaly_annual.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/CNRM_ESM2_anomaly_annual.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/MRI_anomaly_annual.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_annual/UKMO_anomaly_annual.nc')      


#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod) 

CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

TT_CMIP5     = []
LHF_CMIP5    = []
SHF_CMIP5    = []


for i in range(len(CMIP5_models)):
    TT_CM5  = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    LHF_CM5 = CMIP5_models[i].LHF.mean(dim=["X10_105","Y21_199"]) 
    SHF_CM5 = CMIP5_models[i].SHF.mean(dim=["X10_105","Y21_199"])

    TT_CMIP5.append(TT_CM5)
    LHF_CMIP5.append(LHF_CM5)
    SHF_CMIP5.append(SHF_CM5)

    
    
TT_CMIP5     = model_mean(TT_CMIP5)
LHF_CMIP5    = model_mean(LHF_CMIP5)
SHF_CMIP5    = model_mean(SHF_CMIP5)

    
SEB_var_CMIP5 = [LHF_CMIP5, SHF_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
LHF_CMIP6    = []
SHF_CMIP6    = []


for i in range(len(CMIP6_models)):
    TT_CM6  = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    LHF_CM6 = CMIP6_models[i].LHF.mean(dim=["X10_105","Y21_199"]) 
    SHF_CM6 = CMIP6_models[i].SHF.mean(dim=["X10_105","Y21_199"])

    TT_CMIP6.append(TT_CM6)
    LHF_CMIP6.append(LHF_CM6)
    SHF_CMIP6.append(SHF_CM6)

    
    
TT_CMIP6     = model_mean(TT_CMIP6)
LHF_CMIP6    = model_mean(LHF_CMIP6)
SHF_CMIP6    = model_mean(SHF_CMIP6)
    
SEB_var_CMIP6 = [LHF_CMIP6, SHF_CMIP6]

SEB_var_label = ['LHF','SHF']


#===== Fit a Regression line ========
### TEST NY METODE FOR REGRESSION KURVE###
TAS_CM5 = TT_CMIP5.to_dataframe()
LHF_CM5 = LHF_CMIP5.to_dataframe()
SHF_CM5 = SHF_CMIP5.to_dataframe()


TAS_CM6 = TT_CMIP6.to_dataframe()
LHF_CM6 = LHF_CMIP6.to_dataframe()
SHF_CM6 = SHF_CMIP6.to_dataframe()
    
### CMIP5 ###
x_CM5  = TAS_CM5['TT']
y1_CM5 = LHF_CM5['LHF']
y2_CM5 = SHF_CM5['SHF']

coeff_CM5 = np.polyfit(x_CM5, y1_CM5,2)
poly1_CM5 = np.poly1d(coeff_CM5)

coeff2_CM5 = np.polyfit(x_CM5, y2_CM5, 2)
poly2_CM5 = np.poly1d(coeff2_CM5)

t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y1_CM5 = poly1_CM5(curve_x_CM5)
curve_y2_CM5 = poly2_CM5(curve_x_CM5)


### CMIP6 ###
x_CM6  = TAS_CM6['TT']
y1_CM6 = LHF_CM6['LHF']
y2_CM6 = SHF_CM6['SHF']

coeff_CM6 = np.polyfit(x_CM6, y1_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)

coeff2_CM6 = np.polyfit(x_CM6, y2_CM6, 2)
poly2_CM6 = np.poly1d(coeff2_CM6)

t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y1_CM6 = poly1_CM6(curve_x_CM6)
curve_y2_CM6 = poly2_CM6(curve_x_CM6)

#=== PLOT ===   
fig, (ax1,ax2) = plt.subplots(1,2, sharex= True, sharey= True, figsize=(20,10))
for i in range(len(SEB_var_CMIP5)):
    ax1.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= SEB_var_label[i], s=10)

ax1.plot(curve_x_CM5, curve_y1_CM5)  ### TEST
ax1.plot(curve_x_CM5, curve_y2_CM5)  ### TEST
ax1.set_title('CMIP5 Model Mean - Annual SEB Heat flux component anomalies')
ax1.set_xlabel('Near-surface Temperature anomalies [$^\circ$C]')
ax1.set_ylabel('SEB components anomalies [Wm-2]')
ax1.legend(loc='upper left')

for i in range(len(SEB_var_CMIP6)):
    ax2.scatter(TT_CMIP6, SEB_var_CMIP6[i], label = SEB_var_label[i], s=10)

ax2.plot(curve_x_CM6, curve_y1_CM6)  ### TEST
ax2.plot(curve_x_CM6, curve_y2_CM6)  ### TEST
ax2.set_title('CMIP6 Model Mean - Annual SEB Heat flux component anomalies ')
ax2.set_xlabel('Near-surface Temperature anomalies [$^\circ$C]')
ax2.set_ylabel('SEB components anomalies [Wm-2]')
ax2.legend(loc='upper left')
sns.set_palette('colorblind')
sns.despine()
plt.show()
fig.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_heat_flux_anomalies_CMIP5_CMIP6_annual.png')

print('TAS 5.0')
print('CMIP5', 'LHF:', np.round(poly1_CM5(5),4), 'SHF:',np.round(poly2_CM5(5),4))
print('CMIP6', 'LHF:', np.round(poly1_CM6(5),4), 'SHF:',np.round(poly2_CM6(5),4))

#output from terminal 
"""
TAS 5.0
CMIP5 LHF: 1.2357 SHF: -1.4234
CMIP6 LHF: 1.5941 SHF: -0.617
"""

