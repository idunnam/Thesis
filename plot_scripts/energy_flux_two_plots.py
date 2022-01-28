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
season = input('Enter season [MAM, JJA, SON, DJF]:')

if season == 'MAM':
    temperature = '3'
else:
    temperature = '4'
    #CMIP5 models
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
HADGEM_SMB_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_SMB_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_'+temperature+'_'+season+'.nc').mean(dim='year')

    #CMIP6 models
CESM_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_'+temperature+'_'+season+'.nc').mean(dim='year')
    

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


from function_two_plots import two_plots


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


#=== NET ENERGY FLUX ===#
two_plots(NET_f_CMIP5_model_mean, NET_f_CMIP6_model_mean, ds['LON'], ds['LAT'],-50,50,
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              fontsize_title_fig = 16,
              cbar_title = '('+season+') Net energy flux [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_Net_flux_two_plots')



#=== NET RADIATIVE FLUX ===#
two_plots(NET_rad_f_CMIP5_model_mean, NET_rad_f_CMIP6_model_mean, ds['LON'], ds['LAT'], -50,50,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') Net Radiative energy flux [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_Net_rad_flux_two_plots')


#=== NET NON-RADIATIVE FLUX ===#
two_plots(NET_non_rad_f_CMIP5_model_mean, NET_non_rad_f_CMIP6_model_mean, ds['LON'], ds['LAT'], -50,50,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') Net non-Radiative energy flux [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_Net_non_rad_flux_two_plots')

#=== ALBEDO ===#
two_plots(ALB_CMIP5_model_mean, ALB_CMIP6_model_mean, ds['LON'], ds['LAT'], -0.2,0,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') Albedo' , cmap_color = 'Blues_r', 
              file_title = '4_deg_Albedo_two_plots')


#=== Sensible Heat Flux ===#
two_plots(SHF_CMIP5_model_mean, SHF_CMIP6_model_mean, ds['LON'], ds['LAT'], -15,15,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') SHF [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_SHF_two_plots')


#=== Latent Heat Flux ===#
two_plots(LHF_CMIP5_model_mean, LHF_CMIP6_model_mean, ds['LON'], ds['LAT'], -15,15,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') LHF [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_LHF_two_plots')


#=== Long Waved Down ===#
two_plots(LWD_CMIP5_model_mean, LWD_CMIP6_model_mean, ds['LON'], ds['LAT'], -30,30,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') LWD [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_LWD_two_plots')

#=== LW_net ===#
two_plots(LW_net_CMIP5_model_mean, LW_net_CMIP6_model_mean, ds['LON'], ds['LAT'], -30,30,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') LW$_{net}$ [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_LW_net_two_plots')


#=== SWD ===#
two_plots(SWD_CMIP5_model_mean, SWD_CMIP6_model_mean, ds['LON'], ds['LAT'], -30,30,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') SWD [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_SWD_two_plots')


#=== SW_net ===#
two_plots(SW_net_CMIP5_model_mean, SW_net_CMIP6_model_mean, ds['LON'], ds['LAT'], -30,30,
              surf_height_data = ds['SH'],
              add_contour_levels = False,
              contour_levels = [2000,3000],
              title_fig_l = 'MAR CMIP5 Model mean',  
              title_fig_r = 'MAR CMIP6 Model mean',
              fontsize_title_fig = 16,
              cbar_title = '('+season+') Net SW [Wm$^{-2}$]' , cmap_color = 'RdBu_r', 
              file_title = '4_deg_SW_net_two_plots')

