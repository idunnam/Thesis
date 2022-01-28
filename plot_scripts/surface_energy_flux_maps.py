"""
Surface energy fluxes over the Greenland ice sheet for a mean warming of one degree (TAS[4,5]) 
"""
import xarray as xr             # to work with netCDF fils
from function_10 import test_plot


#import data 
#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/ACCESS_anomaly_ablation_JJA.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/HADGEM_anomaly_ablation_JJA.nc')
#HADGEM_cloud= xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/HADGEM_anomaly_ablation_JJA_cloud.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/CSIRO_anomaly_ablation_JJA.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/IPSL_anomaly_ablation_JJA.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/MIROC5_anomaly_ablation_JJA.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/NORESM_anomaly_ablation_JJA.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/CESM_anomaly_ablation_JJA.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/CNRM_ESM2_anomaly_ablation_JJA.nc')
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/CNRM_CM6_anomaly_ablation_JJA.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/MRI_anomaly_ablation_JJA.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/ablation_JJA/UKMO_anomaly_ablation_JJA.nc')
#"""

#pick the years for each model where the overall mean temperature increases from tas=4-5 degrees
ACCESS = ACCESS.sel(year = [2060, 2075, 2076, 2082, 2083, 2085, 2088, 2090, 2091, 2093, 2097, 2098, 2099])
HADGEM = HADGEM.sel(year = [2057, 2059, 2062, 2064, 2068, 2070, 2072, 2074, 2075, 2076, 2077, 2082, 2083, 2087, 2088])
CSIRO  = CSIRO.sel(year = [2073, 2078, 2079, 2083, 2088, 2093, 2096]) 
IPSL   = IPSL.sel(year = [2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2069, 2070, 2071, 2072, 2073, 2074, 2079, 2080, 2082, 2086, 2089, 2095])
MIROC5 = MIROC5.sel(year = [2056, 2060, 2065, 2066, 2067, 2073, 2076, 2078, 2079, 2081, 2084, 2090])
NORESM = NORESM.sel(year = [2078, 2081, 2083, 2085, 2089, 2092, 2095])

#CMIP6
CESM      = CESM.sel(year = [2033, 2044, 2046, 2054, 2055, 2058, 2061, 2063, 2067, 2068, 2070, 2071, 2072, 2073, 2074, 2080])
CNRM_CM6  = CNRM_CM6.sel(year = [2059, 2066, 2068, 2073, 2074, 2076, 2077, 2078, 2079, 2080, 2086])
CNRM_ESM2 = CNRM_ESM2.sel(year = [2066, 2073, 2074, 2090])
MRI       = MRI.sel(year = [2053, 2060, 2063, 2067, 2068, 2071, 2072, 2075, 2076, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2090, 2092, 2093, 2095, 2098])       
UKMO      = UKMO.sel(year = [2038, 2039, 2040, 2041, 2043, 2047, 2048, 2049, 2050, 2055, 2056, 2057] )

#"""


#dataset for choosing coordinates
ds = xr.open_dataset('/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/MARv3.9-ACCESS13-2074.nc', decode_times=False)

# === Calculate the model mean of each variable ==#

#Function for calculating the model mean 
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

SWD_CMIP5    = [] 
SW_net_CMIP5 = []
LWD_CMIP5    = []
SHF_CMIP5    = []
LHF_CMIP5    = []
NET_f_CMIP5  = []
NET_rad_f_CMIP5  = []
NET_non_rad_f_CMIP5 = []
ALB_CMIP5    = []

for i in range(len(CMIP5_models)):
    SWD_cmip5 = CMIP5_models[i].SWD.mean(dim='year')
    SWD_CMIP5.append(SWD_cmip5)
    
    SW_net_cmip5 = CMIP5_models[i].SW_net.mean(dim='year')
    SW_net_CMIP5.append(SW_net_cmip5)
    
    LWD_cmip5 = CMIP5_models[i].LWD.mean(dim='year')
    LWD_CMIP5.append(LWD_cmip5)
    
    SHF_cmip5 = CMIP5_models[i].SHF.mean(dim='year')
    SHF_CMIP5.append(SHF_cmip5)
    
    LHF_cmip5 = CMIP5_models[i].LHF.mean(dim='year')
    LHF_CMIP5.append(LHF_cmip5)
    
    NET_f_cmip5 = CMIP5_models[i].NET_f.mean(dim='year')
    NET_f_CMIP5.append(NET_f_cmip5)
    
    NET_rad_f_cmip5 = CMIP5_models[i].NET_rad_f.mean(dim='year')
    NET_rad_f_CMIP5.append(NET_rad_f_cmip5)
    
    NET_non_rad_f_cmip5 = CMIP5_models[i].NET_non_rad_f.mean(dim='year')
    NET_non_rad_f_CMIP5.append(NET_non_rad_f_cmip5)
    
    ALB_cmip5 = CMIP5_models[i].AL2.mean(dim='year')
    ALB_CMIP5.append(ALB_cmip5)
    

    
SWD_CMIP5_model_mean = model_mean(SWD_CMIP5)
SW_net_CMIP5_model_mean = model_mean(SW_net_CMIP5)
LWD_CMIP5_model_mean = model_mean(LWD_CMIP5)
SHF_CMIP5_model_mean = model_mean(SHF_CMIP5)
LHF_CMIP5_model_mean = model_mean(LHF_CMIP5)
NET_f_CMIP5_model_mean = model_mean(NET_f_CMIP5)
NET_rad_f_CMIP5_model_mean = model_mean(NET_rad_f_CMIP5)
NET_non_rad_f_CMIP5_model_mean = model_mean(NET_non_rad_f_CMIP5)
ALB_CMIP5_model_mean = model_mean(ALB_CMIP5)

#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

SWD_CMIP6    = [] 
SW_net_CMIP6 = []
LWD_CMIP6    = []
SHF_CMIP6    = []
LHF_CMIP6    = []
NET_f_CMIP6  = []
NET_rad_f_CMIP6  = []
NET_non_rad_f_CMIP6 = []
ALB_CMIP6    = []

for i in range(len(CMIP6_models)):
    SWD_cmip6 = CMIP6_models[i].SWD.mean(dim='year')
    SWD_CMIP6.append(SWD_cmip6)
    
    SW_net_cmip6 = CMIP6_models[i].SW_net.mean(dim='year')
    SW_net_CMIP6.append(SW_net_cmip6)
    
    LWD_cmip6 = CMIP6_models[i].LWD.mean(dim='year')
    LWD_CMIP6.append(LWD_cmip6)
    
    SHF_cmip6 = CMIP6_models[i].SHF.mean(dim='year')
    SHF_CMIP6.append(SHF_cmip6)
    
    LHF_cmip6 = CMIP6_models[i].LHF.mean(dim='year')
    LHF_CMIP6.append(LHF_cmip6)
    
    NET_f_cmip6 = CMIP6_models[i].NET_f.mean(dim='year')
    NET_f_CMIP6.append(NET_f_cmip6)
    
    NET_rad_f_cmip6 = CMIP6_models[i].NET_rad_f.mean(dim='year')
    NET_rad_f_CMIP6.append(NET_rad_f_cmip6)
    
    NET_non_rad_f_cmip6 = CMIP6_models[i].NET_non_rad_f.mean(dim='year')
    NET_non_rad_f_CMIP6.append(NET_non_rad_f_cmip6)
    
    ALB_cmip6 = CMIP6_models[i].AL2.mean(dim='year')
    ALB_CMIP6.append(ALB_cmip6)
    

    
SWD_CMIP6_model_mean = model_mean(SWD_CMIP6)
SW_net_CMIP6_model_mean = model_mean(SW_net_CMIP6)
LWD_CMIP6_model_mean = model_mean(LWD_CMIP6)
SHF_CMIP6_model_mean = model_mean(SHF_CMIP6)
LHF_CMIP6_model_mean = model_mean(LHF_CMIP6)
NET_f_CMIP6_model_mean = model_mean(NET_f_CMIP6)
NET_rad_f_CMIP6_model_mean = model_mean(NET_rad_f_CMIP6)
NET_non_rad_f_CMIP6_model_mean = model_mean(NET_non_rad_f_CMIP6)
ALB_CMIP6_model_mean = model_mean(ALB_CMIP6)

test_plot(NET_rad_f_CMIP5_model_mean, NET_rad_f_CMIP6_model_mean, ds['LON'], ds['LAT'], 0, 50,  'CMIP5 model mean','CMIP6 model mean',16,  'Net radiative flux anomalies', 'Reds',True,'HELLO.png' )

"""

def test_plot(var_left, var_right, lon, lat, vmin, vmax, 
              title_fig_l = 'left figure',  
              title_fig_r = 'right figure',
              fontsize_title_fig = 16,
              cbar_title = None , cmap_color = 'RdBu_r', 
              savefig = True, file_title = None):
            
"""

import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy



#calculate the total cloud cover difference 
diff_net_rad = NET_rad_f_CMIP6_model_mean - NET_rad_f_CMIP5_model_mean

proj = ccrs.LambertConformal(central_longitude=-35,
                             central_latitude=65,
                             standard_parallels=[35])
fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'projection': proj})

divnorm=colors.TwoSlopeNorm(vmin=-8, vcenter=0., vmax=8) 

ax.add_feature(cartopy.feature.OCEAN.with_scale(
                '50m'), zorder=1, facecolor='white')           
ax.add_feature(cartopy.feature.COASTLINE.with_scale(
                '50m'), zorder=1, edgecolor='black')
ax.set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())
    
cont = ax.pcolormesh(ds['LON'], ds['LAT'], diff_net_rad.values,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', norm=divnorm)
#remove outer box of the plot 
fig.patch.set_visible(False)
ax.axis('off')


fig.canvas.draw()
fig.tight_layout(pad=0.01)

plt.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.24)
cbar = fig.colorbar(cont, ax=ax, shrink=0.96, orientation ='vertical')
cbar.set_label(
    '(CMIP6 - CMIP5) Net radiative flux [Wm-2]', fontsize=14)
fig.savefig('HELLO_diff.png')