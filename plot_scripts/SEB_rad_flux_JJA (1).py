"""
This code is used for plotting seasonal (JJA) anomalies of radiative fluxes for the model mean of CMIP5 and CMIP6 models. 
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd
import scipy as sc
from latex_size import set_size 


season= input('Enter season [MAM,JJA,SON,DJF]:')

ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_'+season+'.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'.nc')
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
LWU_CMIP5    = []
LWD_CMIP5    = [] 
SWD_CMIP5    = []
ALB_CMIP5    = []
SW_net_CMIP5 = []
LW_net_CMIP5 = []
Net_rad_f_CMIP5  = []

for i in range(len(CMIP5_models)):
    TT_CM5      = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    LWU_CM5     = CMIP5_models[i].LWU.mean(dim=["X10_105","Y21_199"]) *(-1)
    LWD_CM5     = CMIP5_models[i].LWD.mean(dim=["X10_105","Y21_199"]) 
    SWD_CM5     = CMIP5_models[i].SWD.mean(dim=["X10_105","Y21_199"])
    ALB_CM5     = CMIP5_models[i].AL2.mean(dim=["X10_105","Y21_199"])*100
    SW_net_CM5  = CMIP5_models[i].SW_net.mean(dim=["X10_105","Y21_199"])
    LW_net_CM5  = CMIP5_models[i].LW_net.mean(dim=["X10_105","Y21_199"])
    Net_rad_f_CM5   = CMIP5_models[i].NET_rad_f.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    SWD_CMIP5.append(SWD_CM5)
    LWU_CMIP5.append(LWU_CM5)
    LWD_CMIP5.append(LWD_CM5)
    ALB_CMIP5.append(ALB_CM5)
    SW_net_CMIP5.append(SW_net_CM5)
    LW_net_CMIP5.append(LW_net_CM5)
    Net_rad_f_CMIP5.append(Net_rad_f_CM5)

TT_CMIP5     = model_mean(TT_CMIP5)
SWD_CMIP5    = model_mean(SWD_CMIP5)
LWU_CMIP5    = model_mean(LWU_CMIP5)
LWD_CMIP5    = model_mean(LWD_CMIP5)
ALB_CMIP5    = model_mean(ALB_CMIP5)
SW_net_CMIP5 = model_mean(SW_net_CMIP5)
LW_net_CMIP5 = model_mean(LW_net_CMIP5)
Net_rad_f_CMIP5  = model_mean(Net_rad_f_CMIP5)

SEB_var_CMIP5 = [LWU_CMIP5, LWD_CMIP5, SWD_CMIP5, SW_net_CMIP5, LW_net_CMIP5, Net_rad_f_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
LWU_CMIP6    = []
LWD_CMIP6    = [] 
SWD_CMIP6    = []
ALB_CMIP6    = []
SW_net_CMIP6 = []
LW_net_CMIP6 = []
Net_rad_f_CMIP6  = []

for i in range(len(CMIP6_models)):
    TT_CM6      = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    LWU_CM6     = CMIP6_models[i].LWU.mean(dim=["X10_105","Y21_199"]) *(-1)
    LWD_CM6     = CMIP6_models[i].LWD.mean(dim=["X10_105","Y21_199"]) 
    SWD_CM6     = CMIP6_models[i].SWD.mean(dim=["X10_105","Y21_199"])
    ALB_CM6     = CMIP6_models[i].AL2.mean(dim=["X10_105","Y21_199"])*100
    SW_net_CM6  = CMIP6_models[i].SW_net.mean(dim=["X10_105","Y21_199"])
    LW_net_CM6  = CMIP6_models[i].LW_net.mean(dim=["X10_105","Y21_199"])
    Net_rad_f_CM6   = CMIP6_models[i].NET_rad_f.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP6.append(TT_CM6)
    SWD_CMIP6.append(SWD_CM6)
    LWU_CMIP6.append(LWU_CM6)
    LWD_CMIP6.append(LWD_CM6)
    ALB_CMIP6.append(ALB_CM6)
    SW_net_CMIP6.append(SW_net_CM6)
    LW_net_CMIP6.append(LW_net_CM6)
    Net_rad_f_CMIP6.append(Net_rad_f_CM6)

TT_CMIP6     = model_mean(TT_CMIP6)
SWD_CMIP6    = model_mean(SWD_CMIP6)
LWU_CMIP6    = model_mean(LWU_CMIP6)
LWD_CMIP6    = model_mean(LWD_CMIP6)
ALB_CMIP6    = model_mean(ALB_CMIP6)
SW_net_CMIP6 = model_mean(SW_net_CMIP6)
LW_net_CMIP6 = model_mean(LW_net_CMIP6)
Net_rad_f_CMIP6  = model_mean(Net_rad_f_CMIP6)

SEB_var_CMIP6 = [LWU_CMIP6, LWD_CMIP6, SWD_CMIP6, SW_net_CMIP6, LW_net_CMIP6,Net_rad_f_CMIP6]
SEB_var_label = ['LWU','LWD','SWD','SW$_{net}$', 'LW$_{net}$','Net energy flux']

# ==== REGRESSION =====
# CMIP5
TT_reg_CM5 = TT_CMIP5.to_dataframe()
LWU_reg_CM5 = LWU_CMIP5.to_dataframe()
LWD_reg_CM5 = LWD_CMIP5.to_dataframe()
SWD_reg_CM5 = SWD_CMIP5.to_dataframe()
ALB_reg_CM5 = ALB_CMIP5.to_dataframe()
SW_net_reg_CM5 = SW_net_CMIP5.to_dataframe()
LW_net_reg_CM5 = LW_net_CMIP5.to_dataframe()
Net_rad_f_reg_CM5 = Net_rad_f_CMIP5.to_dataframe()


#CMIP6
TT_reg_CM6 = TT_CMIP6.to_dataframe()
LWU_reg_CM6 = LWU_CMIP6.to_dataframe()
LWD_reg_CM6 = LWD_CMIP6.to_dataframe()
SWD_reg_CM6 = SWD_CMIP6.to_dataframe()
ALB_reg_CM6 = ALB_CMIP6.to_dataframe()
SW_net_reg_CM6 = SW_net_CMIP6.to_dataframe()
LW_net_reg_CM6 = LW_net_CMIP6.to_dataframe()
Net_rad_f_reg_CM6 = Net_rad_f_CMIP6.to_dataframe()


### CMIP5 ###
x_CM5  = TT_reg_CM5['TT']
y1_CM5 = LWU_reg_CM5['LWU']
y2_CM5 = LWD_reg_CM5['LWD']
y3_CM5 = SWD_reg_CM5['SWD']
y4_CM5 = ALB_reg_CM5['AL2']
y5_CM5 = SW_net_reg_CM5['SW_net']
y7_CM5 = LW_net_reg_CM5['LW_net']
y6_CM5 = Net_rad_f_reg_CM5['NET_rad_f']

coeff_CM5 = np.polyfit(x_CM5, y1_CM5,2)
poly1_CM5 = np.poly1d(coeff_CM5)

coeff2_CM5 = np.polyfit(x_CM5, y2_CM5, 2)
poly2_CM5 = np.poly1d(coeff2_CM5)

coeff3_CM5 = np.polyfit(x_CM5, y3_CM5, 2)
poly3_CM5 = np.poly1d(coeff3_CM5)

coeff4_CM5 = np.polyfit(x_CM5, y4_CM5, 2)
poly4_CM5 = np.poly1d(coeff4_CM5)

coeff5_CM5 = np.polyfit(x_CM5, y5_CM5, 2)
poly5_CM5 = np.poly1d(coeff5_CM5)

coeff7_CM5 = np.polyfit(x_CM5, y7_CM5, 2)
poly7_CM5 = np.poly1d(coeff7_CM5)

coeff6_CM5 = np.polyfit(x_CM5, y6_CM5, 2)
poly6_CM5 = np.poly1d(coeff6_CM5)

t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y1_CM5 = poly1_CM5(curve_x_CM5)
curve_y2_CM5 = poly2_CM5(curve_x_CM5)
curve_y3_CM5 = poly3_CM5(curve_x_CM5)
curve_y4_CM5 = poly4_CM5(curve_x_CM5)
curve_y5_CM5 = poly5_CM5(curve_x_CM5)
curve_y7_CM5 = poly7_CM5(curve_x_CM5)
curve_y6_CM5 = poly6_CM5(curve_x_CM5)

### CMIP6 ###
x_CM6  = TT_reg_CM6['TT']
y1_CM6 = LWU_reg_CM6['LWU']
y2_CM6 = LWD_reg_CM6['LWD']
y3_CM6 = SWD_reg_CM6['SWD']
y4_CM6 = ALB_reg_CM6['AL2']
y5_CM6 = SW_net_reg_CM6['SW_net']
y7_CM6 = LW_net_reg_CM6['LW_net']
y6_CM6 = Net_rad_f_reg_CM6['NET_rad_f']

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

coeff7_CM6 = np.polyfit(x_CM6, y7_CM6, 2)
poly7_CM6 = np.poly1d(coeff7_CM6)

coeff6_CM6 = np.polyfit(x_CM6, y6_CM6, 2)
poly6_CM6 = np.poly1d(coeff6_CM6)

t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y1_CM6 = poly1_CM6(curve_x_CM6)
curve_y2_CM6 = poly2_CM6(curve_x_CM6)
curve_y3_CM6 = poly3_CM6(curve_x_CM6)
curve_y4_CM6 = poly4_CM6(curve_x_CM6)
curve_y5_CM6 = poly5_CM6(curve_x_CM6)
curve_y7_CM6 = poly7_CM6(curve_x_CM6)
curve_y6_CM6 = poly6_CM6(curve_x_CM6)

#fig.savefig('/projects/NS9600K/idunnam/src/Figures/SEB_rad_flux_anomalies_CMIP5_CMIP6_JJA.png')
#==========================================================================================
#==========================================================================================
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif":  ["Computer Modern Roman"],
"font.size":   20})


#== JOINT PLOT CM5 & CM6 ==
#plt.figure(figsize= (10,10))
plt.figure(figsize= (6.4,6.4))
#plt.figure(figsize=set_size(width=460, fraction=1))
#plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 20)
plt.ylabel('Surface energy flux anomalies [Wm$^{-2}$]', fontsize = 20)   
plt.title(season, fontsize = 32, fontweight='extra bold')
#plt.title('('+season+') SEB Radiative flux component anomalies \n Model Mean of MAR CMIP5 vs. MAR CMIP6 simulations', fontsize=24) 
#plt.title('CMIP5 & CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies') 

color_CM5 = ['darkolivegreen', 'firebrick','indigo','darkorange', 'steelblue','dimgrey']
label_CM5 = ['LWU - CMIP5','LWD - CMIP5', 'SWD - CMIP5', 'SW$_{net}$- CMIP5','LW$_{net}$- CMIP5','Net radiative flux - CMIP5' ]
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=17, color = color_CM5[i], alpha=0.8)
    #sns.set_palette('colorblind')
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM5, curve_y5_CM5, color ='darkorange', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM5, curve_y7_CM5, color ='steelblue', linewidth=1.5)  ### LW_net
plt.plot(curve_x_CM5, curve_y6_CM5, color = 'dimgrey', linewidth=1.5)

color_CM6 = ['yellowgreen','lightcoral','mediumpurple',  'sandybrown','lightskyblue','darkgrey']
label_CM6 = ['LWU - CMIP6','LWD - CMIP6', 'SWD - CMIP6', 'SW$_{net}$- CMIP6','LW$_{net}$- CMIP6', 'Net radiative flux - CMIP6' ]
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=60, marker='+',color = color_CM6[i], linewidth=0.8)
    
#plt.set_title('CMIP6 Model Mean - Seasonal (JJA) SEB Radiative flux component anomalies')
plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM6, curve_y2_CM6, '--',color ='lightcoral', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM6, curve_y3_CM6, '--', color ='mediumpurple', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM6, curve_y5_CM6, '--', color ='sandybrown', linewidth=1.5)  ### TEST
plt.plot(curve_x_CM6, curve_y7_CM6, '--', color ='lightskyblue', linewidth=1.5)  ### LW_net
plt.plot(curve_x_CM6, curve_y6_CM6, '--', color = 'darkgrey', linewidth=1.5)
plt.ylim(-40,40)
plt.xlim(-1,8.5)

#-#-#- FANCY LEGEND -#-#-#
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase


class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        LWU_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='darkolivegreen')
        LWU_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='yellowgreen')
        return [LWU_cm5, LWU_cm6]
    
class AnyObjectHandler2(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        LWD_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='firebrick')
        LWD_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='lightcoral')
        return [LWD_cm5, LWD_cm6]
    
class AnyObjectHandler3(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        SWD_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='indigo')
        SWD_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='mediumpurple')
        return [SWD_cm5, SWD_cm6]
    
class AnyObjectHandler4(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        SW_net_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='darkorange')
        SW_net_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='sandybrown')
        return [SW_net_cm5, SW_net_cm6]
    
class AnyObjectHandler5(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        LW_net_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='steelblue')
        LW_net_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='lightskyblue')
        return [LW_net_cm5, LW_net_cm6]
    
class AnyObjectHandler6(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        NET_rad_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='dimgrey')
        NET_rad_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='darkgrey')
        return [NET_rad_cm5, NET_rad_cm6]

class AnyObjectHandler7(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm5_dott = mlines.Line2D([11],[3], color='black', marker='o', markersize=5, label='MAR CMIP5')
        return [cm5_dott]

class AnyObjectHandler8(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm6_cross = mlines.Line2D([11],[3], color='black', marker='+', markersize=7, label='MAR CMIP6')
        return [cm6_cross]

object1 = HandlerBase()
object2 = HandlerBase()
object3 = HandlerBase()
object4 = HandlerBase()
object5 = HandlerBase()
object6 = HandlerBase()
object7 = HandlerBase()
object8 = HandlerBase()
    
#"""
plt.legend([object1,object2, object3, object4, object5, object6, object7, object8], ['LWU','LWD', 'SWD', 'SW$_{net}$','LW$_{net}$', 'Net radiative flux','MAR CMIP5','MAR CMIP6'],
           handler_map={object1: AnyObjectHandler(),
                        object2:AnyObjectHandler2(),
                        object3:AnyObjectHandler3(),
                        object4:AnyObjectHandler4(),
                        object5:AnyObjectHandler5(),
                        object6:AnyObjectHandler6(),
                        object7:AnyObjectHandler7(),
                        object8:AnyObjectHandler8()}, 
           fontsize=11,frameon=False,ncol=3, loc='lower left')
#"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#


#Imports
import matplotlib.patches as mpatches


###sns.set_palette('colorblind')
sns.despine()
#plt.legend(ncol=2)
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/SEB_rad_flux_anomalies_jointCM5CM6_JJA.pdf,bbox_inches='tight',dpi=300')
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/Albedo_anomalies_JOINT_CMIP5_CMIP6_'+season+'.png',bbox_inches='tight',dpi=300)
#

#==========================================================================================
#== ALBEDO ==
#plt.figure(figsize=(10,10))
plt.figure(figsize=set_size(width=460, fraction=1))
plt.scatter(TT_CMIP5, ALB_CMIP5, label= 'ALB - CMIP5', s=22, color='saddlebrown')

plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 20)
plt.ylabel('('+season+')Albedo anomalies [$\%$]', fontsize = 20)

plt.plot(curve_x_CM5, curve_y4_CM5, color='saddlebrown')  ### TEST

plt.scatter(TT_CMIP6, ALB_CMIP6, label='ALB - CMIP6', s=80, marker = '+', color='tan')
#plt.title('Seasonal ('+season+') Albedo anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize = 16)

#plt.legend(loc='upper right')

####
from matplotlib.legend_handler import HandlerBase

class AnyObjectHandler9(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], color='saddlebrown')
        l2 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                linestyle='--', color='tan')
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
    
plt.legend([object1, object2, object3], ['Albedo', 'MAR CMIP5', 'MAR CMIP6'],
           handler_map={object1: AnyObjectHandler9(),
                        object2:AnyObjectHandler10(),
                        object3:AnyObjectHandler11()},
           fontsize=16,frameon=False,ncol=1, loc='lower left')
    
####

plt.plot(curve_x_CM6, curve_y4_CM6, '--', color ='tan')  ### TEST

plt.xlim(-1,8)
sns.set_palette('colorblind')
sns.despine()
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/Albedo_anomalies_JOINT_CMIP5_CMIP6_JJA.pdf',bbox_inches='tight',dpi=300)
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/Albedo_anomalies_JOINT_CMIP5_CMIP6_'+season+'.pdf',bbox_inches='tight',dpi=300)
#==========================================================================================

#==========================================================================================
#=========================================================================================
def R_std(y, x,coeff, n):
    y_hat = (coeff[0]*x**2 + coeff[1]*x + coeff[2])
    return np.sqrt(np.sum((y - y_hat)**2)/(n-3))

if season =='JJA':
    TAS=5.4

    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    #print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y_CM5,coeff_CM5)),2))
    #print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y_CM6,coeff_CM6)),2))
    #print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',np.std(R_std(x_CM5,y_CM5,coeff_CM5, 20)[-20:]))
    #print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',np.std(R_std(x_CM6,y_CM6,coeff_CM6, 20)[126:146]))
    print('MAR CMIP5', 'LWU:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y1_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'LWU:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y1_CM6[126:146],x_CM6,coeff_CM6, 20))
    print('MAR CMIP5', 'LWD:', np.round(poly2_CM5(TAS),2),'%','std: $\pm$',R_std(y2_CM5[-20:],x_CM5[-20:],coeff2_CM5, 20))
    print('MAR CMIP6', 'LWD:', np.round(poly2_CM6(TAS),2),'%','std: $\pm$',R_std(y2_CM6[126:146],x_CM6,coeff2_CM6, 20))
    print('MAR CMIP5', 'SWD:', np.round(poly3_CM5(TAS),2),'%','std: $\pm$',R_std(y3_CM5[-20:],x_CM5[-20:],coeff3_CM5, 20))
    print('MAR CMIP6', 'SWD:', np.round(poly3_CM6(TAS),2),'%','std: $\pm$',R_std(y3_CM6[126:146],x_CM6,coeff3_CM6, 20))
    print('MAR CMIP5', 'ALB:', np.round(poly4_CM5(TAS),2),'%','std: $\pm$',R_std(y4_CM5[-20:],x_CM5[-20:],coeff4_CM5, 20))
    print('MAR CMIP6', 'ALB:', np.round(poly4_CM6(TAS),2),'%','std: $\pm$',R_std(y4_CM6[126:146],x_CM6,coeff4_CM6, 20))
    print('MAR CMIP5', 'SW_net:', np.round(poly5_CM5(TAS),2),'%','std: $\pm$',R_std(y5_CM5[-20:],x_CM5[-20:],coeff5_CM5, 20))
    print('MAR CMIP6', 'SW_net:', np.round(poly5_CM6(TAS),2),'%','std: $\pm$',R_std(y5_CM6[126:146],x_CM6,coeff5_CM6, 20))
    print('MAR CMIP5', 'NET_r:', np.round(poly6_CM5(TAS),2),'%','std: $\pm$',R_std(y6_CM5[-20:],x_CM5[-20:],coeff6_CM5, 20))
    print('MAR CMIP6', 'NET_r:', np.round(poly6_CM6(TAS),2),'%','std: $\pm$',R_std(y6_CM6[126:146],x_CM6,coeff6_CM6, 20))
    print('MAR CMIP5', 'LW_net:', np.round(poly7_CM5(TAS),2),'%','std: $\pm$',R_std(y7_CM5[-20:],x_CM5[-20:],coeff7_CM5, 20))
    print('MAR CMIP6', 'LW_net:', np.round(poly7_CM6(TAS),2),'%','std: $\pm$',R_std(y7_CM6[126:146],x_CM6,coeff7_CM6, 20))
    
    
      
if season=='SON':
    TAS=6.7
    
    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    #print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y_CM5,coeff_CM5)),2))
    #print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y_CM6,coeff_CM6)),2))
    print('MAR CMIP5', 'LWU:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y1_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'LWU:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y1_CM6[117:137],x_CM6,coeff_CM6, 20))
    print('MAR CMIP5', 'LWD:', np.round(poly2_CM5(TAS),2),'%','std: $\pm$',R_std(y2_CM5[-20:],x_CM5[-20:],coeff2_CM5, 20))
    print('MAR CMIP6', 'LWD:', np.round(poly2_CM6(TAS),2),'%','std: $\pm$',R_std(y2_CM6[117:137],x_CM6,coeff2_CM6, 20))
    print('MAR CMIP5', 'SWD:', np.round(poly3_CM5(TAS),2),'%','std: $\pm$',R_std(y3_CM5[-20:],x_CM5[-20:],coeff3_CM5, 20))
    print('MAR CMIP6', 'SWD:', np.round(poly3_CM6(TAS),2),'%','std: $\pm$',R_std(y3_CM6[117:137],x_CM6,coeff3_CM6, 20))
    print('MAR CMIP5', 'ALB:', np.round(poly4_CM5(TAS),2),'%','std: $\pm$',R_std(y4_CM5[-20:],x_CM5[-20:],coeff4_CM5, 20))
    print('MAR CMIP6', 'ALB:', np.round(poly4_CM6(TAS),2),'%','std: $\pm$',R_std(y4_CM6[117:137],x_CM6,coeff4_CM6, 20))
    print('MAR CMIP5', 'SW_net:', np.round(poly5_CM5(TAS),2),'%','std: $\pm$',R_std(y5_CM5[-20:],x_CM5[-20:],coeff5_CM5, 20))
    print('MAR CMIP6', 'SW_net:', np.round(poly5_CM6(TAS),2),'%','std: $\pm$',R_std(y5_CM6[117:137],x_CM6,coeff5_CM6, 20))
    print('MAR CMIP5', 'NET_r:', np.round(poly6_CM5(TAS),2),'%','std: $\pm$',R_std(y6_CM5[-20:],x_CM5[-20:],coeff6_CM5, 20))
    print('MAR CMIP6', 'NET_r:', np.round(poly6_CM6(TAS),2),'%','std: $\pm$',R_std(y6_CM6[117:137],x_CM6,coeff6_CM6, 20))
    print('MAR CMIP5', 'LW_net:', np.round(poly7_CM5(TAS),2),'%','std: $\pm$',R_std(y7_CM5[-20:],x_CM5[-20:],coeff7_CM5, 20))
    print('MAR CMIP6', 'LW_net:', np.round(poly7_CM6(TAS),2),'%','std: $\pm$',R_std(y7_CM6[117:137],x_CM6,coeff7_CM6, 20))

    
    
    
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


print('LWU: f(x)=',np.round(coeff_CM5[0],2),'x$^2$','+',np.round(coeff_CM5[1],2),'x','+',np.round(coeff_CM5[2],2))
print('LWU: f(x)=',np.round(coeff_CM6[0],3),'x$^2$','+',np.round(coeff_CM6[1],2),'x','+',np.round(coeff_CM6[2],2))

print('LWD: f(x)=',np.round(coeff2_CM5[0],2),'x$^2$','+',np.round(coeff2_CM5[1],2),'x','+',np.round(coeff2_CM5[2],2))
print('LWD: f(x)=',np.round(coeff2_CM6[0],3),'x$^2$','+',np.round(coeff2_CM6[1],2),'x','+',np.round(coeff2_CM6[2],2))

print('SWD: f(x)=',np.round(coeff3_CM5[0],2),'x$^2$','+',np.round(coeff3_CM5[1],2),'x','+',np.round(coeff3_CM5[2],2))
print('SWD: f(x)=',np.round(coeff3_CM6[0],3),'x$^2$','+',np.round(coeff3_CM6[1],2),'x','+',np.round(coeff3_CM6[2],2))

print('AL2: f(x)=',np.round(coeff4_CM5[0],2),'x$^2$','+',np.round(coeff4_CM5[1],2),'x','+',np.round(coeff4_CM5[2],2))
print('AL2: f(x)=',np.round(coeff4_CM6[0],3),'x$^2$','+',np.round(coeff4_CM6[1],2),'x','+',np.round(coeff4_CM6[2],2))

print('SW_net: f(x)=',np.round(coeff5_CM5[0],2),'x$^2$','+',np.round(coeff5_CM5[1],2),'x','+',np.round(coeff5_CM5[2],2))
print('SW_net: f(x)=',np.round(coeff5_CM6[0],3),'x$^2$','+',np.round(coeff5_CM6[1],2),'x','+',np.round(coeff5_CM6[2],2))

print('Net_r: f(x)=',np.round(coeff6_CM5[0],2),'x$^2$','+',np.round(coeff6_CM5[1],2),'x','+',np.round(coeff6_CM5[2],2))
print('Net_r: f(x)=',np.round(coeff6_CM6[0],3),'x$^2$','+',np.round(coeff6_CM6[1],2),'x','+',np.round(coeff6_CM6[2],2))

print('LW_net: f(x)=',np.round(coeff7_CM5[0],2),'x$^2$','+',np.round(coeff7_CM5[1],2),'x','+',np.round(coeff7_CM5[2],2))
print('LW_net: f(x)=',np.round(coeff7_CM6[0],3),'x$^2$','+',np.round(coeff7_CM6[1],2),'x','+',np.round(coeff7_CM6[2],2))


print('R2 - CMIP5')
print('LWU',R_square(x_CM5,y1_CM5,coeff_CM5))
print('LWD',R_square(x_CM5,y2_CM5,coeff2_CM5)) 
print('SWD',R_square(x_CM5,y3_CM5,coeff3_CM5))
print('AL2',R_square(x_CM5,y4_CM5,coeff4_CM5))
print('SW_net',R_square(x_CM5,y5_CM5,coeff5_CM5))
print('NET_rad_f',R_square(x_CM5,y6_CM5,coeff6_CM5))
print('LW_net',R_square(x_CM5,y7_CM5,coeff7_CM5))

print('R2 - CMIP6')
print('LWU',R_square(x_CM6,y1_CM6,coeff_CM6))
print('LWD',R_square(x_CM6,y2_CM6,coeff2_CM6)) 
print('SWD',R_square(x_CM6,y3_CM6,coeff3_CM6))
print('AL2',R_square(x_CM6,y4_CM6,coeff4_CM6))
print('SW_net',R_square(x_CM6,y5_CM6,coeff5_CM6))
print('NET_rad_f',R_square(x_CM6,y6_CM6,coeff6_CM6))
print('LW_net',R_square(x_CM6,y7_CM6,coeff7_CM6))

"""
JJA:

LWU 1.0
LWD 0.99
SWD 0.9
AL2 0.99
SW_net 0.93
NET_rad_f 0.99
LW_net 0.86
R2 - CMIP6
LWU 1.0
LWD 0.99
SWD 0.89
AL2 0.99
SW_net 0.95
NET_rad_f 0.99
LW_net 0.79

SON:

LWU 1.0
LWD 1.0
SWD 0.73
AL2 0.85
SW_net 0.15
NET_rad_f 0.83
LW_net 0.78
R2 - CMIP6
LWU 1.0
LWD 0.99
SWD 0.56
AL2 0.94
SW_net 0.54
NET_rad_f 0.62
LW_net 0.35


"""