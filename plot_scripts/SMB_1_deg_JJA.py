import xarray as xr
from function_two_plots import two_plots
from function_diff_plot import diff2_plot
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

#dataset for choosing coordinates
ds = xr.open_dataset('/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/MARv3.9-ACCESS13-2074.nc', decode_times=False)

# === Calculate the model mean of each variable ==#
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]

SMB_CMIP5 = [] #SMB
ME_CMIP5  = [] #Melt
RU_CMIP5  = [] #Run-off

for i in range(len(CMIP5_models)):
    SMB_cmip5 = CMIP5_models[i].SMB
    SMB_CMIP5.append(SMB_cmip5)
    
    ME_cmip5 = CMIP5_models[i].ME
    ME_CMIP5.append(ME_cmip5)
    
    RU_cmip5 = CMIP5_models[i].RU
    RU_CMIP5.append(RU_cmip5)

SMB_CMIP5_model_mean = model_mean(SMB_CMIP5)
ME_CMIP5_model_mean = model_mean(ME_CMIP5)
RU_CMIP5_model_mean = model_mean(RU_CMIP5)


#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

SMB_CMIP6 = [] 
ME_CMIP6  = []
RU_CMIP6  = []



for i in range(len(CMIP6_models)):
    SMB_cmip6 = CMIP6_models[i].SMB
    SMB_CMIP6.append(SMB_cmip6)
    
    ME_cmip6 = CMIP6_models[i].ME
    ME_CMIP6.append(ME_cmip6)
    
    RU_cmip6 = CMIP6_models[i].RU
    RU_CMIP6.append(RU_cmip6)

SMB_CMIP6_model_mean = model_mean(SMB_CMIP6)
ME_CMIP6_model_mean = model_mean(ME_CMIP6)
RU_CMIP6_model_mean = model_mean(RU_CMIP6)



#=== SMB ===#
two_plots(SMB_CMIP5_model_mean, SMB_CMIP6_model_mean, ds['LON'], ds['LAT'],
              vmin=-800, vmax=0,
              title_fig_l = 'CMIP5 MAR simulations',  
              title_fig_r = 'CMIP6 MAR simulations',
              fontsize_title_fig = 16,
              cbar_title = 'SMB anomalies' , cmap_color = 'Blues_r', 
              suptitle = 'Model Mean',
              savefig = True, file_title = 'SMB_two_plots')


#===SMB ===#
diff2_plot(SMB_CMIP6_model_mean,SMB_CMIP5_model_mean, ds['LON'], ds['LAT'],-150,150, '(CMIP6-CMIP5) SMB anomalies [mmWE] ','RdBu_r',file_title='diff_SMB')#,cbar_title= '(CMIP6-CMIP5) SMB anomalies [mmWE]')


#=== ME ===#
two_plots(ME_CMIP5_model_mean, ME_CMIP6_model_mean, ds['LON'], ds['LAT'],
              vmin=0, vmax=800,
              title_fig_l = 'CMIP5 MAR simulations',  
              title_fig_r = 'CMIP6 MAR simulations',
              fontsize_title_fig = 16,
              cbar_title = 'Melt anomalies' , cmap_color = 'Reds', 
              suptitle = 'Model Mean',
              savefig = True, file_title = 'ME_two_plots')


#===ME ===#
diff2_plot(ME_CMIP6_model_mean,ME_CMIP5_model_mean, ds['LON'], ds['LAT'], -150,150,'(CMIP6-CMIP5) Melt anomalies [mmWE]','RdBu_r',file_title='diff_ME')#,cbar_title= '(CMIP6-CMIP5) Melt anomalies [mmWE]')


#=== RU ===#
two_plots(RU_CMIP5_model_mean, RU_CMIP6_model_mean, ds['LON'], ds['LAT'], 
              vmin=0, vmax=800,
              title_fig_l = 'CMIP5 MAR simulations',  
              title_fig_r = 'CMIP6 MAR simulations',
              fontsize_title_fig = 16,
              cbar_title = 'Run-off anomalies' , cmap_color = 'Reds', 
              suptitle = 'Model Mean',
              savefig = True, file_title = 'RU_two_plots')


#===RU ===#
diff2_plot(RU_CMIP6_model_mean,RU_CMIP5_model_mean, ds['LON'], ds['LAT'],-150,150, '(CMIP6-CMIP5) Run-off anomalies [mmWE]','RdBu_r',file_title='diff_RU')#, cbar_title= '(CMIP6-CMIP5) Run-off anomalies [mmWE]')
              
