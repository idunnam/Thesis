"""
This code is used for plotting seasonal (JJA) anomalies of COD, with reference period from 1961-1990, as model mean for CMIP5 models and CMIP6 models. 
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

TT_CMIP5     = []
COD_CMIP5    = []



for i in range(len(CMIP5_models)):
    TT_CM5  = CMIP5_models[i].TT.mean(dim=["X10_105","Y21_199"])
    COD_CM5 = CMIP5_models[i].COD.mean(dim=["X10_105","Y21_199"]) 
   

    TT_CMIP5.append(TT_CM5)
    COD_CMIP5.append(COD_CM5)    
    
TT_CMIP5     = model_mean(TT_CMIP5)
COD_CMIP5    = model_mean(COD_CMIP5)

SEB_var_CMIP5 = [COD_CMIP5]

#=== CMIP6 component model mean ===
CMIP6_models = [CESM, CNRM_CM6, CNRM_ESM2, MRI, UKMO]

TT_CMIP6     = []
COD_CMIP6    = []

for i in range(len(CMIP6_models)):
    TT_CM6  = CMIP6_models[i].TT.mean(dim=["X10_105","Y21_199"])
    COD_CM6 = CMIP6_models[i].COD.mean(dim=["X10_105","Y21_199"]) 
    
    TT_CMIP6.append(TT_CM6)
    COD_CMIP6.append(COD_CM6)
      
    
TT_CMIP6     = model_mean(TT_CMIP6)
COD_CMIP6    = model_mean(COD_CMIP6)

    
SEB_var_CMIP6 = [COD_CMIP6]
SEB_var_label = ['COD']

#===== Fit a Regression line ========

### TEST NY METODE FOR REGRESSION KURVE###
TAS_CM5 = TT_CMIP5.to_dataframe()
COD_CM5 = COD_CMIP5.to_dataframe()

TAS_CM6 = TT_CMIP6.to_dataframe()
COD_CM6 = COD_CMIP6.to_dataframe()

    
### CMIP5 ###
x_CM5  = TAS_CM5['TT']
y_CM5 = COD_CM5['COD']


coeff_CM5 = np.polyfit(x_CM5, y_CM5,2)
poly1_CM5 = np.poly1d(coeff_CM5)


t = np.sort(TT_CMIP5)
curve_x_CM5 = np.linspace(t[0], t[-1])
curve_y_CM5 = poly1_CM5(curve_x_CM5)


### CMIP6 ###
x_CM6  = TAS_CM6['TT']
y_CM6 = COD_CM6['COD']

coeff_CM6 = np.polyfit(x_CM6, y_CM6,2)
poly1_CM6 = np.poly1d(coeff_CM6)

t = np.sort(TT_CMIP6)
curve_x_CM6 = np.linspace(t[0], t[-1])
curve_y_CM6 = poly1_CM6(curve_x_CM6)

#=== PLOT ===  
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 30})

plt.figure(figsize=(10,10))
for i in range(len(SEB_var_CMIP5)):
    plt.scatter(TT_CMIP5, SEB_var_CMIP5[i], label= 'COD - CMIP5', s=22, color= 'darkslategrey')

plt.plot(curve_x_CM5, curve_y_CM5, color = 'darkslategrey')  ### TEST
plt.xlabel('Near-surface Temperature anomalies [$^\circ$C]', fontsize = 37)
#plt.ylabel('Cloud Optical Depth anomalies', fontsize = 37)
#plt.ylabel('Annual Cloud Optical Depth anomalies', fontsize = 20)
plt.legend(loc='upper left')

for i in range(len(SEB_var_CMIP6)):
    plt.scatter(TT_CMIP6, SEB_var_CMIP6[i], label = 'COD - CMIP6', s=80, marker = '+', color='lightseagreen')
    
    
#-#-#- FANCY LEGEND -#-#-#
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerBase

class AnyObjectHandler1(HandlerBase):  
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        COD_cm5 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height], 
                                                 color='darkslategrey')
        COD_cm6 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], linestyle='--', color='lightseagreen')
        return [COD_cm5, COD_cm6]
    
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
    
plt.legend([object1,object2, object3], ['COD', 'MAR CMIP5','MAR CMIP6'],
           handler_map={object1: AnyObjectHandler1(),
                        object2:AnyObjectHandler2(),
                        object3:AnyObjectHandler3()}, 
           fontsize=16,frameon=False, loc='upper left')
#-#-#-#-#-#-#-#-#-#-#-#-#-#    


plt.plot(curve_x_CM6, curve_y_CM6, '--', color='lightseagreen')  ### TEST
plt.ylim(-0.1,0.5)
plt.xlim(-1,8.5)
sns.set_palette('colorblind')
sns.despine()
plt.show()
plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/Cloud_components/COD_anomalies_CMIP5_CMIP6_'+season+'.pdf',bbox_inches='tight',dpi=300 )
#plt.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/Cloud_components/COD_anomalies_CMIP5_CMIP6_annual.pdf',bbox_inches='tight',dpi=300 )


TAS = 5
print('TAS:', TAS)
print('CMIP5', 'COD:', np.round(poly1_CM5(TAS),4))
print('CMIP6', 'COD:', np.round(poly1_CM6(TAS),4))


#OUTPUT FROM TERMINAL
"""
TAS: 1
CMIP5 COD: 0.0267
CMIP6 COD: 0.0249

TAS: 2
CMIP5 COD: 0.0656
CMIP6 COD: 0.0622

TAS: 3
CMIP5 COD: 0.1163
CMIP6 COD: 0.1127

TAS: 4
CMIP5 COD: 0.1788
CMIP6 COD: 0.1766

TAS: 5
CMIP5 COD: 0.2532
CMIP6 COD: 0.2536
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


print('COD: f(x)=',np.round(coeff_CM5[0],4),'x$^2$','+',np.round(coeff_CM5[1],4),'x','+',np.round(coeff_CM5[2],4))
print('COD: f(x)=',np.round(coeff_CM6[0],4),'x$^2$','+',np.round(coeff_CM6[1],4),'x','+',np.round(coeff_CM6[2],4))


print('R2 - CMIP5')
print('COD',R_square(x_CM5,y_CM5,coeff_CM5))

print('R2 - CMIP6')
print('COD',R_square(x_CM6,y_CM6,coeff_CM6))

"""

R2 - CMIP5
COD 0.99
R2 - CMIP6
COD 0.98
"""

#def stand_dev(x,y,coeff):
    #use y = y_CM5, x= x_CM5, coeff = coeff_CM5
    #use y = y_CM6, x= x_CM6, coeff = coeff_CM6
#    c = y - (coeff[0]*(x**2) + coeff[1]*x + coeff[2])
#    return c

#if season =='JJA':
#    TAS=5.4
#if season=='SON':
#    TAS=6.7
#for TAS in range(1,6):
#print('Season:',season)
#print('TAS:', TAS)
#print('MAR CMIP5', 'COD:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.std(stand_dev(x_CM5,y_CM5,coeff_CM5)[-20:]))
#print('MAR CMIP6', 'COD:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.std(stand_dev(x_CM6,y_CM6,coeff_CM6)[-20:])) 

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
    print('MAR CMIP5', 'COD:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'COD:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y_CM6[126:146],x_CM6,coeff_CM6, 20))
    
      
if season=='SON':
    TAS=6.7
    
    #for TAS in range(1,6):
    print('Season:',season)
    print('TAS:', TAS)
    #print('MAR CMIP5', 'CC:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM5,y_CM5,coeff_CM5)),2))
    #print('MAR CMIP6', 'CC:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$', np.round(np.std(stand_dev(x_CM6,y_CM6,coeff_CM6)),2))
    print('MAR CMIP5', 'COD:', np.round(poly1_CM5(TAS),2),'%','std: $\pm$',R_std(y_CM5[-20:],x_CM5[-20:],coeff_CM5, 20))
    print('MAR CMIP6', 'COD:', np.round(poly1_CM6(TAS),2),'%','std: $\pm$',R_std(y_CM6[117:137],x_CM6,coeff_CM6, 20))