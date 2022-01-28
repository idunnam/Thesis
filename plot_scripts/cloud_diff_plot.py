import xarray as xr
from function_diff_plot import diff_plot
"""
#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/ACCESS_1_deg_anomalies.nc')
#HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies.nc')
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
season = input('Enter season here:')
#CMIP5 models
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_4_'+season+'.nc').mean(dim='year')
#HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_4'+season+'.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_4_'+season+'.nc').mean(dim='year')
#HADGEM_SMB_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_SMB_rol_4_'+season+'.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_4_'+season+'.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_4_'+season+'.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_4_'+season+'.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_4_'+season+'.nc').mean(dim='year')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_4_'+season+'.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_4_'+season+'.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_4_'+season+'.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_4_'+season+'.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_4_'+season+'.nc').mean(dim='year')

ACCESS       = ACCESS_rol_4 
#HADGEM       = HADGEM_rol_4 
HADGEM_cloud = HADGEM_cloud_rol_4
#HADGEM_SMB   = HADGEM_SMB_rol_4 
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
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models = [ACCESS, HADGEM_cloud, CSIRO, IPSL, MIROC5, NORESM]

CC_CMIP5 = [] #Cloud Cover (total)
CU_CMIP5 = [] #Cloud Cover (UP)
CM_CMIP5 = [] #Cloud COver (Middle)
CD_CMIP5 = [] #Cloud Cover (Down)
COD_CMIP5 = [] #Cloud Optical Depth


for i in range(len(CMIP5_models)):
    CC_cmip5 = CMIP5_models[i].CC
    CC_CMIP5.append(CC_cmip5)
      
    CU_cmip5 = CMIP5_models[i].CU
    CU_CMIP5.append(CU_cmip5)
    
    CM_cmip5 = CMIP5_models[i].CM
    CM_CMIP5.append(CM_cmip5)
    
    CD_cmip5 = CMIP5_models[i].CD
    CD_CMIP5.append(CD_cmip5)
    
    COD_cmip5 = CMIP5_models[i].COD
    COD_CMIP5.append(COD_cmip5)



CC_CMIP5_model_mean = model_mean(CC_CMIP5)
CU_CMIP5_model_mean = model_mean(CU_CMIP5)
CM_CMIP5_model_mean = model_mean(CM_CMIP5)
CD_CMIP5_model_mean = model_mean(CD_CMIP5)
COD_CMIP5_model_mean = model_mean(COD_CMIP5)


#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

CC_CMIP6 = [] #Cloud Cover (total)
CU_CMIP6 = [] #Cloud Cover (UP)
CM_CMIP6 = [] #Cloud COver (Middle)
CD_CMIP6 = [] #Cloud Cover (Down)
COD_CMIP6 = [] #Cloud Optical Depth


for i in range(len(CMIP6_models)):
    CC_cmip6 = CMIP6_models[i].CC
    CC_CMIP6.append(CC_cmip6)
    
    CU_cmip6 = CMIP6_models[i].CU
    CU_CMIP6.append(CU_cmip6)
    
    CM_cmip6 = CMIP6_models[i].CM
    CM_CMIP6.append(CM_cmip6)
    
    CD_cmip6 = CMIP6_models[i].CD
    CD_CMIP6.append(CD_cmip6)
    
    COD_cmip6 = CMIP6_models[i].COD
    COD_CMIP6.append(COD_cmip6)



CC_CMIP6_model_mean = model_mean(CC_CMIP6)
CU_CMIP6_model_mean = model_mean(CU_CMIP6)
CM_CMIP6_model_mean = model_mean(CM_CMIP6)
CD_CMIP6_model_mean = model_mean(CD_CMIP6)
COD_CMIP6_model_mean = model_mean(COD_CMIP6)


#===Tot Cloud Cover ===#
diff_plot(CC_CMIP6_model_mean*100,CC_CMIP5_model_mean*100, ds['LON'], ds['LAT'], 
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) tot. Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CC')


#===Tot Upper Cover ===#
diff_plot(CU_CMIP6_model_mean*100,CU_CMIP5_model_mean*100, ds['LON'], ds['LAT'], 
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) High level Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CU')

#===Tot Middle Cover ===#
diff_plot(CM_CMIP6_model_mean*100,CM_CMIP5_model_mean*100, ds['LON'], ds['LAT'],
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Mid level Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CM')

#===Tot Lower Cover ===#
diff_plot(CD_CMIP6_model_mean*100,CD_CMIP5_model_mean*100, ds['LON'], ds['LAT'], 
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Low level Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CD')

#===Cloud optical depth ===#
diff_plot(COD_CMIP6_model_mean,COD_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -1,1,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Cloud Optical Depth anomalies',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_COD')



"""
import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})

def diff(variable_CMIP6, variable_CMIP5, lon, lat,
          cbar_title=None, cmap_color = 'RdBu_r',
          savefig = True, file_title = None):
    

    diff_var = variable_CMIP6 - variable_CMIP5

    proj = ccrs.LambertConformal(central_longitude=-35,
                                 central_latitude=65,
                                 standard_parallels=[35])
    fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'projection': proj})

    #divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter., vmax=vmax, cbar_title=None) 

    ax.add_feature(cartopy.feature.OCEAN.with_scale(
                    '50m'), zorder=1, facecolor='white')           
    ax.add_feature(cartopy.feature.COASTLINE.with_scale(
                    '50m'), zorder=1, edgecolor='black')
    ax.set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())
    
    cont = ax.pcolormesh(lon, lat, diff_var.values,   
                                        transform=ccrs.PlateCarree(),
                                        cmap=cmap_color)#, vmin=vmin, vmax=vmax)
    #remove outer box of the plot 
    fig.patch.set_visible(False)
    ax.axis('off')


    fig.canvas.draw()
    fig.tight_layout(pad=0.01)

    plt.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.24)
    cbar = fig.colorbar(cont, ax=ax, shrink=0.96, orientation ='vertical')
    cbar.set_label(
        cbar_title, fontsize=14)
    
    if savefig == True:
        fig.savefig('/projects/NS9600K/idunnam/src/Figures/_deg_spatial_plots/'+file_title+'.png')
       
diff_plot(CC_CMIP6_model_mean*100,CC_CMIP5_model_mean*100, ds['LON'], ds['LAT'],
          vmin=-5, vmax=5,
          cbar_title='(CMIP6-CMIP5) tot. cloud cover anomalies [Wm$^{-2}$]',cmap_color='RdBu_r',
          file_title='4_deg_CC_diff_map_plot.png')





### ===================== TEST ===================== ###
import xarray as xr
import matplotlib.pyplot as plt 
from matplotlib import colors

import cartopy.crs as ccrs
import cartopy.feature
# === Calculate the model mean of each variable ==#
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models = [ACCESS, HADGEM_cloud, CSIRO, IPSL, MIROC5, NORESM]

CC_CMIP5 = [] #Cloud Cover (total)
CU_CMIP5 = [] #Cloud Cover (UP)
CM_CMIP5 = [] #Cloud COver (Middle)
CD_CMIP5 = [] #Cloud Cover (Down)


for i in range(len(CMIP5_models)):
    CC_cmip5 = CMIP5_models[i].CC
    CC_CMIP5.append(CC_cmip5)
    
    CU_cmip5 = CMIP5_models[i].CU
    CU_CMIP5.append(CU_cmip5)
    
    CM_cmip5 = CMIP5_models[i].CM
    CM_CMIP5.append(CM_cmip5)
    
    CD_cmip5 = CMIP5_models[i].CD
    CD_CMIP5.append(CD_cmip5)


CC_CMIP5_model_mean = model_mean(CC_CMIP5)
CU_CMIP5_model_mean = model_mean(CU_CMIP5)
CM_CMIP5_model_mean = model_mean(CM_CMIP5)
CD_CMIP5_model_mean = model_mean(CD_CMIP5)


#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

CC_CMIP6 = [] #Cloud Cover (total)
CU_CMIP6 = [] #Cloud Cover (UP)
CM_CMIP6 = [] #Cloud COver (Middle)
CD_CMIP6 = [] #Cloud Cover (Down)


for i in range(len(CMIP6_models)):
    CC_cmip6 = CMIP6_models[i].CC
    CC_CMIP6.append(CC_cmip6)
    
    CU_cmip6 = CMIP6_models[i].CU
    CU_CMIP6.append(CU_cmip6)
    
    CM_cmip6 = CMIP6_models[i].CM
    CM_CMIP6.append(CM_cmip6)
    
    CD_cmip6 = CMIP6_models[i].CD
    CD_CMIP6.append(CD_cmip6)


CC_CMIP6_model_mean = model_mean(CC_CMIP6)
CU_CMIP6_model_mean = model_mean(CU_CMIP6)
CM_CMIP6_model_mean = model_mean(CM_CMIP6)
CD_CMIP6_model_mean = model_mean(CD_CMIP6)



## ==== Difference in model mean (CMIP6-CMIP5) ==== ## 

#calculate the total cloud cover difference 
diff_CC = CM_CMIP6_model_mean - CM_CMIP5_model_mean

proj = ccrs.LambertConformal(central_longitude=-35,
                             central_latitude=65,
                             standard_parallels=[35])
fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'projection': proj})

divnorm=colors.TwoSlopeNorm(vmin=-5, vcenter=0., vmax=5) 

ax.add_feature(cartopy.feature.OCEAN.with_scale(
                '50m'), zorder=1, facecolor='white')           
ax.add_feature(cartopy.feature.COASTLINE.with_scale(
                '50m'), zorder=1, edgecolor='black')
ax.set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())
    
cont = ax.pcolormesh(ds['LON'], ds['LAT'], diff_CC.values*100,   
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
    '(CMIP6 - CMIP5) total Cloud Cover anomalies [%]', fontsize=14)
#fig.savefig('CC_diff_map_plot.png') 
fig.savefig('4_deg_CC_diff_map_plot.png')

"""