"""
This code is used for plotting seasonal (JJA) anomalies of precipitation and refreezing for the model mean of CMIP5 and CMIP6 models. 
"""
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
CNRM_CM6  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_'+season+'.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_'+season+'.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_'+season+'.nc')       
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_'+season+'.nc')      


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
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    PR_CM5     = CMIP5_models[i].PR.mean(dim=["X10_105","Y21_199"]) 
    SF_CM5     = CMIP5_models[i].SF.mean(dim=["X10_105","Y21_199"]) 
    RF_CM5     = CMIP5_models[i].RF.mean(dim=["X10_105","Y21_199"])
    RZ_CM5     = CMIP5_models[i].RZ.mean(dim=["X10_105","Y21_199"])
    
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

SEB_var_CMIP5 = [PR_CMIP5, SF_CMIP5, RF_CMIP5, RZ_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
PR_CMIP6    = []
SF_CMIP6    = [] 
RF_CMIP6    = []
RZ_CMIP6    = []


for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    PR_CM6     = CMIP6_models[i].PR.mean(dim=["X10_105","Y21_199"]) 
    SF_CM6     = CMIP6_models[i].SF.mean(dim=["X10_105","Y21_199"]) 
    RF_CM6     = CMIP6_models[i].RF.mean(dim=["X10_105","Y21_199"])
    RZ_CM6     = CMIP6_models[i].RZ.mean(dim=["X10_105","Y21_199"])
    
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

SEB_var_CMIP6 = [PR_CMIP6, SF_CMIP6, RF_CMIP6, RZ_CMIP6]
SEB_var_label = ['PR','SF','RF','RZ']

# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
PR_reg_CM5 = PR_CMIP5.to_dataframe()
SF_reg_CM5 = SF_CMIP5.to_dataframe()
RF_reg_CM5 = RF_CMIP5.to_dataframe()
RZ_reg_CM5 = RZ_CMIP5.to_dataframe()


#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
PR_reg_CM6 = PR_CMIP6.to_dataframe()
SF_reg_CM6 = SF_CMIP6.to_dataframe()
RF_reg_CM6 = RF_CMIP6.to_dataframe()
RZ_reg_CM6 = RZ_CMIP6.to_dataframe()


### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y1_CM5 = PR_reg_CM5['PR']
y2_CM5 = SF_reg_CM5['SF']
y3_CM5 = RF_reg_CM5['RF']
y4_CM5 = RZ_reg_CM5['RZ']

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
y1_CM6 = PR_reg_CM6['PR']
y2_CM6 = SF_reg_CM6['SF']
y3_CM6 = RF_reg_CM6['RF']
y4_CM6 = RZ_reg_CM6['RZ']

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

#fig.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_rad_flux_anomalies_CMIP5_CMIP6_JJA.png')
#==========================================================================================
#==========================================================================================
#plt.rcParams.update({
#"text.usetex": True,
#"font.family": 'DejaVu Sans',
#"font.serif": ["Computer Modern Roman"]})


#== JOINT PLOT CM5 & CM6 ==
plt.figure(figsize= (10,10))
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 14)
plt.ylabel('Anomalies [mmWE$]', fontsize = 14)
plt.title('Seasonal ('+season+') Precipitation and Refreezing anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=16) 
#plt.title('CMIP5 & CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies') 

color_CM5 = ['darkolivegreen', 'firebrick','indigo','darkorange']
label_CM5 = ['PR - CMIP5','SF - CMIP5', 'RF - CMIP5', 'RZ - CMIP5']
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=10, color = color_CM5[i])
    #sns.set_palette('colorblind')
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen')  ### TEST
plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick')  ### TEST
plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo')  ### TEST
plt.plot(curve_x_CM5, curve_y4_CM5, color ='darkorange')  ### TEST

color_CM6 = ['yellowgreen','lightcoral','mediumpurple',  'sandybrown']
label_CM6 = ['PR - CMIP6','SF - CMIP6', 'RF - CMIP6', 'SZ - CMIP6' ]
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=10, marker='x',color = color_CM6[i])
    
#plt.set_title('CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies')
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
#plt.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_components/SEB_rad_flux_anomalies_jointCM5CM6_JJA.png')
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/precip_rz_anomalies_jointCM5CM6_'+season+'.png')



#== JOINT PLOT CM5 & CM6 ==
plt.figure(figsize= (10,10))
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 14)
plt.ylabel('Precipitation [mmWE]', fontsize = 14)
#plt.title('Seasonal ('+season+') Precipitation and Refreezing anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=16) 
#plt.title('CMIP5 & CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies') 

color_CM5 = ['darkolivegreen']
label_CM5 = ['PR - CMIP5']
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[0], label= label_CM5[0], s=10, color = color_CM5[0])
    #sns.set_palette('colorblind')
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen')  ### TEST
#plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick')  ### TEST
#plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo')  ### TEST
#plt.plot(curve_x_CM5, curve_y4_CM5, color ='darkorange')  ### TEST

color_CM6 = ['yellowgreen']
label_CM6 = ['PR - CMIP6']
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[0] ,label = label_CM6[0], s=10, marker='x',color = color_CM6[0])
    
#plt.set_title('CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies')
plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen')  ### TEST
#plt.plot(curve_x_CM6, curve_y2_CM6, '--',color ='lightcoral')  ### TEST
#plt.plot(curve_x_CM6, curve_y3_CM6, '--', color ='mediumpurple')  ### TEST
#plt.plot(curve_x_CM6, curve_y4_CM6, '--', color ='sandybrown')  ### TEST


#Imports
import matplotlib.patches as mpatches


###sns.set_palette('colorblind')
sns.despine()
plt.legend(ncol=2)
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_components/SEB_rad_flux_anomalies_jointCM5CM6_JJA.png')
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/precip_anomalies_jointCM5CM6_'+season+'.png')

def R_std(y, x,coeff, n):
    y_hat = (coeff[0]*x**2 + coeff[1]*x + coeff[2])
    return np.sqrt(np.sum((y - y_hat)**2)/(n-3))

if season =='JJA':
    TAS=5.4

    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    print('MAR CMIP6', 'PR:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y1_CM5[-20:],x_CM5,coeff_CM5, 20))
    print('MAR CMIP6', 'PR:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y1_CM6[126:146],x_CM6,coeff_CM6, 20))
    
    
      
if season=='SON':
    TAS=6.7
    
    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    print('MAR CMIP5', 'PR:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y1_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'PR:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y1_CM6[117:137],x_CM6,coeff_CM6, 20))
    