"""
This code is used for plotting seasonal (JJA) anomalies, with a reference period from 1961-1990, for 'net energy flux', 'net radiative energy flux' and 'net non-radiative energy flux', for the model means of CMIP5 and CMIP6 models. 
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc


#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/ACCESS_anomaly_JJA.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA.nc') 
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CSIRO_anomaly_JJA.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/IPSL_anomaly_JJA.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/MIROC5_anomaly_JJA.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/NORESM_anomaly_JJA.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CESM_anomaly_JJA.nc')
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_JJA.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_JJA.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/MRI_anomaly_JJA.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/UKMO_anomaly_JJA.nc')      


#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod)

CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

TT_CMIP5             = []
Net_f_CMIP5          = []
Net_rad_f_CMIP5      = []
Net_non_rad_f_CMIP5  = []

for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    Net_f_CM5   = CMIP5_models[i].NET_f.mean(dim=["X10_105","Y21_199"])
    Net_rad_f_CM5 = CMIP5_models[i].NET_rad_f.mean(dim=["X10_105","Y21_199"])
    Net_non_rad_f_CM5 = CMIP5_models[i].NET_non_rad_f.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    Net_f_CMIP5.append(Net_f_CM5)
    Net_rad_f_CMIP5.append(Net_rad_f_CM5)
    Net_non_rad_f_CMIP5.append(Net_non_rad_f_CM5)

TT_CMIP5             = model_mean(TT_CMIP5)
Net_f_CMIP5          = model_mean(Net_f_CMIP5)
Net_rad_f_CMIP5      = model_mean(Net_rad_f_CMIP5)
Net_non_rad_f_CMIP5  = model_mean(Net_non_rad_f_CMIP5)

SEB_var_CMIP5 = [Net_f_CMIP5, Net_rad_f_CMIP5, Net_non_rad_f_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6             = []
Net_f_CMIP6          = []
Net_rad_f_CMIP6      = []
Net_non_rad_f_CMIP6  = []

for i in range(len(CMIP6_models)):
    TT_CM6            = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    Net_f_CM6         = CMIP6_models[i].NET_f.mean(dim=["X10_105","Y21_199"])
    Net_rad_f_CM6     = CMIP6_models[i].NET_rad_f.mean(dim=["X10_105","Y21_199"])
    Net_non_rad_f_CM6 = CMIP6_models[i].NET_non_rad_f.mean(dim=["X10_105","Y21_199"])
    
    
    TT_CMIP6.append(TT_CM6)
    Net_f_CMIP6.append(Net_f_CM6)
    Net_rad_f_CMIP6.append(Net_rad_f_CM6)
    Net_non_rad_f_CMIP6.append(Net_non_rad_f_CM6)

TT_CMIP6             = model_mean(TT_CMIP6)
Net_f_CMIP6          = model_mean(Net_f_CMIP6)
Net_rad_f_CMIP6      = model_mean(Net_rad_f_CMIP6)
Net_non_rad_f_CMIP6  = model_mean(Net_non_rad_f_CMIP6)

SEB_var_CMIP6 = [Net_f_CMIP6, Net_rad_f_CMIP6, Net_non_rad_f_CMIP6]
SEB_var_label = ['Net energy flux', 'Net Radiative flux', 'Net non-Radiative flux']



# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
Net_f_reg_CM5 = Net_f_CMIP5.to_dataframe()
Net_rad_f_reg_CM5 = Net_rad_f_CMIP5.to_dataframe()
Net_non_rad_f_reg_CM5 = Net_non_rad_f_CMIP5.to_dataframe()

#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
Net_f_reg_CM6 = Net_f_CMIP6.to_dataframe()
Net_rad_f_reg_CM6 = Net_rad_f_CMIP6.to_dataframe()
Net_non_rad_f_reg_CM6 = Net_non_rad_f_CMIP6.to_dataframe()

### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y6_CM5 = Net_f_reg_CM5['NET_f']
y7_CM5 = Net_rad_f_reg_CM5['NET_rad_f']
y8_CM5 = Net_non_rad_f_reg_CM5['NET_non_rad_f']

coeff6_CM5 = np.polyfit(x_CM5, y6_CM5, 2)
poly6_CM5 = np.poly1d(coeff6_CM5)

coeff7_CM5 = np.polyfit(x_CM5, y7_CM5, 2)
poly7_CM5 = np.poly1d(coeff7_CM5)

coeff8_CM5 = np.polyfit(x_CM5, y8_CM5, 2)
poly8_CM5 = np.poly1d(coeff8_CM5)

t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y6_CM5 = poly6_CM5(curve_x_CM5)
curve_y7_CM5 = poly7_CM5(curve_x_CM5)
curve_y8_CM5 = poly8_CM5(curve_x_CM5)

### CMIP6 ###
x_CM6  = TT_reg_CM6['TT']
y6_CM6 = Net_f_reg_CM6['NET_f']
y7_CM6 = Net_rad_f_reg_CM6['NET_rad_f']
y8_CM6 = Net_non_rad_f_reg_CM6['NET_non_rad_f']

coeff6_CM6 = np.polyfit(x_CM6, y6_CM6, 2)
poly6_CM6 = np.poly1d(coeff6_CM6)

coeff7_CM6 = np.polyfit(x_CM6, y7_CM6, 2)
poly7_CM6 = np.poly1d(coeff7_CM6)

coeff8_CM6 = np.polyfit(x_CM6, y8_CM6, 2)
poly8_CM6 = np.poly1d(coeff8_CM6)

t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y6_CM6 = poly6_CM6(curve_x_CM6)
curve_y7_CM6 = poly7_CM6(curve_x_CM6)
curve_y8_CM6 = poly8_CM6(curve_x_CM6)

#"""
#== JOINT PLOT CMIP5 & CMIP6
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})

plt.figure(figsize= (10,10))
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 14)
plt.ylabel('SEB Net flux anomalies [Wm$^{-2}$]',fontsize = 14)
plt.title('Seasonal (JJA) Net flux anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=16) 

color_CM5 = ['darkolivegreen','firebrick', 'indigo']
label_CM5 = ['Net energy flux - CMIP5','Net Radiative energy flux - CMIP5','Net non-Radiative energy flux - CMIP5' ]
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=10, color = color_CM5[i])
    
plt.plot(curve_x_CM5, curve_y6_CM5, color = 'darkolivegreen')
plt.plot(curve_x_CM5, curve_y7_CM5, color = 'firebrick')
plt.plot(curve_x_CM5, curve_y8_CM5, color = 'indigo')


color_CM6 = ['yellowgreen',  'lightcoral','mediumpurple']
label_CM6 = ['Net energy flux - CMIP6','Net Radiative energy flux - CMIP6','Net non-Radiative energy flux - CMIP6' ]
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=10, marker='x',color = color_CM6[i])
    
plt.plot(curve_x_CM6, curve_y6_CM6, '--', color = 'yellowgreen')
plt.plot(curve_x_CM6, curve_y7_CM6, '--', color = 'lightcoral')
plt.plot(curve_x_CM6, curve_y8_CM6, '--', color = 'mediumpurple')



#Imports
import matplotlib.patches as mpatches

sns.despine()
plt.legend(ncol=2)
plt.show()
plt.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_components/Net_fluxes_JJA.png')
#"""
for TAS in range(1,6):
    print('TAS:', TAS)
    print('CMIP5:', 'Net energy flux:', np.round(poly6_CM5(TAS),3), 
          'Net rad flux:', np.round(poly7_CM5(TAS),3),
          'Net non-rad flux:', np.round(poly8_CM5(TAS),3))
    print('CMIP6:', 'Net energy flux:', np.round(poly6_CM6(TAS),3),
          'Net rad flux:', np.round(poly7_CM6(TAS),3),
          'Net non-rad flux:', np.round(poly8_CM6(TAS),3))


"""
Output from terminal

TAS: 1
CMIP5: Net energy flux: 2.019 Net rad flux: 1.745 Net non-rad flux: 0.274
CMIP6: Net energy flux: 1.659 Net rad flux: 1.315 Net non-rad flux: 0.344
TAS: 2
CMIP5: Net energy flux: 5.092 Net rad flux: 4.119 Net non-rad flux: 0.973
CMIP6: Net energy flux: 4.497 Net rad flux: 3.47 Net non-rad flux: 1.028
TAS: 3
CMIP5: Net energy flux: 9.212 Net rad flux: 7.047 Net non-rad flux: 2.165
CMIP6: Net energy flux: 8.589 Net rad flux: 6.381 Net non-rad flux: 2.208
TAS: 4
CMIP5: Net energy flux: 14.379 Net rad flux: 10.53 Net non-rad flux: 3.849
CMIP6: Net energy flux: 13.935 Net rad flux: 10.05 Net non-rad flux: 3.885
TAS: 5
CMIP5: Net energy flux: 20.592 Net rad flux: 14.566 Net non-rad flux: 6.026
CMIP6: Net energy flux: 20.535 Net rad flux: 14.476 Net non-rad flux: 6.059

"""

### TEST OUT BOX PLOT ###
#import seaborn as sns
#plt.boxplot(x = 'test', data = SEB_var_CMIP5)
#plt.savefig('boxplot_test.png')