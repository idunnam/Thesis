import xarray as xr
from function_two_plots import two_plots

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
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models = [ACCESS, HADGEM_cloud, CSIRO, IPSL, MIROC5, NORESM]

CC_CMIP5 = [] #Cloud Cover (total)
CU_CMIP5 = [] #Cloud Cover (UP)
CM_CMIP5 = [] #Cloud COver (Middle)
CD_CMIP5 = [] #Cloud Cover (Down)
COD_CMIP5= [] #Cloud Optical Depth


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
COD_CMIP6 = []#Cloud Optical Depth  


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

#=== tot. Cloud Cover ===#
two_plots(CC_CMIP5_model_mean*100, CC_CMIP6_model_mean*100, ds['LON'], ds['LAT'], -8, 8,
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              fontsize_title_fig = 16,
              cbar_title = 'tot. Cloud Cover anomalies [$\%$]' , cmap_color = 'RdBu_r', 
              suptitle = None,
              file_title = '4_deg_CC_two_plots')


#=== High Cloud Cover ===#
two_plots(CU_CMIP5_model_mean*100, CU_CMIP6_model_mean*100, ds['LON'], ds['LAT'], -8, 8,
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              fontsize_title_fig = 16,
              cbar_title = 'High level Cloud Cover anomalies [$\%$]' , cmap_color = 'RdBu_r',
              suptitle = None,
              file_title = '4_deg_CU_two_plots')

#=== Mid Cloud Cover ===#
two_plots(CM_CMIP5_model_mean*100, CM_CMIP6_model_mean*100, ds['LON'], ds['LAT'], -8, 8,
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              fontsize_title_fig = 16,
              cbar_title = 'Mid level Cloud Cover anomalies [$\%$]' , cmap_color = 'RdBu_r',
              suptitle = None,
              file_title = '4_deg_CM_two_plots')

#=== Low Cloud Cover ===#
two_plots(CD_CMIP5_model_mean*100, CD_CMIP6_model_mean*100, ds['LON'], ds['LAT'], -8, 8,
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              fontsize_title_fig = 16,
              cbar_title = 'Low level Cloud Cover anomalies [$\%$]' , cmap_color = 'RdBu_r',
              suptitle = None,
              file_title = '4_deg_CD_two_plots')
              
    
#=== Cloud Optical Depth ===#
two_plots(COD_CMIP5_model_mean, COD_CMIP6_model_mean, ds['LON'], ds['LAT'], -1, 1,
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              fontsize_title_fig = 16,
              cbar_title = 'Cloud Optical Depth anomalies' , cmap_color = 'RdBu_r',
              suptitle = None,
              file_title = '4_deg_COD_two_plots')
              
