####### TEST OF MULTI PLOT FOR ALL ##########
import xarray as xr
import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy
from latex_size import set_size


"""

#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/ACCESS_1_deg_anomalies.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies.nc')
#HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies_cloud.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CSIRO_1_deg_anomalies.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/IPSL_1_deg_anomalies.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/MIROC5_1_deg_anomalies.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/NORESM_1_deg_anomalies.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CESM_1_deg_anomalies.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CNRM_ESM2_1_deg_anomalies.nc')
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CNRM_CM6_1_deg_anomalies.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/MRI_1_deg_anomalies.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/UKMO_1_deg_anomalies.nc')
"""
season = input('Enter season [MAM,JJA,SON]:')
if season == 'MAM':
    TAS = 3
else:
    TAS = 4
    
#CMIP5 models
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
HADGEM_SMB_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_SMB_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')

ACCESS       = ACCESS_rol_4 
HADGEM       = HADGEM_rol_4 
HADGEM_cloud = HADGEM_cloud_rol_4
HADGEM_SMB   = HADGEM_SMB_rol_4 
CSIRO        = CSIRO_rol_4   
IPSL         = IPSL_rol_4   
MIROC5       = MIROC5_rol_4  
NORESM       = NORESM_rol_4  

#CMIP6 models
CESM      = CESM_rol_4       
CNRM_ESM2 = CNRM_ESM2_rol_4  
CNRM_CM6  = CNRM_CM6_rol_4   
MRI       = MRI_rol_4      
UKMO      = UKMO_rol_4 

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
LW_net_CMIP5 = []
SHF_CMIP5    = []
LHF_CMIP5    = []
NET_f_CMIP5  = []
NET_rad_f_CMIP5  = []
NET_non_rad_f_CMIP5 = []
ALB_CMIP5    = []

for i in range(len(CMIP5_models)):
    SWD_cmip5 = CMIP5_models[i].SWD
    SWD_CMIP5.append(SWD_cmip5)
    
    SW_net_cmip5 = CMIP5_models[i].SW_net
    SW_net_CMIP5.append(SW_net_cmip5)
    
    LWD_cmip5 = CMIP5_models[i].LWD
    LWD_CMIP5.append(LWD_cmip5)
    
    LW_net_cmip5 = CMIP5_models[i].LW_net
    LW_net_CMIP5.append(LW_net_cmip5)
    
    SHF_cmip5 = CMIP5_models[i].SHF
    SHF_CMIP5.append(SHF_cmip5)
    
    LHF_cmip5 = CMIP5_models[i].LHF
    LHF_CMIP5.append(LHF_cmip5)
    
    NET_f_cmip5 = CMIP5_models[i].NET_f
    NET_f_CMIP5.append(NET_f_cmip5)
    
    NET_rad_f_cmip5 = CMIP5_models[i].NET_rad_f
    NET_rad_f_CMIP5.append(NET_rad_f_cmip5)
    
    NET_non_rad_f_cmip5 = CMIP5_models[i].NET_non_rad_f
    NET_non_rad_f_CMIP5.append(NET_non_rad_f_cmip5)
    
    ALB_cmip5 = CMIP5_models[i].AL2
    ALB_CMIP5.append(ALB_cmip5)
    

    
SWD_CMIP5_model_mean = model_mean(SWD_CMIP5)
SW_net_CMIP5_model_mean = model_mean(SW_net_CMIP5)
LWD_CMIP5_model_mean = model_mean(LWD_CMIP5)
LW_net_CMIP5_model_mean = model_mean(LW_net_CMIP5)
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
LW_net_CMIP6 = []
SHF_CMIP6    = []
LHF_CMIP6    = []
NET_f_CMIP6  = []
NET_rad_f_CMIP6  = []
NET_non_rad_f_CMIP6 = []
ALB_CMIP6    = []

for i in range(len(CMIP6_models)):
    SWD_cmip6 = CMIP6_models[i].SWD
    SWD_CMIP6.append(SWD_cmip6)
    
    SW_net_cmip6 = CMIP6_models[i].SW_net
    SW_net_CMIP6.append(SW_net_cmip6)
    
    LWD_cmip6 = CMIP6_models[i].LWD
    LWD_CMIP6.append(LWD_cmip6)
    
    LW_net_cmip6 = CMIP6_models[i].LW_net
    LW_net_CMIP6.append(LW_net_cmip6)
    
    SHF_cmip6 = CMIP6_models[i].SHF
    SHF_CMIP6.append(SHF_cmip6)
    
    LHF_cmip6 = CMIP6_models[i].LHF
    LHF_CMIP6.append(LHF_cmip6)
    
    NET_f_cmip6 = CMIP6_models[i].NET_f
    NET_f_CMIP6.append(NET_f_cmip6)
    
    NET_rad_f_cmip6 = CMIP6_models[i].NET_rad_f
    NET_rad_f_CMIP6.append(NET_rad_f_cmip6)
    
    NET_non_rad_f_cmip6 = CMIP6_models[i].NET_non_rad_f
    NET_non_rad_f_CMIP6.append(NET_non_rad_f_cmip6)
    
    ALB_cmip6 = CMIP6_models[i].AL2
    ALB_CMIP6.append(ALB_cmip6)
    

    
SWD_CMIP6_model_mean = model_mean(SWD_CMIP6)
SW_net_CMIP6_model_mean = model_mean(SW_net_CMIP6)
LWD_CMIP6_model_mean = model_mean(LWD_CMIP6)
LW_net_CMIP6_model_mean = model_mean(LW_net_CMIP6)
SHF_CMIP6_model_mean = model_mean(SHF_CMIP6)
LHF_CMIP6_model_mean = model_mean(LHF_CMIP6)
NET_f_CMIP6_model_mean = model_mean(NET_f_CMIP6)
NET_rad_f_CMIP6_model_mean = model_mean(NET_rad_f_CMIP6)
NET_non_rad_f_CMIP6_model_mean = model_mean(NET_non_rad_f_CMIP6)
ALB_CMIP6_model_mean = model_mean(ALB_CMIP6)


SWD_diff = SWD_CMIP6_model_mean - SWD_CMIP5_model_mean
SW_net_diff = SW_net_CMIP6_model_mean - SW_net_CMIP5_model_mean
LWD_diff = LWD_CMIP6_model_mean - LWD_CMIP5_model_mean
LW_net_diff = LW_net_CMIP6_model_mean - LW_net_CMIP5_model_mean

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})


### ======= MULTIPLOT ======= ###
proj = ccrs.LambertConformal(central_longitude=-35,
                            central_latitude=65,
                            standard_parallels=[35])

fig, axes = plt.subplots( ncols=2, nrows=4, figsize=(10, 12), subplot_kw={'projection': proj})

ax = axes.ravel().tolist()


for i in [0,1,2,3,4,5,6,7]:
    ax[i].add_feature(cartopy.feature.OCEAN.with_scale(
        '50m'), zorder=1, facecolor='white')           
    ax[i].add_feature(cartopy.feature.COASTLINE.with_scale(
        '50m'), zorder=1, edgecolor='black')
    ax[i].set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())    


#divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
#divnorm=colors(vmin=vmin, vcenter=vcenter, vmax=vmax)
    
#CMIP5 model mean
cont = ax[0].pcolormesh(ds['LON'], ds['LAT'], LWD_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)
#CMIP6 model mean
cont2 = ax[1].pcolormesh(ds['LON'], ds['LAT'], LWD_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)

#CMIP6 model mean
cont4 = ax[2].pcolormesh(ds['LON'], ds['LAT'], SWD_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)

#CMIP5 model mean
cont = ax[3].pcolormesh(ds['LON'], ds['LAT'], SWD_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)

#CMIP5 model mean
cont3 = ax[4].pcolormesh(ds['LON'], ds['LAT'], LW_net_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)
#CMIP6 model mean
cont4 = ax[5].pcolormesh(ds['LON'], ds['LAT'], LW_net_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)

#CMIP5 model mean
cont3 = ax[6].pcolormesh(ds['LON'], ds['LAT'], SW_net_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)
#CMIP6 model mean
cont4 = ax[7].pcolormesh(ds['LON'], ds['LAT'], SW_net_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -30, vmax=30)





plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 20})

#Top title
title_top = [''+season+'']    
j = 0
for i in [0]:
    ax[i].set_title(title_top[j], fontsize=20)
    j += 1
    
# Left side title
title_left = ['LWD', 'SWD', 'LW$_{net}$', 'SW$_{net}$']    
j = 0
for i in [0, 2, 4, 6]:
    ax[i].text(-0.5, 0.5, title_left[j], transform=ax[i].transAxes,fontsize=20, fontweight="bold")
    j += 1
    
    
#remove outer box of the plot 
fig.patch.set_visible(False)
ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')
ax[4].axis('off')
ax[5].axis('off')
ax[6].axis('off')
ax[7].axis('off')


fig.canvas.draw()
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
    

plt.subplots_adjust(left=0.2, right=0.98, top=0.97, bottom=0.24)
cbar = fig.colorbar(cont2, ax=ax, shrink=0.7, orientation ='vertical')
cbar.set_label('Seasonal('+season+') Surf. energy flux amonalies [Wm$^{-2}$]', fontsize=14)

#plt.suptitle(suptitle, fontsize = 16, y=0.95, x=0.40)
plt.show()
    
#if savefig == True:
#fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/1_deg_spatial_plots/energy_multiplot.png')
fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/'+str(TAS)+'_'+season+'_energy_multiplot.png')



### ======= MULTIPLOT ======= ###
proj = ccrs.LambertConformal(central_longitude=-35,
                            central_latitude=65,
                            standard_parallels=[35])

fig, axes = plt.subplots( ncols=1, nrows=4, figsize=(10,12), subplot_kw={'projection': proj})

ax = axes.ravel().tolist()


for i in [0,1,2,3]:
    ax[i].add_feature(cartopy.feature.OCEAN.with_scale(
        '50m'), zorder=1, facecolor='white')           
    ax[i].add_feature(cartopy.feature.COASTLINE.with_scale(
        '50m'), zorder=1, edgecolor='black')
    ax[i].set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())    


#divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
#divnorm=colors(vmin=vmin, vcenter=vcenter, vmax=vmax)
if season == 'JJA':
    vmin = -10

else:
    vmin = -4

if season =='JJA':    
    vmax = 10
else:
    vmax = 4

cont3 = ax[0].pcolormesh(ds['LON'], ds['LAT'], LWD_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= vmin, vmax=vmax)
cont2 = ax[1].pcolormesh(ds['LON'], ds['LAT'], SWD_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= vmin, vmax=vmax)

cont = ax[2].pcolormesh(ds['LON'], ds['LAT'], LW_net_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= vmin, vmax=vmax)

cont4 = ax[3].pcolormesh(ds['LON'], ds['LAT'], SW_net_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= vmin, vmax=vmax)




plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"], 
"font.size": 20})

#Top title
title_top = [''+season+'']    
j = 0
for i in [0]:
    ax[i].set_title(title_top[j], fontsize=20)
    j += 1
    
    
    
#remove outer box of the plot 
fig.patch.set_visible(False)
ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')


fig.canvas.draw()
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
    

plt.subplots_adjust(left=0.2, right=0.98, top=0.93, bottom=0.20)
cbar = fig.colorbar(cont2, ax=ax, shrink=0.75, orientation ='vertical')
#cbar.set_label('(CMIP6-CMIP5) Surf. energy flux amonalies [Wm$^{-2}$]', fontsize=20)

# Left side title
title_left = ['LWD', 'SWD', 'LW$_{net}$', 'SW$_{net}$']    
j = 0
for i in [0, 1, 2, 3]:
    ax[i].text(-0.75, 0.5, title_left[j], transform=ax[i].transAxes,fontsize=20, fontweight="extra bold")
    j += 1

plt.show()
    
#if savefig == True:
#fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/1_deg_spatial_plots/diff_multiplot.png')
fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/'+str(TAS)+'_'+season+'_diff_multiplot.pdf',bbox_inches='tight',dpi=300)