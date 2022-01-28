"""
This code is used for plotting Cloud Cover for seasonal (JJA) anomalies for each model, 
with reference period 1961-1990, from monthly MAR output data of 6 CMIP5 models and 5 CMIP6 models. 
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd

#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/ACCESS_COD_JJA.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/HADGEM_COD_JJA.nc') 
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/CSIRO_COD_JJA.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/IPSL_COD_JJA.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/MIROC5_COD_JJA.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/NORESM_COD_JJA.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/CESM_COD_JJA.nc')      
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/CNRM_CM6_COD_JJA.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/CNRM_ESM2_COD_JJA.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/MRI_COD_JJA.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/Cloud/UKMO_COD_JJA.nc')      


#=== CMIP5 component model mean ===
TT_ACCESS = ACCESS.TT.mean(dim=["X10_105","Y21_199"])
TT_HADGEM = HADGEM.TT.mean(dim=["X10_105","Y21_199"])
TT_CSIRO  = CSIRO.TT.mean(dim=["X10_105","Y21_199"])
TT_IPSL   = IPSL.TT.mean(dim=["X10_105","Y21_199"])
TT_MIROC5 = MIROC5.TT.mean(dim=["X10_105","Y21_199"])
TT_NORESM = NORESM.TT.mean(dim=["X10_105","Y21_199"])

CC_ACCESS = ACCESS.CC.mean(dim=["X10_105","Y21_199"])
CC_HADGEM = HADGEM.CC.mean(dim=["X10_105","Y21_199"])
CC_CSIRO  = CSIRO.CC.mean(dim=["X10_105","Y21_199"])
CC_IPSL   = IPSL.CC.mean(dim=["X10_105","Y21_199"])
CC_MIROC5 = MIROC5.CC.mean(dim=["X10_105","Y21_199"])
CC_NORESM = NORESM.CC.mean(dim=["X10_105","Y21_199"])

#=== CMIP6 component model mean ===
TT_CESM = CESM.TT.mean(dim=["X10_105","Y21_199"])
TT_CNRM_CM6 = CNRM_CM6.TT.mean(dim=["X10_105","Y21_199"])
TT_CNRM_ESM2  = CNRM_ESM2.TT.mean(dim=["X10_105","Y21_199"])
TT_MRI   = MRI.TT.mean(dim=["X10_105","Y21_199"])
TT_UKMO = UKMO.TT.mean(dim=["X10_105","Y21_199"])

CC_CESM = CESM.CC.mean(dim=["X10_105","Y21_199"])
CC_CNRM_CM6 = CNRM_CM6.CC.mean(dim=["X10_105","Y21_199"])
CC_CNRM_ESM2  = CNRM_ESM2.CC.mean(dim=["X10_105","Y21_199"])
CC_MRI   = MRI.CC.mean(dim=["X10_105","Y21_199"])
CC_UKMO = UKMO.CC.mean(dim=["X10_105","Y21_199"])



#===== Fit a Regression line ========

### TEST NY METODE FOR REGRESSION KURVE###
#CMIP5
TAS_ACCESS = TT_ACCESS.to_dataframe()
TAS_HADGEM = TT_HADGEM.to_dataframe()
TAS_CSIRO = TT_CSIRO.to_dataframe()
TAS_IPSL = TT_IPSL.to_dataframe()
TAS_MIROC5 = TT_MIROC5.to_dataframe()
TAS_NORESM = TT_NORESM.to_dataframe()

CC_ACCESS = CC_ACCESS.to_dataframe()
CC_HADGEM = CC_HADGEM.to_dataframe()
CC_CSIRO = CC_CSIRO.to_dataframe()
CC_IPSL = CC_IPSL.to_dataframe()
CC_MIROC5 = CC_MIROC5.to_dataframe()
CC_NORESM = CC_NORESM.to_dataframe()

#CMIP6
TAS_CESM = TT_CESM.to_dataframe()
TAS_CNRM_CM6 = TT_CNRM_CM6.to_dataframe()
TAS_CNRM_ESM2 = TT_CNRM_ESM2.to_dataframe()
TAS_MRI = TT_MRI.to_dataframe()
TAS_UKMO = TT_UKMO.to_dataframe()

CC_CESM = CC_CESM.to_dataframe()
CC_CNRM_CM6 = CC_CNRM_CM6.to_dataframe()
CC_CNRM_ESM2 = CC_CNRM_ESM2.to_dataframe()
CC_MRI = CC_MRI.to_dataframe()
CC_UKMO = CC_UKMO.to_dataframe()


    
### CMIP5 ###
x_ACCESS = TAS_ACCESS['TT']
x_HADGEM = TAS_HADGEM['TT']
x_CSIRO = TAS_CSIRO['TT']
x_IPSL = TAS_IPSL['TT']
x_MIROC5 = TAS_MIROC5['TT']
x_NORESM = TAS_NORESM['TT']

y_ACCESS = CC_ACCESS['CC']
y_HADGEM = CC_HADGEM['CC']
y_CSIRO = CC_CSIRO['CC']
y_IPSL = CC_IPSL['CC']
y_MIROC5 = CC_MIROC5['CC']
y_NORESM = CC_NORESM['CC']

coeff_ACCESS = np.polyfit(x_ACCESS, y_ACCESS,2)
coeff_HADGEM = np.polyfit(x_HADGEM, y_HADGEM,2)
coeff_CSIRO = np.polyfit(x_CSIRO, y_CSIRO,2)
coeff_IPSL = np.polyfit(x_IPSL, y_IPSL,2)
coeff_MIROC5 = np.polyfit(x_MIROC5, y_MIROC5,2)
coeff_NORESM = np.polyfit(x_NORESM, y_NORESM,2)

poly1_ACCESS = np.poly1d(coeff_ACCESS)
poly1_HADGEM = np.poly1d(coeff_HADGEM)
poly1_CSIRO = np.poly1d(coeff_CSIRO)
poly1_IPSL = np.poly1d(coeff_IPSL)
poly1_MIROC5 = np.poly1d(coeff_MIROC5)
poly1_NORESM = np.poly1d(coeff_NORESM)



t = np.sort(TT_ACCESS)
curve_x_ACCESS = np.linspace(t[0], t[-1])
curve_x_HADGEM = np.linspace(t[0], t[-1])
curve_x_CSIRO = np.linspace(t[0], t[-1])
curve_x_IPSL = np.linspace(t[0], t[-1])
curve_x_MIROC5 = np.linspace(t[0], t[-1])
curve_x_NORESM = np.linspace(t[0], t[-1])

curve_y_ACCESS = poly1_ACCESS(curve_x_ACCESS)
curve_y_HADGEM = poly1_HADGEM(curve_x_HADGEM)
curve_y_CSIRO = poly1_CSIRO(curve_x_CSIRO)
curve_y_IPSL = poly1_IPSL(curve_x_IPSL)
curve_y_MIROC5 = poly1_MIROC5(curve_x_MIROC5)
curve_y_NORESM = poly1_NORESM(curve_x_NORESM)



### CMIP6 ###
x_CESM = TAS_CESM['TT']
x_CNRM_CM6 = TAS_CNRM_CM6['TT']
x_CNRM_ESM2 = TAS_CNRM_ESM2['TT']
x_MRI = TAS_MRI['TT']
x_UKMO = TAS_UKMO['TT']


y_CESM = CC_CESM['CC']
y_CNRM_CM6 = CC_CNRM_CM6['CC']
y_CNRM_ESM2 = CC_CNRM_ESM2['CC']
y_MRI = CC_MRI['CC']
y_UKMO = CC_UKMO['CC']


coeff_CESM = np.polyfit(x_CESM, y_CESM,2)
coeff_CNRM_CM6 = np.polyfit(x_CNRM_CM6, y_CNRM_CM6,2)
coeff_CNRM_ESM2 = np.polyfit(x_CNRM_ESM2, y_CNRM_ESM2,2)
coeff_MRI = np.polyfit(x_MRI, y_MRI,2)
coeff_UKMO = np.polyfit(x_UKMO, y_UKMO,2)

poly1_CESM = np.poly1d(coeff_CESM)
poly1_CNRM_CM6 = np.poly1d(coeff_CNRM_CM6)
poly1_CNRM_ESM2 = np.poly1d(coeff_CNRM_ESM2)
poly1_MRI = np.poly1d(coeff_MRI)
poly1_UKMO = np.poly1d(coeff_UKMO)


t = np.sort(TT_CESM)
curve_x_CESM = np.linspace(t[0], t[-1])
curve_x_CNRM_CM6 = np.linspace(t[0], t[-1])
curve_x_CNRM_ESM2 = np.linspace(t[0], t[-1])
curve_x_MRI = np.linspace(t[0], t[-1])
curve_x_UKMO = np.linspace(t[0], t[-1])


curve_y_CESM = poly1_CESM(curve_x_CESM)
curve_y_CNRM_CM6 = poly1_CNRM_CM6(curve_x_CNRM_CM6)
curve_y_CNRM_ESM2 = poly1_CNRM_ESM2(curve_x_CNRM_ESM2)
curve_y_MRI = poly1_MRI(curve_x_MRI)
curve_y_UKMO = poly1_UKMO(curve_x_UKMO)

#=== PLOT ===   
plt.figure(figsize=(10,10))
#for i in range(len(SEB_var_CMIP5)):
    #plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= 'CC - CMIP5', s=10, color= 'darkblue')

    
plt.scatter(TT_ACCESS, CC_ACCESS, label = 'CC - ACCESS', s=10)
plt.scatter(TT_HADGEM, CC_HADGEM, label = 'CC - HADGEM', s=10)
plt.scatter(TT_CSIRO, CC_CSIRO, label = 'CC - CSIRO', s=10)
plt.scatter(TT_IPSL, CC_IPSL, label = 'CC - IPSL', s=10)
plt.scatter(TT_MIROC5, CC_MIROC5, label = 'CC - MIROC5', s=10)
plt.scatter(TT_NORESM, CC_NORESM, label = 'CC - NORESM', s=10)
    
plt.plot(curve_x_ACCESS, curve_y_ACCESS, color = 'darkblue')  ### TEST
plt.plot(curve_x_HADGEM, curve_y_HADGEM, color = 'orange')  ### TEST
plt.plot(curve_x_CSIRO, curve_y_CSIRO, color = 'green')  ### TEST
plt.plot(curve_x_IPSL, curve_y_IPSL, color = 'red')  ### TEST
plt.plot(curve_x_MIROC5, curve_y_MIROC5, color = 'purple')  ### TEST
plt.plot(curve_x_NORESM, curve_y_NORESM, color = 'brown')  ### TEST

plt.title('Seasonal (JJA) Cloud Cover anomalies - CMIP5', fontsize = 16)
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]')
plt.ylabel('CC anomalies')
plt.legend(loc='upper left')

#for i in range(len(SEB_var_CMIP6)):
#    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i], label = 'CC - CMIP6', s=10, marker = 'x', color='royalblue')


#plt.plot(curve_x_CM6, curve_y_CM6, '--', color='royalblue')  ### TEST
plt.legend(loc='upper left')
sns.set_palette('colorblind')
sns.despine()
plt.show()
plt.savefig('/projects/NS9600K/idunnam/src/Figures/CC_anomalies_CMIP5_all.png')



###### PLOT CMIP6 ######
plt.figure(figsize=(10,10))
#for i in range(len(SEB_var_CMIP5)):
    #plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= 'CC - CMIP5', s=10, color= 'darkblue')

    
plt.scatter(TT_CESM, CC_CESM, label = 'CC - CESM', s=10)
plt.scatter(TT_CNRM_CM6, CC_CNRM_CM6, label = 'CC - CNRM_CM6', s=10)
plt.scatter(TT_CNRM_ESM2, CC_CNRM_ESM2, label = 'CC - CNRM_ESM2', s=10)
plt.scatter(TT_MRI, CC_MRI, label = 'CC - MRI', s=10)
plt.scatter(TT_UKMO, CC_UKMO, label = 'CC - UKMO', s=10)
    
plt.plot(curve_x_CESM, curve_y_CESM, color = 'darkblue')  ### TEST
plt.plot(curve_x_CNRM_CM6, curve_y_CNRM_CM6, color = 'orange')  ### TES
plt.plot(curve_x_CNRM_ESM2, curve_y_CNRM_ESM2, color = 'green')  ### TEST
plt.plot(curve_x_MRI, curve_y_MRI, color = 'red')  ### TEST
plt.plot(curve_x_UKMO, curve_y_UKMO, color = 'purple')  ### TEST

plt.title('Seasonal (JJA) Cloud Cover anomalies - CMIP6', fontsize = 16)
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]')
plt.ylabel('CC anomalies')
plt.legend(loc='upper left')

#for i in range(len(SEB_var_CMIP6)):
#    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i], label = 'CC - CMIP6', s=10, marker = 'x', color='royalblue')


#plt.plot(curve_x_CM6, curve_y_CM6, '--', color='royalblue')  ### TEST
plt.legend(loc='upper left')
sns.set_palette('colorblind')
sns.despine()
plt.show()
plt.savefig('/projects/NS9600K/idunnam/src/Figures/Cloud_components/CC_anomalies_CMIP6_all.png')



#TAS = 1
#print('TAS:', TAS)
#print('CMIP5', 'CC:', np.round(poly1_CM5(TAS)*100,4),'%')
#print('CMIP6', 'CC:', np.round(poly1_CM6(TAS)*100,4),'%')


###
"""
Output: 

TAS: 1
CMIP5 CC: 0.1487 %
CMIP6 CC: -0.722 %

TAS: 2
CMIP5 CC: 0.5293 %
CMIP6 CC: -1.0023 %

TAS: 3
CMIP5 CC: 0.9909 %
CMIP6 CC: -1.3422 %

TAS: 4
CMIP5 CC: 1.5336 %
CMIP6 CC: -1.7416 %

TAS: 5
CMIP5 CC: 2.1574 %
CMIP6 CC: -2.2006 %
"""