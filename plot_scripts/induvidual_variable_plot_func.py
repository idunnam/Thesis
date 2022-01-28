"""
This code is used for plotting seasonal (JJA) anomalies of radiative fluxes for the model mean of CMIP5 and CMIP6 models. 
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc

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
LWU_CMIP5    = []
LWD_CMIP5    = [] 
SWD_CMIP5    = []
ALB_CMIP5    = []
##SW_net_CMIP5 = []
#LW_net_CMIP5 = []
#Net_rad_f_CMIP5  = []

for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    LWU_CM5     = CMIP5_models[i].LWU.mean(dim=["X10_105","Y21_199"]) *(-1)
    LWD_CM5     = CMIP5_models[i].LWD.mean(dim=["X10_105","Y21_199"]) 
    SWD_CM5     = CMIP5_models[i].SWD.mean(dim=["X10_105","Y21_199"])
    ALB_CM5     = CMIP5_models[i].AL2.mean(dim=["X10_105","Y21_199"])
    #SW_net_CM5  = CMIP5_models[i].#SW_net.mean(dim=["X10_105","Y21_199"])
    #LW_net_CM5  = CMIP5_models[i].#LW_net.mean(dim=["X10_105","Y21_199"])
    #Net_rad_f_CM5   = CMIP5_models[i].#Net_rad_f.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    SWD_CMIP5.append(SWD_CM5)
    LWU_CMIP5.append(LWU_CM5)
    LWD_CMIP5.append(LWD_CM5)
    ALB_CMIP5.append(ALB_CM5)
    #SW_net_CMIP5.append(#SW_net_CM5)
    #LW_net_CMIP5.append(#LW_net_CM5)
    #Net_rad_f_CMIP5.append(#Net_rad_f_CM5)

TT_CMIP5     = model_mean(TT_CMIP5)
SWD_CMIP5    = model_mean(SWD_CMIP5)
LWU_CMIP5    = model_mean(LWU_CMIP5)
LWD_CMIP5    = model_mean(LWD_CMIP5)
ALB_CMIP5    = model_mean(ALB_CMIP5)
#SW_net_CMIP5 = model_mean(#SW_net_CMIP5)
#LW_net_CMIP5 = model_mean(#LW_net_CMIP5)
#Net_rad_f_CMIP5  = model_mean(#Net_rad_f_CMIP5)

#SEB_var_CMIP5 = [LWU_CMIP5, LWD_CMIP5, SWD_CMIP5, #SW_net_CMIP5, #LW_net_CMIP5, #Net_rad_f_CMIP5]
SEB_var_CMIP5 = [LWU_CMIP5, LWD_CMIP5, SWD_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
LWU_CMIP6    = []
LWD_CMIP6    = [] 
SWD_CMIP6    = []
ALB_CMIP6    = []
#SW_net_CMIP6 = []
#LW_net_CMIP6 = []
#Net_rad_f_CMIP6  = []

for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    LWU_CM6     = CMIP6_models[i].LWU.mean(dim=["X10_105","Y21_199"]) *(-1)
    LWD_CM6     = CMIP6_models[i].LWD.mean(dim=["X10_105","Y21_199"]) 
    SWD_CM6     = CMIP6_models[i].SWD.mean(dim=["X10_105","Y21_199"])
    ALB_CM6     = CMIP6_models[i].AL2.mean(dim=["X10_105","Y21_199"])
    #SW_net_CM6  = CMIP6_models[i].#SW_net.mean(dim=["X10_105","Y21_199"])
    #LW_net_CM6  = CMIP6_models[i].#LW_net.mean(dim=["X10_105","Y21_199"])
    #Net_rad_f_CM6   = CMIP6_models[i].#Net_rad_f.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP6.append(TT_CM6)
    SWD_CMIP6.append(SWD_CM6)
    LWU_CMIP6.append(LWU_CM6)
    LWD_CMIP6.append(LWD_CM6)
    ALB_CMIP6.append(ALB_CM6)
    #SW_net_CMIP6.append(#SW_net_CM6)
    #LW_net_CMIP6.append(#LW_net_CM6)
    #Net_rad_f_CMIP6.append(#Net_rad_f_CM6)

TT_CMIP6     = model_mean(TT_CMIP6)
SWD_CMIP6    = model_mean(SWD_CMIP6)
LWU_CMIP6    = model_mean(LWU_CMIP6)
LWD_CMIP6    = model_mean(LWD_CMIP6)
ALB_CMIP6    = model_mean(ALB_CMIP6)
#SW_net_CMIP6 = model_mean(#SW_net_CMIP6)
#LW_net_CMIP6 = model_mean(#LW_net_CMIP6)
#Net_rad_f_CMIP6  = model_mean(#Net_rad_f_CMIP6)

# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
LWU_reg_CM5 = LWU_CMIP5.to_dataframe()
LWD_reg_CM5 = LWD_CMIP5.to_dataframe()
SWD_reg_CM5 = SWD_CMIP5.to_dataframe()
ALB_reg_CM5 = ALB_CMIP5.to_dataframe()
#SW_net_reg_CM5 = #SW_net_CMIP5.to_dataframe()
#LW_net_reg_CM5 = #LW_net_CMIP5.to_dataframe()
#Net_rad_f_reg_CM5 = #Net_rad_f_CMIP5.to_dataframe()


#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
LWU_reg_CM6 = LWU_CMIP6.to_dataframe()
LWD_reg_CM6 = LWD_CMIP6.to_dataframe()
SWD_reg_CM6 = SWD_CMIP6.to_dataframe()
ALB_reg_CM6 = ALB_CMIP6.to_dataframe()
#SW_net_reg_CM6 = #SW_net_CMIP6.to_dataframe()
#LW_net_reg_CM6 = #LW_net_CMIP6.to_dataframe()
#Net_rad_f_reg_CM6 = #Net_rad_f_CMIP6.to_dataframe()


### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y1_CM5 = LWU_reg_CM5['LWU']
y2_CM5 = LWD_reg_CM5['LWD']
y3_CM5 = SWD_reg_CM5['SWD']
y4_CM5 = ALB_reg_CM5['AL2']
#y5_CM5 = #SW_net_reg_CM5['#SW_net']
#y7_CM5 = #LW_net_reg_CM5['#LW_net']
#y6_CM5 = #Net_rad_f_reg_CM5['#Net_rad_f']

coeff_CM5 = np.polyfit(x_CM5, y1_CM5,2)
poly1_CM5 = np.poly1d(coeff_CM5)

coeff2_CM5 = np.polyfit(x_CM5, y2_CM5, 2)
poly2_CM5 = np.poly1d(coeff2_CM5)

coeff3_CM5 = np.polyfit(x_CM5, y3_CM5, 2)
poly3_CM5 = np.poly1d(coeff3_CM5)

coeff4_CM5 = np.polyfit(x_CM5, y4_CM5, 2)
poly4_CM5 = np.poly1d(coeff4_CM5)

#coeff5_CM5 = np.polyfit(x_CM5, y5_CM5, 2)
#poly5_CM5 = np.poly1d(coeff5_CM5)

#coeff7_CM5 = np.polyfit(x_CM5, y7_CM5, 2)
#poly7_CM5 = np.poly1d(coeff7_CM5)

#coeff6_CM5 = np.polyfit(x_CM5, y6_CM5, 2)
#poly6_CM5 = np.poly1d(coeff6_CM5)

t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y1_CM5 = poly1_CM5(curve_x_CM5)
curve_y2_CM5 = poly2_CM5(curve_x_CM5)
curve_y3_CM5 = poly3_CM5(curve_x_CM5)
curve_y4_CM5 = poly4_CM5(curve_x_CM5)
#curve_y5_CM5 = poly5_CM5(curve_x_CM5)
#curve_y7_CM5 = poly7_CM5(curve_x_CM5)
#curve_y6_CM5 = poly6_CM5(curve_x_CM5)

### CMIP6 ###
x_CM6  = TT_reg_CM6['TT']
y1_CM6 = LWU_reg_CM6['LWU']
y2_CM6 = LWD_reg_CM6['LWD']
y3_CM6 = SWD_reg_CM6['SWD']
y4_CM6 = ALB_reg_CM6['AL2']
#y5_CM6 = #SW_net_reg_CM6['#SW_net']
#y7_CM6 = #LW_net_reg_CM6['#LW_net']
#y6_CM6 = #Net_rad_f_reg_CM6['#Net_rad_f']

coeff_CM6 = np.polyfit(x_CM6, y1_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)

coeff2_CM6 = np.polyfit(x_CM6, y2_CM6, 2)
poly2_CM6 = np.poly1d(coeff2_CM6)

coeff3_CM6 = np.polyfit(x_CM6, y3_CM6, 2)
poly3_CM6 = np.poly1d(coeff3_CM6)

coeff4_CM6 = np.polyfit(x_CM6, y4_CM6, 2)
poly4_CM6 = np.poly1d(coeff4_CM6)

#coeff5_CM6 = np.polyfit(x_CM6, y5_CM6, 2)
#poly5_CM6 = np.poly1d(coeff5_CM6)

#coeff7_CM6 = np.polyfit(x_CM6, y7_CM6, 2)
#poly7_CM6 = np.poly1d(coeff7_CM6)

#coeff6_CM6 = np.polyfit(x_CM6, y6_CM6, 2)
#poly6_CM6 = np.poly1d(coeff6_CM6)

t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y1_CM6 = poly1_CM6(curve_x_CM6)
curve_y2_CM6 = poly2_CM6(curve_x_CM6)
curve_y3_CM6 = poly3_CM6(curve_x_CM6)
curve_y4_CM6 = poly4_CM6(curve_x_CM6)
#curve_y5_CM6 = poly5_CM6(curve_x_CM6)
#curve_y7_CM6 = poly7_CM6(curve_x_CM6)
#curve_y6_CM6 = poly6_CM6(curve_x_CM6)

#fig.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_rad_flux_anomalies_CMIP5_CMIP6_JJA.png')
#==========================================================================================
#==========================================================================================

curve_x_CM5_std = np.std(curve_x_CM5)
curve_x_CM5_std = np.round(curve_x_CM5_std)
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})



plt.figure(figsize= (10,10))
plt.xlabel('xlabel', fontsize = 14)
plt.ylabel('ylabel', fontsize = 14)
plt.title('title', fontsize=16)
plt.scatter(ACCESS.TT.mean(dim=["X10_105","Y21_199"]), ACCESS.SWD.mean(dim=["X10_105","Y21_199"]))
plt.fill_between(curve_x_CM5+curve_x_CM5_std, curve_x_CM5-curve_x_CM5_std)
plt.plot(curve_x_CM5, curve_y3_CM5)
plt.savefig('test_indu.png')
plt.show()

"""
#== JOINT PLOT CM5 & CM6 ==
def induvidual_var_plot(xlabel=None, ylabel=None,title=None, label_CM5, SEB_var_CMIP5):

    plt.figure(figsize= (10,10))
    plt.xlabel(xlabel, fontsize = 14)
    plt.ylabel(ylabel, fontsize = 14)
    plt.title(title, fontsize=16) 
#plt.title('CMIP5 & CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies') 

    color_CM5 = ['darkolivegreen', 'firebrick','indigo','darkorange', 'steelblue','dimgrey']
    label_CM5 = [label_CM5]
    for i in range(len(SEB_var_CMIP5)):
        plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=10, color = color_CM5[i])
        #sns.set_palette('colorblind')
    
    plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen')  ### TEST
    plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick')  ### TEST
    plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo')  ### TEST
    plt.plot(curve_x_CM5, curve_y5_CM5, color ='darkorange')  ### TEST
    plt.plot(curve_x_CM5, curve_y7_CM5, color ='steelblue')  ### #LW_net
    plt.plot(curve_x_CM5, curve_y6_CM5, color = 'dimgrey')

    color_CM6 = ['yellowgreen','lightcoral','mediumpurple',  'sandybrown','lightskyblue','darkgrey']
    label_CM6 = ['LWU - CMIP6','LWD - CMIP6', 'SWD - CMIP6', 'SW$_{net}$- CMIP6','LW$_{net}$- CMIP6', 'Net radiative flux - CMIP6' ]
    for i in range(len(SEB_var_CMIP6)):
        plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=10, marker='x',color = color_CM6[i])
    
    plt.set_title('CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies')
    plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen')  ### TEST
    plt.plot(curve_x_CM6, curve_y2_CM6, '--',color ='lightcoral')  ### TEST
    plt.plot(curve_x_CM6, curve_y3_CM6, '--', color ='mediumpurple')  ### TEST
    plt.plot(curve_x_CM6, curve_y5_CM6, '--', color ='sandybrown')  ### TEST
    plt.plot(curve_x_CM6, curve_y7_CM6, '--', color ='lightskyblue')  ### #LW_net
    plt.plot(curve_x_CM6, curve_y6_CM6, '--', color = 'darkgrey')


    #Imports
    import matplotlib.patches as mpatches


    ###sns.set_palette('colorblind')
    sns.despine()
    plt.legend(ncol=2)
    plt.show()
    plt.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_components/SEB_rad_flux_anomalies_jointCM5CM6_JJA.png')

"""