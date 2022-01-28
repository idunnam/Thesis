
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc
from latex_size import set_size
"""
#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
#CMIP5
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

TT_CMIP5     = []
SMB_CMIP5    = []
ME_CMIP5    = [] 
RU_CMIP5    = []
RF_CMIP5    = []


for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    SMB_CM5     = CMIP5_models[i].SMB.mean(dim=["X10_105","Y21_199"]) 
    ME_CM5      = CMIP5_models[i].ME.mean(dim=["X10_105","Y21_199"]) 
    RU_CM5     = CMIP5_models[i].RU.mean(dim=["X10_105","Y21_199"])
    RF_CM5     = CMIP5_models[i].RF.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    SMB_CMIP5.append(SMB_CM5)
    ME_CMIP5.append(ME_CM5)
    RU_CMIP5.append(RU_CM5)
    RF_CMIP5.append(RF_CM5)

TT_CMIP5     = model_mean(TT_CMIP5)
SMB_CMIP5    = model_mean(SMB_CMIP5)
ME_CMIP5    = model_mean(ME_CMIP5)
RU_CMIP5    = model_mean(RU_CMIP5)
RF_CMIP5    = model_mean(RF_CMIP5)

SEB_var_CMIP5 = [SMB_CMIP5, ME_CMIP5, RU_CMIP5, RF_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
SMB_CMIP6    = []
ME_CMIP6    = [] 
RU_CMIP6    = []
RF_CMIP6    = []


for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    SMB_CM6     = CMIP6_models[i].SMB.mean(dim=["X10_105","Y21_199"]) 
    ME_CM6     = CMIP6_models[i].ME.mean(dim=["X10_105","Y21_199"]) 
    RU_CM6     = CMIP6_models[i].RU.mean(dim=["X10_105","Y21_199"])
    RF_CM6     = CMIP6_models[i].RF.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP6.append(TT_CM6)
    SMB_CMIP6.append(SMB_CM6)
    RU_CMIP6.append(RU_CM6)
    ME_CMIP6.append(ME_CM6)
    RF_CMIP6.append(RF_CM6)
    
TT_CMIP6     = model_mean(TT_CMIP6)
SMB_CMIP6    = model_mean(SMB_CMIP6)
ME_CMIP6    = model_mean(ME_CMIP6)
RU_CMIP6    = model_mean(RU_CMIP6)
RF_CMIP6    = model_mean(RF_CMIP6)

SEB_var_CMIP6 = [SMB_CMIP6, ME_CMIP6, RU_CMIP6, RF_CMIP6]
SEB_var_label = ['SMB','ME','RU','RF']

# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
SMB_reg_CM5 = SMB_CMIP5.to_dataframe()
ME_reg_CM5 = ME_CMIP5.to_dataframe()
RU_reg_CM5 = RU_CMIP5.to_dataframe()
RF_reg_CM5 = RF_CMIP5.to_dataframe()

#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
SMB_reg_CM6 = SMB_CMIP6.to_dataframe()
ME_reg_CM6 = ME_CMIP6.to_dataframe()
RU_reg_CM6 = RU_CMIP6.to_dataframe()
RF_reg_CM6 = RF_CMIP6.to_dataframe()

### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y1_CM5 = SMB_reg_CM5['SMB']
y2_CM5 = ME_reg_CM5['ME']
y3_CM5 = RU_reg_CM5['RU']
y4_CM5 = RF_reg_CM5['RF']


coeff_CM5 = np.polyfit(x_CM5, y1_CM5,2)
poly1_CM5 = np.poly1d(coeff_CM5)

coeff2_CM5 = np.polyfit(x_CM5, y2_CM5, 2)
poly2_CM5 = np.poly1d(coeff2_CM5)

coeff3_CM5 = np.polyfit(x_CM5, y3_CM5, 2)
poly3_CM5 = np.poly1d(coeff3_CM5)

coeff4_CM5 = np.polyfit(x_CM5, y4_CM5, 2)
poly4_CM5 = np.poly1d(coeff4_CM5)


t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y1_CM5 = poly1_CM5(curve_x_CM5)
curve_y2_CM5 = poly2_CM5(curve_x_CM5)
curve_y3_CM5 = poly3_CM5(curve_x_CM5)
curve_y4_CM5 = poly4_CM5(curve_x_CM5)


### CMIP6 ###
x_CM6  = TT_reg_CM6['TT']
y1_CM6 = SMB_reg_CM6['SMB']
y2_CM6 = ME_reg_CM6['ME']
y3_CM6 = RU_reg_CM6['RU']
y4_CM6 = RF_reg_CM6['RF']

coeff_CM6 = np.polyfit(x_CM6, y1_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)

coeff2_CM6 = np.polyfit(x_CM6, y2_CM6, 2)
poly2_CM6 = np.poly1d(coeff2_CM6)

coeff3_CM6 = np.polyfit(x_CM6, y3_CM6, 2)
poly3_CM6 = np.poly1d(coeff3_CM6)

coeff4_CM6 = np.polyfit(x_CM6, y4_CM6, 2)
poly4_CM6 = np.poly1d(coeff4_CM6)


t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y1_CM6 = poly1_CM6(curve_x_CM6)
curve_y2_CM6 = poly2_CM6(curve_x_CM6)
curve_y3_CM6 = poly3_CM6(curve_x_CM6)
curve_y4_CM6 = poly4_CM6(curve_x_CM6)


#==========================================================================================
#==========================================================================================
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})


#== JOINT PLOT CM5 & CM6 ==
plt.figure(figsize= (10,10))
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 14)
plt.ylabel('SMB', fontsize = 14)
plt.title('Seasonal (JJA) SMB component anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=16) 
#plt.title('CMIP5 & CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies') 

color_CM5 = ['darkolivegreen', 'firebrick','indigo','darkorange']
label_CM5 = ['SMB - CMIP5','ME - CMIP5', 'RU - CMIP5', 'RF - CMIP5']
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=10, color = color_CM5[i])
    #sns.set_palette('colorblind')
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen')  ### TEST
plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick')  ### TEST
plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo')  ### TEST
plt.plot(curve_x_CM5, curve_y4_CM5, color ='darkorange')  ### TEST

color_CM6 = ['yellowgreen','lightcoral','mediumpurple',  'sandybrown']
label_CM6 = ['SMB - CMIP6','ME - CMIP6', 'RU - CMIP6', 'RF - CMIP6']
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=10, marker='x',color = color_CM6[i])
    
plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen')  ### TEST
plt.plot(curve_x_CM6, curve_y2_CM6, '--',color ='lightcoral')  ### TEST
plt.plot(curve_x_CM6, curve_y3_CM6, '--', color ='mediumpurple')  ### TEST
plt.plot(curve_x_CM6, curve_y4_CM6, '--', color ='sandybrown')  ### TEST


#Imports
import matplotlib.patches as mpatches


###sns.set_palette('colorblind')
sns.despine()
plt.legend(ncol=2)
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/src/Figures/SMB_anomalies_jointCM5CM6_JJA.png')
"""

#######============== ANNUAL ============ #############

import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc


#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
#CMIP5
"""
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/ACCESS_anomaly_annual.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_SMB_annual.nc') 
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CSIRO_anomaly_annual.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/IPSL_anomaly_annual.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/MIROC5_anomaly_annual.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/NORESM_anomaly_annual.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CESM_anomaly_annual.nc')
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CNRM_CM6_anomaly_annual.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CNRM_ESM2_anomaly_annual.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/MRI_anomaly_annual.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/UKMO_anomaly_annual.nc')      

"""
season= input('Enter season [MAM,JJA,SON,DJF]:')

ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_'+season+'.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_SMB.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CSIRO_anomaly_'+season+'.nc') 
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/IPSL_anomaly_'+season+'.nc')  
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MIROC5_anomaly_'+season+'.nc') 
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/NORESM_anomaly_'+season+'.nc')  

#CMIP6
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CESM_anomaly_'+season+'.nc')
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_'+season+'.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_'+season+'.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_'+season+'.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_'+season+'.nc')      



#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod)

CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

TT_CMIP5    = []
SMB_CMIP5   = []
ME_CMIP5    = [] 
RU_CMIP5    = []
RF_CMIP5    = []
RZ_CMIP5    = []


for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    SMB_CM5     = CMIP5_models[i].SMB.mean(dim=["X10_105","Y21_199"])
    ME_CM5      = CMIP5_models[i].ME.mean(dim=["X10_105","Y21_199"]) 
    RU_CM5     = CMIP5_models[i].RU.mean(dim=["X10_105","Y21_199"])
    RF_CM5     = CMIP5_models[i].RF.mean(dim=["X10_105","Y21_199"])
    RZ_CM5     = CMIP5_models[i].RZ.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    SMB_CMIP5.append(SMB_CM5)
    ME_CMIP5.append(ME_CM5)
    RU_CMIP5.append(RU_CM5)
    RF_CMIP5.append(RF_CM5)
    RZ_CMIP5.append(RZ_CM5)

TT_CMIP5     = model_mean(TT_CMIP5)
SMB_CMIP5    = model_mean(SMB_CMIP5)
ME_CMIP5    = model_mean(ME_CMIP5)
RU_CMIP5    = model_mean(RU_CMIP5)
RF_CMIP5    = model_mean(RF_CMIP5)
RZ_CMIP5    = model_mean(RZ_CMIP5)


SEB_var_CMIP5 = [SMB_CMIP5, ME_CMIP5, RU_CMIP5]#, RZ_CMIP5, RF_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
SMB_CMIP6    = []
ME_CMIP6    = [] 
RU_CMIP6    = []
RF_CMIP6    = []
RZ_CMIP6    = []


for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    SMB_CM6     = CMIP6_models[i].SMB.mean(dim=["X10_105","Y21_199"]) 
    ME_CM6     = CMIP6_models[i].ME.mean(dim=["X10_105","Y21_199"]) 
    RU_CM6     = CMIP6_models[i].RU.mean(dim=["X10_105","Y21_199"])
    RF_CM6     = CMIP6_models[i].RF.mean(dim=["X10_105","Y21_199"])
    RZ_CM6     = CMIP6_models[i].RZ.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP6.append(TT_CM6)
    SMB_CMIP6.append(SMB_CM6)
    RU_CMIP6.append(RU_CM6)
    ME_CMIP6.append(ME_CM6)
    RF_CMIP6.append(RF_CM6)
    RZ_CMIP6.append(RZ_CM6)
    
TT_CMIP6     = model_mean(TT_CMIP6)
SMB_CMIP6    = model_mean(SMB_CMIP6)
ME_CMIP6    = model_mean(ME_CMIP6)
RU_CMIP6    = model_mean(RU_CMIP6)
RF_CMIP6    = model_mean(RF_CMIP6)
RZ_CMIP6    = model_mean(RZ_CMIP6)

SEB_var_CMIP6 = [SMB_CMIP6, ME_CMIP6, RU_CMIP6]#, RZ_CMIP6, RF_CMIP6]
SEB_var_label = ['SMB','ME','RU']#, 'RZ', 'RF']

# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
SMB_reg_CM5 = SMB_CMIP5.to_dataframe()
ME_reg_CM5 = ME_CMIP5.to_dataframe()
RU_reg_CM5 = RU_CMIP5.to_dataframe()
RF_reg_CM5 = RF_CMIP5.to_dataframe()
RZ_reg_CM5 = RZ_CMIP5.to_dataframe()


#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
SMB_reg_CM6 = SMB_CMIP6.to_dataframe()
ME_reg_CM6 = ME_CMIP6.to_dataframe()
RU_reg_CM6 = RU_CMIP6.to_dataframe()
RF_reg_CM6 = RF_CMIP6.to_dataframe()
RZ_reg_CM6 = RZ_CMIP6.to_dataframe()


### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y1_CM5 = SMB_reg_CM5['SMB']
y2_CM5 = ME_reg_CM5['ME']
y3_CM5 = RU_reg_CM5['RU']
y4_CM5 = RF_reg_CM5['RF']
y5_CM5 = RZ_reg_CM5['RZ']


coeff_CM5 = np.polyfit(x_CM5, y1_CM5, 2)
poly1_CM5 = np.poly1d(coeff_CM5)

coeff2_CM5 = np.polyfit(x_CM5, y2_CM5, 2)
poly2_CM5 = np.poly1d(coeff2_CM5)

coeff3_CM5 = np.polyfit(x_CM5, y3_CM5, 2)
poly3_CM5 = np.poly1d(coeff3_CM5)

coeff4_CM5 = np.polyfit(x_CM5, y4_CM5, 2)
poly4_CM5 = np.poly1d(coeff4_CM5)

coeff5_CM5 = np.polyfit(x_CM5, y5_CM5, 2)
poly5_CM5 = np.poly1d(coeff5_CM5)



t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y1_CM5 = poly1_CM5(curve_x_CM5)
curve_y2_CM5 = poly2_CM5(curve_x_CM5)
curve_y3_CM5 = poly3_CM5(curve_x_CM5)
curve_y4_CM5 = poly4_CM5(curve_x_CM5)
curve_y5_CM5 = poly5_CM5(curve_x_CM5)


### CMIP6 ###
x_CM6  = TT_reg_CM6['TT']
y1_CM6 = SMB_reg_CM6['SMB']
y2_CM6 = ME_reg_CM6['ME']
y3_CM6 = RU_reg_CM6['RU']
y4_CM6 = RF_reg_CM6['RF']
y5_CM6 = RZ_reg_CM6['RZ']

coeff_CM6 = np.polyfit(x_CM6, y1_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)

coeff2_CM6 = np.polyfit(x_CM6, y2_CM6, 2)
poly2_CM6 = np.poly1d(coeff2_CM6)

coeff3_CM6 = np.polyfit(x_CM6, y3_CM6, 2)
poly3_CM6 = np.poly1d(coeff3_CM6)

coeff4_CM6 = np.polyfit(x_CM6, y4_CM6, 2)
poly4_CM6 = np.poly1d(coeff4_CM6)

coeff5_CM6 = np.polyfit(x_CM6, y5_CM6, 2)
poly5_CM6 = np.poly1d(coeff5_CM6)


t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y1_CM6 = poly1_CM6(curve_x_CM6)
curve_y2_CM6 = poly2_CM6(curve_x_CM6)
curve_y3_CM6 = poly3_CM6(curve_x_CM6)
curve_y4_CM6 = poly4_CM6(curve_x_CM6)
curve_y5_CM6 = poly5_CM6(curve_x_CM6)


#==========================================================================================
#==========================================================================================

#plt.rcParams.update({
#"text.usetex": True,
#"font.family": 'DejaVu Sans',
#"font.serif": ["Computer Modern Roman"],
#"font.size": 20})

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"axes.labelsize": 12,
"font.size": 12,
"legend.fontsize": 8,
"xtick.labelsize": 20,
"ytick.labelsize": 20,})


#== JOINT PLOT CM5 & CM6 ==
plt.figure(figsize=set_size(width=490)) # ANNUAL
#plt.figure(figsize=set_size(width=460)) #Seasonl
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 22)
plt.ylabel('Annual SMB anomalies [mmWE]', fontsize = 22)
#plt.title('Annual SMB component anomalies \n Model Mean of MAR CMIP5 vs. MAR CMIP6 simulations', fontsize=24) 
#plt.title('('+season+') SMB component anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=24) 

color_CM5 = ['darkolivegreen', 'firebrick','indigo']#,'darkorange','black']
label_CM5 = ['SMB - CMIP5','ME - CMIP5', 'RU - CMIP5']#, 'RZ - CMIP5', 'RF - CMIP5']
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s = 22,color = color_CM5[i], alpha=0.9)#seasonal: s=1, Annual: s=2
    sns.set_palette('colorblind')
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen', linewidth=2.5)#, linewidth=0.7)  
plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick', linewidth=2.5)#, linewidth=0.7)  
plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo', linewidth=2.5)#, linewidth=0.7)  
#plt.plot(curve_x_CM5, curve_y4_CM5, color ='black')  
#plt.plot(curve_x_CM5, curve_y5_CM5, color ='darkorange')  

color_CM6 = ['yellowgreen','lightcoral','mediumpurple']#,  'sandybrown', 'black']
label_CM6 = ['SMB - CMIP6','ME - CMIP6', 'RU - CMIP6']#, 'RZ - CMIP6', 'RF - CMIP5']
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], marker='+', linewidth=0.8,s= 80,color = color_CM6[i]) #seasnoal: s=5, Annual:s=20, linewidth=0.5,
        
    
plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen', linewidth=2.5)#, linewidth=0.7)#seasonal: linewidth=0.7  
plt.plot(curve_x_CM6, curve_y2_CM6, '--',color ='lightcoral', linewidth=2.5)#, linewidth=0.7)  
plt.plot(curve_x_CM6, curve_y3_CM6, '--', color ='mediumpurple', linewidth=2.5)#, linewidth=0.7)  

#plt.plot(curve_x_CM6, curve_y4_CM6, '--', color ='black')  
#plt.plot(curve_x_CM5, curve_y5_CM6, '--', color ='sandybrown')  
#if season == 'JJA':
#    plt.ylim(-400,400)
#else:
#    plt.ylim(-75,75)
#plt.ylim(-150,150)
plt.xlim(-1,8.5)

#remove thicks from xaixs 
#x = range(-1,8)
#plt.xticks(x, np.arange(0, 8, step=2)) #Annual and JJA



#Imports
import matplotlib.patches as mpatches


###sns.set_palette('colorblind')
sns.despine()

#-#-#- FANCY LEGEND -#-#-#
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase

class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        SMB_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='darkolivegreen')
        SMB_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', linewidth=1,color='yellowgreen')
        return [SMB_cm5, SMB_cm6]
    
class AnyObjectHandler2(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        ME_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='firebrick')
        ME_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--',linewidth=1, color='lightcoral')
        return [ME_cm5, ME_cm6]
    
class AnyObjectHandler3(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        RU_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='indigo')
        RU_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', linewidth=1,color='mediumpurple')
        return [RU_cm5, RU_cm6]
    
class AnyObjectHandler4(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm5_dott = mlines.Line2D([11],[3], color='black', marker='o', markersize=7,label='MAR CMIP5')#markersize=7, 
        return [cm5_dott]
    
class AnyObjectHandler5(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm6_cross = mlines.Line2D([11],[3], color='black', marker='+', markersize=9, label='MAR CMIP6')#markersize=9,
        return [cm6_cross]

object1 = HandlerBase()
object2 = HandlerBase()
object3 = HandlerBase()
object4 = HandlerBase()
object5 = HandlerBase()
    
#plt.legend([object1,object2, object3, object4, object5], ['SMB','ME', 'RU', 'MAR CMIP5','MAR CMIP6'],
#           handler_map={object1: AnyObjectHandler(),
#                        object2:AnyObjectHandler2(),
#                        object3:AnyObjectHandler3(),
#                        object4:AnyObjectHandler4(),
#                        object5:AnyObjectHandler5()}, 
#           fontsize=20,frameon=False,ncol=2, loc='upper left') #fontsize=16
#-#-#-#-#-#-#-#-#-#-#-#-#-#

#plt.legend(ncol=2)
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SMB_anomalies_jointCM5CM6_annual.pdf',bbox_inches='tight',dpi=300)
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SMB_anomalies_jointCM5CM6_'+season+'.pdf', bbox_inches='tight',dpi=300)

#print(season)
#print('TAS:',curve_x_CM5[-1])
#print('CMIP5', 'SMB:', np.round(poly1_CM5(curve_x_CM5[-1]),2))
#print('CMIP6', 'SMB:', np.round(poly1_CM6(curve_x_CM5[-1]),2))
#print('SMB (CMIP6 - CMIP5) =',np.round(poly1_CM6(curve_x_CM5[-1]) - poly1_CM5(curve_x_CM5[-1]),2))
#print('Standard deviation CMIP6:', np.std((poly1_CM5(curve_x_CM65[-1]),2)))
#print('Standard deviation CMIP6:', np.std((poly1_CM6(curve_x_CM5[-1]),2)))

    
    
print('TEMPERATURE:')
print('CMIP5',curve_x_CM5[-1])
print('CMIP6',curve_x_CM6[-1])

def R_square(x, y, coeff):
    """
    coeff = coeff_CM.. 
    x= x_CM6                 
    y= y1_CM6
    """
    p = np.poly1d(coeff)                  
    curve = np.polyval(coeff, x)
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssres = np.sum((y - curve)**2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    R_square = 1 - ssres / sstot
    return np.round(R_square,3)

print('R2 - CMIP5')
print('SMB',R_square(x_CM5,y1_CM5,coeff_CM5))
print('ME',R_square(x_CM5,y2_CM5,coeff2_CM5)) 
print('RU',R_square(x_CM5,y3_CM5,coeff3_CM5))
print('RF',R_square(x_CM5,y4_CM5,coeff4_CM5))
print('RZ',R_square(x_CM5,y5_CM5,coeff5_CM5))

print('R2 - CMIP6')
print('SMB',R_square(x_CM6,y1_CM6,coeff_CM6))
print('ME',R_square(x_CM6,y2_CM6,coeff2_CM6)) 
print('RU',R_square(x_CM6,y3_CM6,coeff3_CM6))
print('RF',R_square(x_CM6,y4_CM6,coeff4_CM6))
print('RZ',R_square(x_CM6,y5_CM6,coeff5_CM6))


print('SMB: f(x)=',np.round(coeff_CM5[0],2),'x$^2$','+',np.round(coeff_CM5[1],2),'x','+',np.round(coeff_CM5[2],2))
print('SMB: f(x)=',np.round(coeff_CM6[0],3),'x$^2$','+',np.round(coeff_CM6[1],2),'x','+',np.round(coeff_CM6[2],2))

print('ME: f(x)=',np.round(coeff2_CM5[0],2),'x$^2$','+',np.round(coeff2_CM5[1],2),'x','+',np.round(coeff2_CM5[2],2))
print('ME: f(x)=',np.round(coeff2_CM6[0],3),'x$^2$','+',np.round(coeff2_CM6[1],2),'x','+',np.round(coeff2_CM6[2],2))

print('RU: f(x)=',np.round(coeff3_CM5[0],2),'x$^2$','+',np.round(coeff3_CM5[1],2),'x','+',np.round(coeff3_CM5[2],2))
print('RU: f(x)=',np.round(coeff3_CM6[0],3),'x$^2$','+',np.round(coeff3_CM6[1],2),'x','+',np.round(coeff3_CM6[2],2))


"""
ANNUAL: 

R2 - CMIP5
SMB 0.96
ME 0.98
RU 0.99
RF 0.98
RZ 0.96
R2 - CMIP6
SMB 0.98
ME 0.99
RU 0.99
RF 0.97
RZ 0.96


JJA: 
R2 - CMIP5
SMB 0.99
ME 1.0
RU 1.0
RF 0.96
RZ 0.96
R2 - CMIP6
SMB 0.99
ME 1.0
RU 0.99
RF 0.97
RZ 0.96


SON:
SMB 0.15
ME 0.94
RU 0.95
RF 0.94
RZ 0.37
R2 - CMIP6
SMB 0.78
ME 0.96
RU 0.97
RF 0.96
RZ 0.22


"""
def stand_dev(x,y,coeff):
    #use y = y_CM5, x= x_CM5, coeff = coeff_CM5
    #use y = y_CM6, x= x_CM6, coeff = coeff_CM6
    c = y - (coeff[0]*(x**2) + coeff[1]*x + coeff[2])
    return c

if season =='JJA':
    TAS=5.4
if season=='SON':
    TAS=6.7
#for TAS in range(1,6):
print('Season:',season)
print('TAS:', TAS)
print('MAR CMIP5', 'SMB:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y1_CM5,coeff_CM5)[-20:]),2))
print('MAR CMIP6', 'SMB:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y1_CM6,coeff_CM6)[-20:]),2)) 
print('MAR CMIP5', 'ME:', np.round(poly2_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y2_CM5,coeff2_CM5)[-20:]),2))
print('MAR CMIP6', 'ME:', np.round(poly2_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y2_CM6,coeff2_CM6)[-20:]),2)) 
print('MAR CMIP5', 'RU:', np.round(poly3_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y3_CM5,coeff3_CM5)[-20:]),2))
print('MAR CMIP6', 'RU:', np.round(poly3_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y3_CM6,coeff3_CM6)[-20:]),2)) 

"""
TAS: 1
MAR CMIP5 SMB: -3.39 mmWE std: $\pm$ 2.69
RANGE CMIP5: [ -0.69 , -6.08 ]
MAR CMIP6 SMB: -3.68 mmWE std: $\pm$ 2.84
RANGE CMIP6: [ -0.99 , -6.53 ]

ANNUAL
TAS: 2
MAR CMIP5 SMB: -8.05 mmWE std: $\pm$ 5.02
RANGE CMIP5: [ -3.02 , -13.07 ]
MAR CMIP6 SMB: -9.33 mmWE std: $\pm$ 5.67
RANGE CMIP6: [ -4.31 , -15.0 ]

ANNUAL
TAS: 3
MAR CMIP5 SMB: -14.22 mmWE std: $\pm$ 8.11
RANGE CMIP5: [ -6.11 , -22.32 ]
MAR CMIP6 SMB: -17.67 mmWE std: $\pm$ 9.84
RANGE CMIP6: [ -9.56 , -27.51 ]

ANNUAL
TAS: 4
MAR CMIP5 SMB: -21.9 mmWE std: $\pm$ 11.95
RANGE CMIP5: [ -9.95 , -33.85 ]
MAR CMIP6 SMB: -28.69 mmWE std: $\pm$ 15.35
RANGE CMIP6: [ -16.74 , -44.04 ]

ANNUAL
TAS: 5
MAR CMIP5 SMB: -31.09 mmWE std: $\pm$ 16.55
RANGE CMIP5: [ -14.55 , -47.64 ]
MAR CMIP6 SMB: -42.4 mmWE std: $\pm$ 22.2
RANGE CMIP6: [ -25.85 , -64.6 ]

ANNUAL
TAS: 6
MAR CMIP5 SMB: -41.8 mmWE std: $\pm$ 21.9
RANGE CMIP5: [ -19.9 , -63.7 ]
MAR CMIP6 SMB: -58.79 mmWE std: $\pm$ 30.4
RANGE CMIP6: [ -36.89 , -89.19 ]



Season: JJA
TAS: 1
MAR CMIP5 SMB: -14.22 mmWE std: $\pm$ 8.11
RANGE CMIP5: [ -6.11 , -22.34 ]
MAR CMIP6 SMB: -12.13 mmWE std: $\pm$ 7.07
RANGE CMIP6: [ -4.02 , -19.2 ]

Season: JJA
TAS: 2
MAR CMIP5 SMB: -36.29 mmWE std: $\pm$ 19.15
RANGE CMIP5: [ -17.15 , -55.44 ]
MAR CMIP6 SMB: -32.69 mmWE std: $\pm$ 17.34
RANGE CMIP6: [ -13.54 , -50.03 ] 

TAS: 3
MAR CMIP5 SMB: -66.58 mmWE std: $\pm$ 34.29
RANGE CMIP5: [ -32.29 , -100.88 ]
MAR CMIP6 SMB: -63.99 mmWE std: $\pm$ 33.0
RANGE CMIP6: [ -29.7 , -96.99 ]


TAS: 4
MAR CMIP5 SMB: -105.1 mmWE std: $\pm$ 53.55
RANGE CMIP5: [ -51.55 , -158.65 ]
MAR CMIP6 SMB: -106.05 mmWE std: $\pm$ 54.03
RANGE CMIP6: [ -52.5 , -160.08 ]

Season: JJA
TAS: 5
MAR CMIP5 SMB: -151.84 mmWE std: $\pm$ 76.92
RANGE CMIP5: [ -74.92 , -228.77 ]
MAR CMIP6 SMB: -158.86 mmWE std: $\pm$ 80.43
RANGE CMIP6: [ -81.94 , -239.3 ]
(master) [idunnam@login2-nird-tos src]$ python SMB_var_timeline_JJA.py 
Enter season [MAM,JJA,SON,DJF]:SON

"""

