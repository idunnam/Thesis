import xarray as xr
import matplotlib.pyplot as plt

"""

#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/ACCESS_1_deg_anomalies.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies.nc')
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
"""
#CMIP5 models
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/ACCESS_rol_4.nc').mean(dim='year')
HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/HADGEM_rol_4.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/HADGEM_cloud_rol_4.nc').mean(dim='year')
HADGEM_SMB_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/HADGEM_SMB_rol_4.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/CSIRO_rol_4.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/IPSL_rol_4.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/MIROC5_rol_4.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/NORESM_rol_4.nc').mean(dim='year')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/CESM_rol_4.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/CNRM_ESM2_rol_4.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/CNRM_CM6_rol_4.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/MRI_rol_4.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/UKMO_rol_4.nc').mean(dim='year')
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


from function_diff_plot import diff_plot


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


plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})




#=== NET Energy Flux ===#
diff_plot(NET_f_CMIP6_model_mean,NET_f_CMIP5_model_mean, ds['LON'], ds['LAT'],
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Net surface energy flux anomalies [Wm$^{-2}$]',
          title_plot='(CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_NET_'+season)

#=== NET Radiative Energy Flux ===#
diff_plot(NET_rad_f_CMIP6_model_mean,NET_rad_f_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Net Radiative energy flux anomalies [Wm$^{-2}$]',
          title_plot='(CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_NET_rad_'+season)


#=== NET Non-Radiative Energy Flux ===#
diff_plot(NET_non_rad_f_CMIP6_model_mean,NET_non_rad_f_CMIP5_model_mean, ds['LON'], ds['LAT'],
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Net non-Radiative flux anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_NET_non_rad_'+season)



#=== Albedo  ===#
diff_plot(ALB_CMIP6_model_mean*100,ALB_CMIP5_model_mean*100, ds['LON'], ds['LAT'],
          vmin=-4, vmax=4,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Albedo anomalies [$\%$]',
          cmap_color='RdBu_r',
          #title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          file_title='4_deg_diff_Albedo_'+season)


#=== SW_net Flux ===#
diff_plot(SW_net_CMIP6_model_mean,SW_net_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) SW$_{net}$ anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_SW_net_'+season)


#=== SWD Flux ===#
diff_plot(SWD_CMIP6_model_mean,SWD_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -10,10,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) SWD anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_SWD_'+season)

#=== LWD Flux ===#
diff_plot(LWD_CMIP6_model_mean,LWD_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -5,5,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) LWD anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_LWD_'+season)


#=== LW_net Flux ===#
diff_plot(LW_net_CMIP6_model_mean,LW_net_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -5,5,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) LW$_{net}$ anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_LW_net_'+season)


#=== SHF Flux ===#
diff_plot(SHF_CMIP6_model_mean,SHF_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -5,5,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) SHF anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',file_title='4_deg_diff_SHF_'+season)


#=== LHF Flux ===#
diff_plot(LHF_CMIP6_model_mean,LHF_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -5,5,
          surf_height_data = ds['SH'],
          add_contour_levels = False,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) LHF anomalies [Wm$^{-2}$]',
          title_plot='Seasonal('+season+') (CMIP6-CMIP5) anomalies',
          cmap_color='RdBu_r',
          file_title='4_deg_diff_LHF_'+season)







"""
import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})


    
proj = ccrs.LambertConformal(central_longitude=-35,
                                central_latitude=65,
                                standard_parallels=[35])
fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'projection': proj})
levels = 2000,3000

#divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter., vmax=vmax, cbar_title=None) 

ax.add_feature(cartopy.feature.OCEAN.with_scale(
                '50m'), zorder=1, facecolor='white')           
ax.add_feature(cartopy.feature.COASTLINE.with_scale(
                '50m'), zorder=1, edgecolor='black')
ax.set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())


    
cont = ax.pcolormesh(ds['LON'], ds['LAT'], ALB_CMIP6_model_mean,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r',vmin=-0.2, vmax=0.2)
plt.contour(ds['LON'],ds['LAT'],ds['SH'], [2000,3000],transform=ccrs.PlateCarree(),colors='black',linestyles = 'dashed', alpha=0.7, linewidths=0.8)

#remove outer box of the plot 
fig.patch.set_visible(False)
ax.axis('off')


fig.canvas.draw()
fig.tight_layout(pad=0.01)

plt.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.24)

cbar = fig.colorbar(cont, ax=ax, shrink=0.96, orientation ='vertical')
cbar.set_label('test', fontsize=14)  

fig.savefig('/projects/NS9600K/idunnam/src/Figures/4_deg_spatial_plots/TEST.png')
plt.show()
"""