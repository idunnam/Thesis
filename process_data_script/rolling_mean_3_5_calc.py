"""
This code is used to pick a twenty-year period for a 4deg warming +/- 10years and then to calculate the anomalies of each induvidual model for this warming period according to a reference period for each model (1961-1990).
"""
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

season = input('Enter season [MAM, JJA, SON]:')

ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_'+season+'.nc')
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_cloud.nc')
HADGEM_SMB = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'_SMB.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_'+season+'.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CSIRO_anomaly_'+season+'.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/IPSL_anomaly_'+season+'.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MIROC5_anomaly_'+season+'.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/NORESM_anomaly_'+season+'.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CESM_anomaly_'+season+'.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_'+season+'.nc')
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_'+season+'.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_'+season+'.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_'+season+'.nc')


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

TAS = int(input('For season:MAM; Enter TAS =3\n For season:JJA,SON; Enter TAS=4\n Enter TAS='))

#Select the year -/+10year interval of the year closest to 3.5deg warming for each model.
ACCESS_sel = ACCESS.sel(year= slice(str(ACCESS_time.year.where((ACCESS_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(ACCESS_time.year.where((ACCESS_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

HADGEM_sel = HADGEM.sel(year= slice(str(HADGEM_time.year.where((HADGEM_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(HADGEM_time.year.where((HADGEM_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

HADGEM_cloud_sel = HADGEM_cloud.sel(year= slice(str(HADGEM_cloud_time.year.where((HADGEM_cloud_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                                str(HADGEM_cloud_time.year.where((HADGEM_cloud_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

HADGEM_SMB_sel = HADGEM_SMB.sel(year= slice(str(HADGEM_SMB_time.year.where((HADGEM_SMB_time.TT >=TAS)).dropna(dim='year')[0].values - 10),
                                    str(HADGEM_SMB_time.year.where((HADGEM_SMB_time.TT >=TAS)).dropna(dim='year')[0].values + 10)))

if season == 'JJA':
    CSIRO_sel= CSIRO.sel(year=slice('2080','2100'))
else:
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
ACCESS_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_'+str(TAS)+'_'+season+'.nc')
HADGEM_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_'+str(TAS)+'_'+season+'.nc')
HADGEM_cloud_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_'+str(TAS)+'_'+season+'.nc')
HADGEM_SMB_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_SMB_rol_'+str(TAS)+'_'+season+'.nc')
CSIRO_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_'+str(TAS)+'_'+season+'.nc')
IPSL_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_'+str(TAS)+'_'+season+'.nc')
MIROC5_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_'+str(TAS)+'_'+season+'.nc')
NORESM_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_'+str(TAS)+'_'+season+'.nc')

CESM_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_'+str(TAS)+'_'+season+'.nc')
CNRM_ESM2_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_'+str(TAS)+'_'+season+'.nc')
CNRM_CM6_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_'+str(TAS)+'_'+season+'.nc')
MRI_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_'+str(TAS)+'_'+season+'.nc')
UKMO_sel.to_netcdf('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_'+str(TAS)+'_'+season+'.nc')
