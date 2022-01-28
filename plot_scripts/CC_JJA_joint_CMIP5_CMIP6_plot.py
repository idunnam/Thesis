"""
This code is used for plotting Model mean Cloud Cover for seasonal (JJA) anomalies, 
with reference period 1961-1990, from monthly MAR output data of 6 CMIP5 models and 5 CMIP6 models. 
"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import seaborn as sns
import pandas as pd

#=== Import SEB Anomalies ====
#from seasonal_SEB_components import * 
season = input('Enter season [MAM,JJA,SON]:')

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
"""

#ANNUAL
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



#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod) 


CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

TT_CMIP5  = []
CC_CMIP5  = []



for i in range(len(CMIP5_models)):
    TT_CM5  = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    CC_CM5 = CMIP5_models[i].CC.mean(dim=["X10_105","Y21_199"])*100 
   

    TT_CMIP5.append(TT_CM5)
    CC_CMIP5.append(CC_CM5)
    
    
TT_CMIP5    = model_mean(TT_CMIP5)
CC_CMIP5    = model_mean(CC_CMIP5)

SEB_var_CMIP5 = [CC_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
CC_CMIP6    = []


for i in range(len(CMIP6_models)):
    TT_CM6  = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    CC_CM6 = CMIP6_models[i].CC.mean(dim=["X10_105","Y21_199"])*100 
    
    TT_CMIP6.append(TT_CM6)
    CC_CMIP6.append(CC_CM6)
      
    
TT_CMIP6     = model_mean(TT_CMIP6)
CC_CMIP6    = model_mean(CC_CMIP6)

    
SEB_var_CMIP6 = [CC_CMIP6]

SEB_var_label = ['CC']


#===== Fit a Regression line ========

### TEST NY METODE FOR REGRESSION KURVE###
TAS_CM5 = TT_CMIP5.to_dataframe()
CC_CM5 = CC_CMIP5.to_dataframe()

TAS_CM6 = TT_CMIP6.to_dataframe()
CC_CM6 = CC_CMIP6.to_dataframe()

    
### CMIP5 ###
x_CM5  = TAS_CM5['TT']
y_CM5 = CC_CM5['CC']


coeff_CM5 = np.polyfit(x_CM5, y_CM5,2)
poly1_CM5 = np.poly1d(coeff_CM5)



t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y_CM5 = poly1_CM5(curve_x_CM5)



### CMIP6 ###
x_CM6  = TAS_CM6['TT']
y_CM6 = CC_CM6['CC']

coeff_CM6 = np.polyfit(x_CM6, y_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)

t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y_CM6 = poly1_CM6(curve_x_CM6)

#=== PLOT ===

    
#plt.figure(figsize=(10,10))
plt.figure(figsize=(6.4,6.4))
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= 'CC - CMIP5', s=17, color= 'darkblue', alpha=0.8)

plt.plot(curve_x_CM5, curve_y_CM5, color = 'darkblue',linewidth=1.5)  ### TEST
#plt.title('('+season+') Cloud Cover anomalies \n Model Mean of MAR CMIP5 vs. MAR CMIP6 simulations', fontsize = 24)
plt.title(season, fontsize=20)
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 20)
plt.ylabel('Cloud Cover anomalies [$\%$]', fontsize = 20)
#plt.ylabel('Annual Cloud Cover anomalies [$\%$]', fontsize = 20)
plt.ylim(-5,5)
plt.xlim(-1,8.5)
plt.legend(loc='upper left')

for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i], label = 'CC - CMIP6', s=60, marker = '+', color='royalblue', linewidth=0.8)


plt.plot(curve_x_CM6, curve_y_CM6, '--', color='royalblue', linewidth=1.5)  ### TEST
#plt.legend(loc='upper left')

#-#-#- FANCY LEGEND -#-#-#
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase

class AnyObjectHandler1(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        CC_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='darkblue')
        CC_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='royalblue')
        return [CC_cm5, CC_cm6]
    
class AnyObjectHandler2(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm5_dott = mlines.Line2D([11],[3], color='black', marker='o', markersize=7, label='MAR CMIP5')
        return [cm5_dott]
    
class AnyObjectHandler3(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        cm6_cross = mlines.Line2D([11],[3], color='black', marker='+', markersize=9, label='MAR CMIP6')
        return [cm6_cross]
object1 = HandlerBase()
object2 = HandlerBase()
object3 = HandlerBase()

#"""    
plt.legend([object1,object2, object3], ['CC', 'MAR CMIP5','MAR CMIP6'],
           handler_map={object1: AnyObjectHandler1(),
                        object2:AnyObjectHandler2(),
                        object3:AnyObjectHandler3()}, 
           fontsize=11,frameon=False, loc='lower left')
#"""           
#-#-#-#-#-#-#-#-#-#-#-#-#-#

sns.set_palette('colorblind')
sns.despine()
plt.show()
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/Cloud_components/CC_anomalies_CMIP5_CMIP6_'+season+'.pdf',bbox_inches='tight',dpi=300)

#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/Cloud_components/CC_anomalies_CMIP5_CMIP6_annual.pdf',bbox_inches='tight',dpi=300)


#def stand_dev(x,y,coeff):
    #use y = y_CM5, x= x_CM5, coeff = coeff_CM5
    #use y = y_CM6, x= x_CM6, coeff = coeff_CM6
#    c = y - (coeff[0]*x**2 + coeff[1]*x + coeff[2])
#    return c

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
    print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y_CM6[126:146],x_CM6,coeff_CM6, 20))
    
      
if season=='SON':
    TAS=6.7
    
    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    #print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y_CM5,coeff_CM5)),2))
    #print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y_CM6,coeff_CM6)),2))
    print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y_CM6[117:137],x_CM6,coeff_CM6, 20))
   
    

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
    return np.round(R_square,4)


print('CMIP5 R2: CC',R_square(x_CM5,y_CM5,coeff_CM5))
print('CMIP5 R2: CC',R_square(x_CM6,y_CM6,coeff_CM6))


print('f(x)=',np.round(coeff_CM5[0],4),'x$^2$','+',np.round(coeff_CM5[1],4),'x','+',np.round(coeff_CM5[2],4))
print('f(x)=',np.round(coeff_CM6[0],4),'x$^2$','+',np.round(coeff_CM6[1],4),'x','+',np.round(coeff_CM6[2],4))

        