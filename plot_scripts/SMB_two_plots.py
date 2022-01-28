import xarray as xr
import matplotlib.pyplot as plt 

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
HADGEM       = HADGEM_SMB_rol_4 
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


from function_two_plots import two_plots


# === Calculate the model mean of each variable ==#

#Function for calculating the model mean 
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models_SMB = [ACCESS, HADGEM_SMB, CSIRO, IPSL, MIROC5, NORESM]
CMIP5_models_precipitation = [ACCESS, HADGEM_cloud, CSIRO, IPSL, MIROC5, NORESM]

SMB_CMIP5    = []
SU_CMIP5     = []
RU_CMIP5     = []
ME_CMIP5     = []

PR_CMIP5     = []
RF_CMIP5     = []
SF_CMIP5     = []

for i in range(len(CMIP5_models_SMB)):
    SMB_cmip5 = CMIP5_models_SMB[i].SMB
    SMB_CMIP5.append(SMB_cmip5)
    
    SU_cmip5 = CMIP5_models_SMB[i].SU
    SU_CMIP5.append(SU_cmip5)
    
    RU_cmip5 = CMIP5_models_SMB[i].RU
    RU_CMIP5.append(RU_cmip5)
    
    ME_cmip5 = CMIP5_models_SMB[i].ME
    ME_CMIP5.append(ME_cmip5)

for i in range(len(CMIP5_models_precipitation)):    
    PR_cmip5 = CMIP5_models_precipitation[i].PR
    PR_CMIP5.append(PR_cmip5)
    
    RF_cmip5 = CMIP5_models_precipitation[i].RF
    RF_CMIP5.append(RF_cmip5)
    
    SF_cmip5 = CMIP5_models_precipitation[i].SF
    SF_CMIP5.append(SF_cmip5)
    
SMB_CMIP5_model_mean = model_mean(SMB_CMIP5)
SU_CMIP5_model_mean = model_mean(SU_CMIP5)
RU_CMIP5_model_mean = model_mean(RU_CMIP5)
ME_CMIP5_model_mean = model_mean(ME_CMIP5)

PR_CMIP5_model_mean = model_mean(PR_CMIP5)
RF_CMIP5_model_mean = model_mean(RF_CMIP5)
SF_CMIP5_model_mean = model_mean(SF_CMIP5)




#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

SMB_CMIP6    = []
SU_CMIP6     = []
RU_CMIP6     = []
ME_CMIP6     = []

PR_CMIP6     = []
RF_CMIP6     = []
SF_CMIP6     = []
for i in range(len(CMIP6_models)):
    SMB_cmip6 = CMIP6_models[i].SMB
    SMB_CMIP6.append(SMB_cmip6)
    
    SU_cmip6 = CMIP6_models[i].SU
    SU_CMIP6.append(SU_cmip6)
    
    RU_cmip6 = CMIP6_models[i].RU
    RU_CMIP6.append(RU_cmip6)
    
    ME_cmip6 = CMIP6_models[i].ME
    ME_CMIP6.append(ME_cmip6)
    
    PR_cmip6 = CMIP6_models[i].PR
    PR_CMIP6.append(PR_cmip6)
    
    RF_cmip6 = CMIP6_models[i].RF
    RF_CMIP6.append(RF_cmip6)
    
    SF_cmip6 = CMIP6_models[i].SF
    SF_CMIP6.append(SF_cmip6)
    
SMB_CMIP6_model_mean = model_mean(SMB_CMIP6)    
SU_CMIP6_model_mean = model_mean(SU_CMIP6)
RU_CMIP6_model_mean = model_mean(RU_CMIP6)
ME_CMIP6_model_mean = model_mean(ME_CMIP6)
PR_CMIP6_model_mean = model_mean(PR_CMIP6)
RF_CMIP6_model_mean = model_mean(RF_CMIP6)
SF_CMIP6_model_mean = model_mean(SF_CMIP6)

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})

#=== SMB ===#
two_plots(SMB_CMIP5_model_mean, SMB_CMIP6_model_mean, ds['LON'], ds['LAT'], -600,600,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'SMB [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_SMB_net_two_plots')

#=== SU (sublimation) ===#
two_plots(SU_CMIP5_model_mean, SU_CMIP6_model_mean, ds['LON'], ds['LAT'], -10,10,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'Sublimation [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_SU_net_two_plots')

#=== RU (Runoff) ===#
two_plots(RU_CMIP5_model_mean, RU_CMIP6_model_mean, ds['LON'], ds['LAT'], -500,500,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'Runoff [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_RU_net_two_plots')

#=== ME (Melt) ===#
two_plots(ME_CMIP5_model_mean, ME_CMIP6_model_mean, ds['LON'], ds['LAT'], -500,500,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'Melt [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_ME_net_two_plots')

#=== PR (precipitation) ===#
two_plots(PR_CMIP5_model_mean, PR_CMIP6_model_mean, ds['LON'], ds['LAT'], -50,50,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'PR [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_PR_net_two_plots')

#=== RF (Rainfall) ===#
two_plots(RF_CMIP5_model_mean, RF_CMIP6_model_mean, ds['LON'], ds['LAT'], -50,50,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'RF [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_RF_net_two_plots')

#=== SF (Snowfall) ===#
two_plots(SF_CMIP5_model_mean, SF_CMIP6_model_mean, ds['LON'], ds['LAT'], -50,50,
              surf_height_data = ds['SH'],
              add_contour_levels = True,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = 'SF [mmWE]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_SF_net_two_plots')