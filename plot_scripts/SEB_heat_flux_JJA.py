"""
This code is used for plotting seasonal (JJA) anomalies of heat fluxes for the model mean of CMIP5 and CMIP6 models. 
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd

#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
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

label_CM5 = ['LHF - CMIP5','SHF - CMIP5']
label_CM6 = ['LHF - CMIP6','SHF - CMIP6']
color_CM5 = ['darkgoldenrod','navy']
color_CM6 = ['gold','cornflowerblue']

#========== ALTERNATIVE JOINT PLOTTING ====================
#==========================================================
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 12})

px = px = 1/plt.rcParams['figure.dpi']
plt.figurefigsize=(306*px,306*px)
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= label_CM5[i], s=22, color = color_CM5[i])
    
for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i], label = label_CM6[i], s=80, marker = '+', color= color_CM6[i])
    
#-#-#- FANCY LEGEND -#-#-#
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase


class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        SHF_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='navy')
        SHF_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='cornflowerblue')
        return [SHF_cm5, SHF_cm6]
    
class AnyObjectHandler2(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        LHF_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='darkgoldenrod')
        LHF_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='gold')
        return [LHF_cm5, LHF_cm6]


class AnyObjectHandler3(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm5_dott = mlines.Line2D([11],[3], color='black', marker='o', markersize=7, label='MAR CMIP5')
        return [cm5_dott]

class AnyObjectHandler4(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm6_cross = mlines.Line2D([11],[3], color='black', marker='+', markersize=9, label='MAR CMIP6')
        return [cm6_cross]

object1 = HandlerBase()
object2 = HandlerBase()
object3 = HandlerBase()
object4 = HandlerBase()

    
plt.legend([object1,object2, object3, object4], ['SHF','LHF', 'MAR CMIP5','MAR CMIP6'],
           handler_map={object1: AnyObjectHandler(),
                        object2:AnyObjectHandler2(),
                        object3:AnyObjectHandler3(),
                        object4:AnyObjectHandler4(),
                       }, 
           fontsize=8,frameon=False,ncol=2, loc='upper left')
#-#-#-#-#-#-#-#-#-#-#-#-#-#


plt.plot(curve_x_CM5, curve_y1_CM5,color = 'darkgoldenrod')  ### TEST
plt.plot(curve_x_CM5, curve_y2_CM5,color = 'navy')  ### TEST
plt.plot(curve_x_CM6, curve_y1_CM6, '--',color = 'gold')  ### TEST
plt.plot(curve_x_CM6, curve_y2_CM6, '--',color = 'cornflowerblue')  ### TEST
#plt.title('('+season+')) Surface Heat flux component anomalies \n Model Mean of CMIP5 vs. CMIP6 MAR simulations', fontsize = 16)
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 12)
plt.ylabel('('+season+')Heat flux anomalies [Wm-2]', fontsize = 12)
#plt.legend(loc='upper left', ncol=2)

sns.despine()
plt.show()
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/SEB_components/SEB_heat_flux_JOINT_CMIP5_CMIP6_'+season+'.pdf',bbox_inches='tight',dpi=300)


#==========================================================
#==========================================================


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
    print('MAR CMIP5', 'LHF:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y1_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'LHF:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y1_CM6[126:146],x_CM6,coeff_CM6, 20))
    print('MAR CMIP5', 'SHF:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y2_CM5[-20:],x_CM5[-20:],coeff2_CM5, 20))
    print('MAR CMIP6', 'SHF:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y2_CM6[126:146],x_CM6,coeff2_CM6, 20))
    
    
      
if season=='SON':
    TAS=6.7
    
    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    #print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y_CM5,coeff_CM5)),2))
    #print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y_CM6,coeff_CM6)),2))
    print('MAR CMIP5', 'LHF:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y1_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'LHF:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y1_CM6[117:137],x_CM6,coeff_CM6, 20))
    print('MAR CMIP5', 'SHF:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y2_CM5[-20:],x_CM5[-20:],coeff2_CM5, 20))
    print('MAR CMIP6', 'SHF:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y2_CM6[117:137],x_CM6,coeff2_CM6, 20))


#OUTPUT FROM TERMINAL
"""
Season: JJA
TAS: 5.4
MAR CMIP5 LHF: 4.93 Wm-2 std: $\pm$ 1.46
RANGE CMIP5: [ 6.39 , 3.46 ]
MAR CMIP6 LHF: 4.85 Wm-2 std: $\pm$ 1.43
RANGE CMIP6: [ 6.32 , 3.43 ]
TAS: 5.4
MAR CMIP5 SHF: 2.11 Wm-2 std: $\pm$ 0.05
RANGE CMIP5: [ 2.16 , 2.05 ]
MAR CMIP6 SHF: 2.43 Wm-2 std: $\pm$ 0.22
RANGE CMIP6: [ 2.49 , 2.22 ]


Season: SON
TAS: 6.7
MAR CMIP5 LHF: 1.19 Wm-2 std: $\pm$ 0.41
RANGE CMIP5: [ 1.59 , 0.78 ]
MAR CMIP6 LHF: 1.7 Wm-2 std: $\pm$ 0.15
RANGE CMIP6: [ 2.11 , 1.55 ]
TAS: 6.7
MAR CMIP5 SHF: -3.45 Wm-2 std: $\pm$ 2.72
RANGE CMIP5: [ -0.72 , -6.17 ]
MAR CMIP6 SHF: -2.61 Wm-2 std: $\pm$ 2.31
RANGE CMIP6: [ 0.11 , 


TAS: 1
CMIP5 LHF: 0.4617 SHF: -0.1874
CMIP6 LHF: 0.4234 SHF: -0.1127

TAS: 2
CMIP5 LHF: 1.1276 SHF: -0.1545
CMIP6 LHF: 1.064  SHF: -0.0866

TAS: 3
CMIP5 LHF: 1.9987 SHF: 0.166
CMIP6 LHF: 1.9202 SHF: 0.2647

TAS: 4
CMIP5 LHF: 3.0749 SHF: 0.7742
CMIP6 LHF: 2.992 SHF: 0.941

TAS: 5
CMIP5 LHF: 4.3562 SHF: 1.6701
CMIP6 LHF: 4.2793 SHF: 1.9425
"""


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
print('LHF',R_square(x_CM5,y1_CM5,coeff_CM5))
print('SHF',R_square(x_CM5,y2_CM5,coeff2_CM5)) 


print('R2 - CMIP6')
print('LHF',R_square(x_CM6,y1_CM6,coeff_CM6))
print('SHF',R_square(x_CM6,y2_CM6,coeff2_CM6)) 


print('LHF: f(x)=',np.round(coeff_CM5[0],2),'x$^2$','+',np.round(coeff_CM5[1],2),'x','+',np.round(coeff_CM5[2],2))
print('LHF: f(x)=',np.round(coeff_CM6[0],3),'x$^2$','+',np.round(coeff_CM6[1],2),'x','+',np.round(coeff_CM6[2],2))

print('SHF: f(x)=',np.round(coeff2_CM5[0],2),'x$^2$','+',np.round(coeff2_CM5[1],2),'x','+',np.round(coeff2_CM5[2],2))
print('SHF: f(x)=',np.round(coeff2_CM6[0],3),'x$^2$','+',np.round(coeff2_CM6[1],2),'x','+',np.round(coeff2_CM6[2],2))

