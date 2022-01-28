"""
This code is used for plotting annual anomalies of radiative fluxes for the model mean of CMIP5 and CMIP6 models. 
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
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/ACCESS_anomaly_annual.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_annual.nc') 
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
    ALB_CM5     = CMIP5_models[i].AL2.mean(dim=["X10_105","Y21_199"])
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
    ALB_CM6     = CMIP6_models[i].AL2.mean(dim=["X10_105","Y21_199"])
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
"font.size":   22})


#== JOINT PLOT CM5 & CM6 ==
plt.figure(figsize= (10,10))
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 20)
plt.ylabel('Annual Surface energy flux anomalies [Wm$^{-2}$]', fontsize = 20)

color_CM5 = ['darkolivegreen', 'firebrick','indigo','darkorange', 'steelblue','dimgrey']
label_CM5 = ['LWU - CMIP5','LWD - CMIP5', 'SWD - CMIP5', 'SW$_{net}$- CMIP5','LW$_{net}$- CMIP5','Net radiative flux - CMIP5' ]
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=22, color = color_CM5[i])
    
plt.plot(curve_x_CM5, curve_y1_CM5, color ='darkolivegreen')  ### TEST
plt.plot(curve_x_CM5, curve_y2_CM5, color ='firebrick')  ### TEST
plt.plot(curve_x_CM5, curve_y3_CM5, color ='indigo')  ### TEST
plt.plot(curve_x_CM5, curve_y5_CM5, color ='darkorange')  ### TEST
plt.plot(curve_x_CM5, curve_y7_CM5, color ='steelblue')  ### LW_net
plt.plot(curve_x_CM5, curve_y6_CM5, color = 'dimgrey')

color_CM6 = ['yellowgreen','lightcoral','mediumpurple',  'sandybrown','lightskyblue','darkgrey']
label_CM6 = ['LWU - CMIP6','LWD - CMIP6', 'SWD - CMIP6', 'SW$_{net}$- CMIP6','LW$_{net}$- CMIP6', 'Net radiative flux - CMIP6' ]
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i] ,label = label_CM6[i], s=80, marker='+',color = color_CM6[i])
    
plt.plot(curve_x_CM6, curve_y1_CM6, '--', color ='yellowgreen')  ### TEST
plt.plot(curve_x_CM6, curve_y2_CM6, '--',color ='lightcoral')  ### TEST
plt.plot(curve_x_CM6, curve_y3_CM6, '--', color ='mediumpurple')  ### TEST
plt.plot(curve_x_CM6, curve_y5_CM6, '--', color ='sandybrown')  ### TEST
plt.plot(curve_x_CM6, curve_y7_CM6, '--', color ='lightskyblue')  ### LW_net
plt.plot(curve_x_CM6, curve_y6_CM6, '--', color = 'darkgrey')
plt.ylim(-40,40)

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
        cm5_dott = mlines.Line2D([11],[3], color='black', marker='o', markersize=7, label='MAR CMIP5')
        return [cm5_dott]

class AnyObjectHandler8(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm6_cross = mlines.Line2D([11],[3], color='black', marker='+', markersize=9, label='MAR CMIP6')
        return [cm6_cross]

object1 = HandlerBase()
object2 = HandlerBase()
object3 = HandlerBase()
object4 = HandlerBase()
object5 = HandlerBase()
object6 = HandlerBase()
object7 = HandlerBase()
object8 = HandlerBase()
    
plt.legend([object1,object2, object3, object4, object5, object6, object7, object8], ['LWU','LWD', 'SWD', 'SW$_{net}$','LW$_{net}$', 'Net radiative flux','MAR CMIP5','MAR CMIP6'],
           handler_map={object1: AnyObjectHandler(),
                        object2:AnyObjectHandler2(),
                        object3:AnyObjectHandler3(),
                        object4:AnyObjectHandler4(),
                        object5:AnyObjectHandler5(),
                        object6:AnyObjectHandler6(),
                        object7:AnyObjectHandler7(),
                        object8:AnyObjectHandler8()}, 
           fontsize=16,frameon=False,ncol=3, loc='upper left')
#-#-#-#-#-#-#-#-#-#-#-#-#-#


#Imports
import matplotlib.patches as mpatches


###sns.set_palette('colorblind')
sns.despine()
#plt.legend(ncol=2)
plt.show()
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/SEB_rad_flux_anomalies_jointCM5CM6_annual.pdf',bbox_inches='tight',dpi=300)


#==========================================================================================
#== ALBEDO ==
plt.figure(figsize=(10,10))
plt.scatter(TT_CMIP5, ALB_CMIP5, label= 'ALB - CMIP5', s=22, color='saddlebrown')

plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 20)
plt.ylabel('Annual Albedo anomalies', fontsize = 20)

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
           fontsize=16,frameon=False,ncol=1, loc='upper right')
    
####

plt.plot(curve_x_CM6, curve_y4_CM6, '--', color ='tan')  ### TEST


sns.set_palette('colorblind')
sns.despine()
plt.show()
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/Albedo_anomalies_JOINT_CMIP5_CMIP6_annual.pdf',bbox_inches='tight',dpi=300)
#==========================================================================================
#==========================================================================================

#Printing Specific values of SEB components for given near-surface temperature (TAS)
for TAS in range(1,6):
    print(season)
    print('TAS:', TAS)
    print('CMIP5', 'LWU:', np.round(poly1_CM5(TAS),2),
          'LWD:',np.round(poly2_CM5(TAS),2),
          'LW_net:', np.round(poly7_CM5(TAS),2),
          'SWD:',np.round(poly3_CM5(TAS),2),
          'SW_net:',np.round(poly5_CM5(TAS),2),
          'Net_rad_f:', np.round(poly6_CM5(TAS),2),
          'ALB:', np.round(poly4_CM5(TAS)*100,2))

    print('CMIP6', 'LWU:', np.round(poly1_CM6(TAS),2), 
          'LWD:',np.round(poly2_CM6(TAS),2),
          'LW_net:', np.round(poly7_CM6(TAS),2),
          'SWD:',np.round(poly3_CM6(TAS),2),
          'SW_net:',np.round(poly5_CM6(TAS),2),
          'Net_rad_f:', np.round(poly6_CM6(TAS),2),
          'ALB:', np.round(poly4_CM6(TAS)*100,2))
