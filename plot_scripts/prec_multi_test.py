import xarray as xr
import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy
from latex_size import set_size # function for figursizing 
ds = xr.open_dataset('/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/MARv3.9-ACCESS13-2074.nc', decode_times=False)

"""
#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/ACCESS_1_deg_anomalies.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies.nc')
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies_cloud.nc')
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

if season=='MAM':
    TAS = 3,
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

#Function for calculating the model mean 
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models_SMB = [ACCESS, HADGEM_SMB, CSIRO, IPSL, MIROC5, NORESM]
#CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

PR_CMIP5  = []
ME_CMIP5  = []
SF_CMIP5  = []
PR_CMIP5 = []
RF_CMIP5  = []

for i in range(len(CMIP5_models_SMB)):
    ME_cmip5 = CMIP5_models_SMB[i].ME
    ME_CMIP5.append(ME_cmip5)
    
    SF_cmip5 = CMIP5_models_SMB[i].SF
    SF_CMIP5.append(SF_cmip5)
    
    RF_cmip5 = CMIP5_models_SMB[i].RF
    RF_CMIP5.append(RF_cmip5)
    
    
for i in range(len(CMIP5_models_SMB)):
    #PR_cmip5 = CMIP5_models[i].PR
    #PR_CMIP5.append(PR_cmip5)
    
    PR_Cmip5 = CMIP5_models_SMB[i].PR
    PR_CMIP5.append(PR_Cmip5)
    
#PR_CMIP5_model_mean = model_mean(PR_CMIP5)
ME_CMIP5_model_mean = model_mean(ME_CMIP5)
SF_CMIP5_model_mean = model_mean(SF_CMIP5)
RF_CMIP5_model_mean = model_mean(RF_CMIP5)
PR_CMIP5_model_mean = model_mean(PR_CMIP5)


#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

PR_CMIP6  = []
ME_CMIP6  = []
SF_CMIP6  = []
RF_CMIP6  = []
PR_CMIP6  = []

for i in range(len(CMIP6_models)):
    #PR_cmip6 = CMIP6_models[i].PR
    #PR_CMIP6.append(PR_cmip6)
    
    ME_cmip6 = CMIP6_models[i].ME
    ME_CMIP6.append(ME_cmip6)
    
    SF_cmip6 = CMIP6_models[i].SF
    SF_CMIP6.append(SF_cmip6)
    
    RF_cmip6 = CMIP6_models[i].RF
    RF_CMIP6.append(RF_cmip6)

    PR_Cmip6 = CMIP6_models[i].PR
    PR_CMIP6.append(PR_Cmip6)
    
#PR_CMIP6_model_mean = model_mean(PR_CMIP6)
ME_CMIP6_model_mean = model_mean(ME_CMIP6)
SF_CMIP6_model_mean = model_mean(SF_CMIP6)
RF_CMIP6_model_mean = model_mean(RF_CMIP6)
PR_CMIP6_model_mean = model_mean(PR_CMIP6)

#PR_diff = PR_CMIP6_model_mean - PR_CMIP5_model_mean
ME_diff = ME_CMIP6_model_mean - ME_CMIP5_model_mean
SF_diff = SF_CMIP6_model_mean - SF_CMIP5_model_mean
RF_diff = RF_CMIP6_model_mean - RF_CMIP5_model_mean
PR_diff = PR_CMIP6_model_mean - PR_CMIP5_model_mean




### ======= MULTIPLOT ======= ###
proj = ccrs.LambertConformal(central_longitude=-35,
                            central_latitude=65,
                            standard_parallels=[35])

#fig, axes = plt.subplots( ncols=2, nrows=3, figsize=(10, 12), subplot_kw={'projection': proj})
fig, axes = plt.subplots( ncols=2, nrows=3, figsize=set_size(width=460, fraction=1/3), subplot_kw={'projection': proj})


ax = axes.ravel().tolist()


for i in [0,1,2,3,4,5]:
    ax[i].add_feature(cartopy.feature.OCEAN.with_scale(
        '50m'), zorder=1, facecolor='white')           
    ax[i].add_feature(cartopy.feature.COASTLINE.with_scale(
        '50m'), zorder=1, edgecolor='black')
    ax[i].set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())    


#divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
#divnorm=colors(vmin=vmin, vcenter=vcenter, vmax=vmax)

if season == 'JJA':
    vmin=-800
    vmax=800
    
if season == 'MAM':
    vmin=-10
    vmax=10
    
if season == 'SON':
    vmin=-20
    vmax=20
    
#CMIP5 model mean
cont = ax[0].pcolormesh(ds['LON'], ds['LAT'], PR_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r')#, vmin=vmin, vmax=vmax)
#CMIP6 model mean
cont2 = ax[1].pcolormesh(ds['LON'], ds['LAT'], PR_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r')#, vmin=vmin, vmax=vmax)

#CMIP6 model mean
cont4 = ax[2].pcolormesh(ds['LON'], ds['LAT'], ME_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r')#, vmin=vmin, vmax=vmax)

#CMIP5 model mean
cont = ax[3].pcolormesh(ds['LON'], ds['LAT'], ME_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r')#, vmin=vmin, vmax=vmax)

#CMIP5 model mean
cont3 = ax[4].pcolormesh(ds['LON'], ds['LAT'], SF_CMIP5_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r')#, vmin=vmin, vmax=vmax)
#CMIP6 model mean
cont4 = ax[5].pcolormesh(ds['LON'], ds['LAT'], SF_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r')#, vmin=vmin, vmax=vmax)







plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})

#Top title
title_top = ['CMIP5', 'CMIP6']    
j = 0
for i in [0,1]:
    ax[i].set_title(title_top[j], fontsize=14)
    j += 1
    
# Left side title
title_left = ['PR', 'Melt', 'SFnoff']    
j = 0
for i in [0, 2, 4]:
    ax[i].text(-0.5, 0.5, title_left[j], transform=ax[i].transAxes,fontsize=14, fontweight="bold")
    j += 1
    
    
#remove outer box of the plot 
fig.patch.set_visible(False)
ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')
ax[4].axis('off')
ax[5].axis('off')



fig.canvas.draw()
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
    

plt.subplots_adjust(left=0.2, right=0.98, top=0.97, bottom=0.24)
cbar = fig.colorbar(cont2, ax=ax, shrink=0.7, orientation ='vertical')
cbar.set_label('Seasonal('+season+') SMB anomalies [mmWE]', fontsize=14)

#plt.suptitle(suptitle, fontsize = 16, y=0.95, x=0.40)
plt.show()
    
#if savefig == TSFe:
#fig.savefig('/projects/NS9600K/idunnam/src/Figures/1_deg_spatial_plots/energy_multiplot.png')
fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/'+str(TAS)+'_'+season+'_deg_pr_multiplot.png')



### ======= MULTIPLOT ======= ###
proj = ccrs.LambertConformal(central_longitude=-35,
                            central_latitude=65,
                            standard_parallels=[35])

fig, axes = plt.subplots( ncols=1, nrows=4, figsize=(10, 12), subplot_kw={'projection': proj})

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
    vmin=-100
    vmax=100
    
if season == 'MAM':
    vmin=-5
    vmax=5
    
if season == 'SON':
    vmin=-20
    vmax=20
    

cont3 = ax[0].pcolormesh(ds['LON'], ds['LAT'], PR_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin=vmin, vmax=vmax)
cont2 = ax[1].pcolormesh(ds['LON'], ds['LAT'], ME_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin=vmin, vmax=vmax)

cont = ax[2].pcolormesh(ds['LON'], ds['LAT'], SF_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin=vmin, vmax=vmax)

cont = ax[3].pcolormesh(ds['LON'], ds['LAT'], RF_diff,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin=vmin, vmax=vmax)






plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 20})

#Top title
title_top = [''+season+'']    
j = 0
for i in [0]:
    ax[i].set_title(title_top[j], fontsize=20,fontweight="extra bold")
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
    

plt.subplots_adjust(left=0.2, right=0.98, top=0.97, bottom=0.24)
cbar = fig.colorbar(cont2, ax=ax, shrink=0.8, orientation ='vertical')
cbar.set_label('(CMIP6-CMIP5) SMB amonalies [mmWE]', fontsize=20)

# Left side title
title_left = ['PR', 'Melt', 'SFnoff','Refreezing']    
j = 0
for i in [0, 1, 2, 3]:
    ax[i].text(-0.75, 0.5, title_left[j], transform=ax[i].transAxes,fontsize=20, fontweight="extra bold")
    j += 1

#plt.suptitle(suptitle, fontsize = 16, y=0.95, x=0.40)
plt.show()
    
fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/'+str(TAS)+'_'+season+'_deg_PR_diff_multiplot.pdf',bbox_inches='tight',dpi=300)

    