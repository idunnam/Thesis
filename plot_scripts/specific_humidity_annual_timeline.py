#######============== ANNUAL ============ #############

import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc

"""
#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
#CMIP5
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/ACCESS_anomaly_annual.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_cloud_annual.nc') 
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
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_cloud.nc')
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
QQP_CMIP5   = []



for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    QQP_CM5     = CMIP5_models[i].QQP.mean(dim=["X10_105","Y21_199"]) 
    
    TT_CMIP5.append(TT_CM5)
    QQP_CMIP5.append(QQP_CM5)
    
TT_CMIP5     = model_mean(TT_CMIP5)
QQP_CMIP5    = model_mean(QQP_CMIP5)


SEB_var_CMIP5 = [QQP_CMIP5]#, RZ_CMIP5, RF_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
QQP_CMIP6    = []


for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    QQP_CM6     = CMIP6_models[i].QQP.mean(dim=["X10_105","Y21_199"]) 
    
    TT_CMIP6.append(TT_CM6)
    QQP_CMIP6.append(QQP_CM6)
    
TT_CMIP6     = model_mean(TT_CMIP6)
QQP_CMIP6    = model_mean(QQP_CMIP6)

SEB_var_CMIP6 = [QQP_CMIP6]#, RZ_CMIP6, RF_CMIP6]
SEB_var_label = ['QQP']#, 'RZ', 'RF']

# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
QQP_reg_CM5 = QQP_CMIP5.to_dataframe()


#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
QQP_reg_CM6 = QQP_CMIP6.to_dataframe()


### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y1_CM5 = QQP_reg_CM5['QQP']

coeff_CM5 = np.polyfit(x_CM5, y1_CM5, 2)
poly1_CM5 = np.poly1d(coeff_CM5)




t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y1_CM5 = poly1_CM5(curve_x_CM5)


### CMIP6 ###
x_CM6  = TT_reg_CM6['TT']
y1_CM6 = QQP_reg_CM6['QQP']

coeff_CM6 = np.polyfit(x_CM6, y1_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)




t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y1_CM6 = poly1_CM6(curve_x_CM6)


#==========================================================================================
#==========================================================================================
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 20})


#== JOINT PLOT CM5 & CM6 ==
plt.figure(figsize= (10,10))
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 20)
plt.ylabel('('+season+') Specific humidity [g/kg]', fontsize = 20)
#plt.title('('+season+') - Specific humidity anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=16) 
#plt.title('Annual - Specific humidity anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize=16) 

color_CM5 = ['darkolivegreen']#,'darkorange','black']
label_CM5 = ['Specific humidity - CMIP5']#, 'RZ - CMIP5', 'RF - CMIP5']
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=22, color = color_CM5[i])
    sns.set_palette('colorblind')
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen')  ### TEST
#plt.plot(curve_x_CM5, curve_y4_CM5, color ='black')  ### TEST
#plt.plot(curve_x_CM5, curve_y5_CM5, color ='darkorange')  ### TEST

color_CM6 = ['yellowgreen']#,  'sandybrown', 'black']
label_CM6 = ['Specific humidity - CMIP6']#, 'RZ - CMIP6', 'RF - CMIP5']
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=80, marker='+',color = color_CM6[i])
    
plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen')  ### TEST
#plt.plot(curve_x_CM6, curve_y4_CM6, '--', color ='black')  ### TEST
#plt.plot(curve_x_CM5, curve_y5_CM6, '--', color ='sandybrown')  ### TEST
#if season == 'JJA':
#    plt.ylim(-400,400)
#else:
#    plt.ylim(-100,100)
#plt.ylim(-100,100)
####

#-#-#- FANCY LEGEND -#-#-#
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase

class AnyObjectHandler9(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], color='darkolivegreen')
        l2 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                linestyle='--', color='yellowgreen')
        
        return [l1, l2]
class AnyObjectHandler10(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm5_dott = mlines.Line2D([11],[3], color='black', marker='o', markersize=7, label='MAR CMIP5')
        return [cm5_dott]

class AnyObjectHandler11(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm6_cross = mlines.Line2D([11],[3], color='black', marker='+', markersize=9, label='MAR CMIP6')
        return [cm6_cross]
    
object1 = HandlerBase()
object2 = HandlerBase()
object3 = HandlerBase()
    
plt.legend([object1, object2, object3], ['Q', 'MAR CMIP5', 'MAR CMIP6'],
           handler_map={object1: AnyObjectHandler9(),
                        object2:AnyObjectHandler10(),
                        object3:AnyObjectHandler11()},
           fontsize=16,frameon=False,ncol=1, loc='upper left')
    
####
#Imports
import matplotlib.patches as mpatches


###sns.set_palette('colorblind')
sns.despine()
#plt.legend(ncol=2)
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/QQP_anomalies_jointCM5CM6_annual.pdf',bbox_inches='tight',dpi=300)
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/QQP_anomalies_jointCM5CM6_'+season+'.pdf',bbox_inches='tight',dpi=300)
