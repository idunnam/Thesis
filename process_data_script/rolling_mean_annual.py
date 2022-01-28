import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/ACCESS_anomaly_annual.nc')
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_cloud_annual.nc')
HADGEM_SMB = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_SMB_annual.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_annual.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CSIRO_anomaly_annual.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/IPSL_anomaly_annual.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/MIROC5_anomaly_annual.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/NORESM_anomaly_annual.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CESM_anomaly_annual.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CNRM_ESM2_anomaly_annual.nc')
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CNRM_CM6_anomaly_annual.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/MRI_anomaly_annual.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/UKMO_anomaly_annual.nc')


#Spatial-rolling mean
ACCESS_time = ACCESS.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
HADGEM_time = HADGEM.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
HADGEM_cloud_time = HADGEM_cloud.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
HADGEM_SMB_time = HADGEM_SMB.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
CSIRO_time  = CSIRO.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
IPSL_time   = IPSL.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
MIROC5_time = MIROC5.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
NORESM_time = NORESM.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()

CESM_time      = CESM.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
CNRM_ESM2_time = CNRM_ESM2.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
CNRM_CM6_time  = CNRM_CM6.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
MRI_time       = MRI.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()
UKMO_time      = UKMO.mean(dim=['X10_105', 'Y21_199']).rolling(year=20,center= True).mean()

"""
#Rolling mean
ACCESS_r = ACCESS.rolling(year=20,center= True).mean()
HADGEM_r = HADGEM.rolling(year=20,center= True).mean()
HADGEM_cloud_r = HADGEM_cloud.rolling(year=20,center= True).mean()
CSIRO_r  = CSIRO.rolling(year=20,center= True).mean()
IPSL_r   = IPSL.rolling(year=20,center= True).mean()
MIROC5_r = MIROC5.rolling(year=20,center= True).mean()
NORESM_r = NORESM.rolling(year=20,center= True).mean()

CESM_r = CESM.rolling(year=20,center= True).mean()
CNRM_ESM2_r = CNRM_ESM2.rolling(year=20,center= True).mean()
CNRM_CM6_r = CNRM_CM6.rolling(year=20,center= True).mean()
MRI_r = MRI.rolling(year=20,center= True).mean()
UKMO_r = UKMO.rolling(year=20,center= True).mean()
"""

TAS = int(input('Enter TAS='))

#Select the year -/+10year interval of the year closest to 3.5deg warming for each model.
ACCESS_sel = ACCESS.sel(year= slice(str(ACCESS_time.year.where((ACCESS_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(ACCESS_time.year.where((ACCESS_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

HADGEM_sel = HADGEM.sel(year= slice(str(HADGEM_time.year.where((HADGEM_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(HADGEM_time.year.where((HADGEM_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

HADGEM_cloud_sel = HADGEM_cloud.sel(year= slice(str(HADGEM_cloud_time.year.where((HADGEM_cloud_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                                str(HADGEM_cloud_time.year.where((HADGEM_cloud_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

HADGEM_SMB_sel = HADGEM_SMB.sel(year= slice(str(HADGEM_SMB_time.year.where((HADGEM_SMB_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(HADGEM_SMB_time.year.where((HADGEM_SMB_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

#if season == 'JJA':
#    CSIRO_sel= CSIRO.sel(year=slice('2080','2100'))
#else:
CSIRO_sel = CSIRO.sel(year= slice(str(CSIRO_time.year.where((CSIRO_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                  str(CSIRO_time.year.where((CSIRO_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

IPSL_sel = IPSL.sel(year= slice(str(IPSL_time.year.where((IPSL_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(IPSL_time.year.where((IPSL_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

MIROC5_sel = MIROC5.sel(year= slice(str(MIROC5_time.year.where((MIROC5_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(MIROC5_time.year.where((MIROC5_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

NORESM_sel = NORESM.sel(year= slice(str(NORESM_time.year.where((NORESM_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(NORESM_time.year.where((NORESM_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

CESM_sel = CESM.sel(year= slice(str(CESM_time.year.where((CESM_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                str(CESM_time.year.where((CESM_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

CNRM_ESM2_sel = CNRM_ESM2.sel(year= slice(str(CNRM_ESM2_time.year.where((CNRM_ESM2_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                          str(CNRM_ESM2_time.year.where((CNRM_ESM2_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

CNRM_CM6_sel = CNRM_CM6.sel(year= slice(str(CNRM_CM6_time.year.where((CNRM_CM6_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(CNRM_CM6_time.year.where((CNRM_CM6_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

MRI_sel = MRI.sel(year= slice(str(MRI_time.year.where((MRI_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(MRI_time.year.where((MRI_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

UKMO_sel = UKMO.sel(year= slice(str(UKMO_time.year.where((UKMO_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(UKMO_time.year.where((UKMO_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))


#Yearly mean of the 20year interval selected above
ACCESS_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_'+str(TAS)+'_annual.nc')
HADGEM_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_'+str(TAS)+'_annual.nc')
HADGEM_cloud_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_'+str(TAS)+'_annual.nc')
HADGEM_SMB_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_SMB_rol_'+str(TAS)+'_annual.nc')
CSIRO_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_'+str(TAS)+'_annual.nc')
IPSL_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_'+str(TAS)+'_annual.nc')
MIROC5_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_'+str(TAS)+'_annual.nc')
NORESM_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_'+str(TAS)+'_annual.nc')

CESM_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_'+str(TAS)+'_annual.nc')
CNRM_ESM2_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_'+str(TAS)+'_annual.nc')
CNRM_CM6_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_'+str(TAS)+'_annual.nc')
MRI_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_'+str(TAS)+'_annual.nc')
UKMO_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_'+str(TAS)+'_annual.nc')




#Print 

ACCESS = ACCESS.mean(dim=['X10_105', 'Y21_199'])
HADGEM = HADGEM.mean(dim=['X10_105', 'Y21_199'])
CSIRO  = CSIRO.mean(dim=['X10_105', 'Y21_199'])
IPSL   = IPSL.mean(dim=['X10_105', 'Y21_199'])
MIROC5 = MIROC5.mean(dim=['X10_105', 'Y21_199'])
NORESM = NORESM.mean(dim=['X10_105', 'Y21_199'])

CESM = CESM.mean(dim=['X10_105', 'Y21_199'])
CNRM_ESM2 = CNRM_ESM2.mean(dim=['X10_105', 'Y21_199'])
CNRM_CM6 = CNRM_CM6.mean(dim=['X10_105', 'Y21_199'])
MRI = MRI.mean(dim=['X10_105', 'Y21_199'])
UKMO = UKMO.mean(dim=['X10_105', 'Y21_199'])

ACCESS = ACCESS.rolling(year=20,center= True).mean()
HADGEM = HADGEM.rolling(year=20,center= True).mean()
CSIRO  = CSIRO.rolling(year=20,center= True).mean()
IPSL   = IPSL.rolling(year=20,center= True).mean()
MIROC5 = MIROC5.rolling(year=20,center= True).mean()
NORESM = NORESM.rolling(year=20,center= True).mean()

CESM = CESM.rolling(year=20,center= True).mean()
CNRM_ESM2 = CNRM_ESM2.rolling(year=20,center= True).mean()
CNRM_CM6 = CNRM_CM6.rolling(year=20,center= True).mean()
MRI = MRI.rolling(year=20,center= True).mean()
UKMO = UKMO.rolling(year=20,center= True).mean()

TAS = [1.5, 2.0 ,2.5, 3.0, 3.5, 4.0]
for i in range(0,6):
    print('TAS:', TAS[i])
    print('Model','     year', '     interval', '     mean', '     std')
    print('--------------------------------------------------')
    print('ACCESS   :',np.int(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((ACCESS.sel(year=slice(
              str(np.int(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((ACCESS.sel(year=slice(
              str(np.int(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(ACCESS.year.where((ACCESS.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
         
         

         
    print('HADGEM   :',np.int(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((HADGEM.sel(year=slice(
              str(np.int(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((HADGEM.sel(year=slice(
              str(np.int(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(HADGEM.year.where((HADGEM.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
               
    
  
    print('CSIRO    :',np.int(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((CSIRO.sel(year=slice(
              str(np.int(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((CSIRO.sel(year=slice(
              str(np.int(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CSIRO.year.where((CSIRO.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
    
    
    print('IPSL     :',np.int(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((IPSL.sel(year=slice(
              str(np.int(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((IPSL.sel(year=slice(
              str(np.int(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(IPSL.year.where((IPSL.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
    
    
    print('MIROC5   :',np.int(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((MIROC5.sel(year=slice(
              str(np.int(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((MIROC5.sel(year=slice(
              str(np.int(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(MIROC5.year.where((MIROC5.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
      
    print('NORESM   :',np.int(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((NORESM.sel(year=slice(
              str(np.int(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((NORESM.sel(year=slice(
              str(np.int(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(NORESM.year.where((NORESM.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
      


    print('CESM     :',np.int(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((CESM.sel(year=slice(
              str(np.int(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((CESM.sel(year=slice(
              str(np.int(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CESM.year.where((CESM.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
      
    
    print('CNRM_ESM2:',np.int(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((CNRM_ESM2.sel(year=slice(
              str(np.int(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((CNRM_ESM2.sel(year=slice(
              str(np.int(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CNRM_ESM2.year.where((CNRM_ESM2.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
      
    print('CNRM_CM6 :',np.int(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((CNRM_CM6.sel(year=slice(
              str(np.int(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((CNRM_CM6.sel(year=slice(
              str(np.int(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(CNRM_CM6.year.where((CNRM_CM6.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
     
    
    print('MRI      :',np.int(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((MRI.sel(year=slice(
              str(np.int(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((MRI.sel(year=slice(
              str(np.int(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(MRI.year.where((MRI.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
     
    print('UKESM    :',np.int(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values),
         ' (',
         np.int(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values - 10),
          '-',
          np.int(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values + 10),
          ')   ',
          np.round((UKMO.sel(year=slice(
              str(np.int(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT.mean()).values,2),
          '    ',
          np.round(np.std((UKMO.sel(year=slice(
              str(np.int(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values - 10)),
              str(UKMO.year.where((UKMO.TT >=TAS[i])).dropna(dim='year')[0].values + 10))).TT)).values,2))
     
    print('--------------------------------------------------')
    print('--------------------------------------------------')