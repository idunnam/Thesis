"""
This code is used to pick and visualize the twenty-year warming period of +4deg +/- 10years for each individual model. 
"""

import xarray as xr 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

#===================== PLOT rolling mean 4 plot timeline + STD =========================
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA_cloud.nc').mean(dim=['X10_105','Y21_199'])
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CSIRO_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/IPSL_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MIROC5_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/NORESM_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CESM_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])


#Spatial-rolling mean
ACCESS_time = ACCESS.rolling(year=20,center= True).mean()
HADGEM_time = HADGEM.rolling(year=20,center= True).mean()
HADGEM_cloud_time = HADGEM_cloud.rolling(year=20,center= True).mean()
CSIRO_time  = CSIRO.rolling(year=20,center= True).mean()
IPSL_time   = IPSL.rolling(year=20,center= True).mean()
MIROC5_time = MIROC5.rolling(year=20,center= True).mean()
NORESM_time = NORESM.rolling(year=20,center= True).mean()

CESM_time      = CESM.rolling(year=20,center= True).mean()
CNRM_ESM2_time = CNRM_ESM2.rolling(year=20,center= True).mean()
CNRM_CM6_time  = CNRM_CM6.rolling(year=20,center= True).mean()
MRI_time       = MRI.rolling(year=20,center= True).mean()
UKMO_time      = UKMO.rolling(year=20,center= True).mean()


#CMIP5 models
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_4.nc').mean(dim='year')
HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_4.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_4.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_4.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_4.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_4.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_4.nc').mean(dim='year')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_4.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_4.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_4.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_4.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_4.nc').mean(dim='year')




plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 12,
"xtick.labelsize": 12,
"ytick.labelsize": 12})

px = 1/plt.rcParams['figure.dpi']
#fig, ax = plt.subplots(1,2, figsize=(20,10),sharey=True,gridspec_kw={'width_ratios': [2, 1]})
#fig, ax = plt.subplots(2,1, figsize=(612*px,1012*px),sharex=True)
fig, ax = plt.subplots(1,2, figsize=(612*px,306*px),sharey=True,gridspec_kw={'width_ratios': [2, 1]})


ax[0].plot(ACCESS_time.year,ACCESS_time.TT,label='ACCESS', linewidth=1.2)
ax[0].plot(HADGEM_time.year,HADGEM_time.TT, label='HADGEM', linewidth=1.2)
ax[0].plot(CSIRO_time.year,CSIRO_time.TT,label='CSIRO', linewidth=1.2)
ax[0].plot(IPSL_time.year,IPSL_time.TT,label='IPSL', linewidth=1.2)
ax[0].plot(MIROC5_time.year,MIROC5_time.TT,label='MIROC5', linewidth=1.2)
ax[0].plot(NORESM_time.year,NORESM_time.TT,label='NORESM', linewidth=1.2)

####---###
#"""
ax[1].boxplot([ACCESS_time.TT.sel(year=slice('2077','2091')),
              HADGEM_time.TT.sel(year=slice('2055','2075')),
              CSIRO_time.TT.sel(year=slice('2080','2091')),
              IPSL_time.TT.sel(year=slice('2055','2075')),
              MIROC5_time.TT.sel(year=slice('2059','2079')),
              NORESM_time.TT.sel(year=slice('2068','2088')),
              CESM_time.TT.sel(year=slice('2044','2064')),
              CNRM_ESM2_time.TT.sel(year=slice('2061','2081')),
              CNRM_CM6_time.TT.sel(year=slice('2059','2079')),
              MRI_time.TT.sel(year=slice('2065','2085')),
              UKMO_time.TT.sel(year=slice('2029','2049'))],widths=0.3)
#secax = ax[0].secondary_yaxis(1.0)
#secax.set_yticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'])
ax[1].set_xticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'], rotation=90, fontsize = 11)

ax[0].plot(CESM_time.year,CESM_time.TT,'--',label='CESM')
ax[0].plot(CNRM_ESM2_time.year,CNRM_ESM2_time.TT,'--',label='CNRM-ESM2')
ax[0].plot(CNRM_CM6_time.year,CNRM_CM6_time.TT,'--',label='CNRM-CM6')
ax[0].plot(MRI_time.year, MRI_time.TT,'--',label='MRI')
ax[0].plot(UKMO_time.year,UKMO_time.TT,'--',label='UKESM', color='navy')
ax[0].legend(frameon=False, ncol=2, fontsize=7)

ax[0].hlines(4,1950,2100, color='black', linewidth= 0.7)

ax[0].set_xlabel('Year', fontsize = 11)
ax[0].set_ylabel('Near-surface temperature anomalies [$^{\circ}$C]', fontsize = 11)

"""
#ACCESS
#ax[1].set_ylim(0,11,1)
ax[0].hlines(4,2077,2097, color='blue')
ax[0].scatter(2077,4, marker ='|', s=100, color='blue')
#ax[0].scatter(2087,4, marker ='|', s=200, color='blue')
ax[0].scatter(2097,4, marker ='|', s=100, color='blue')

#HADGEM
ax[0].hlines(4,2055,2075, color='orange')
ax[0].scatter(2055,4, marker ='|', s=100, color='orange')
#ax[0].scatter(2075,4, marker ='|', s=200, color='orange')
ax[0].scatter(2065,4, marker ='|', s=100, color='orange')

#CSIRO
ax[0].hlines(4,2080,2100, color='green')
ax[0].scatter(2080,4, marker ='|', s=100, color='green')
#ax[0].scatter(2090,4, marker ='|', s=200, color='green')
ax[0].scatter(2100,4, marker ='|', s=100, color='green')

#IPSL
ax[0].hlines(4,2055,2075, color='red')
ax[0].scatter(2055,4, marker ='|', s=100, color='red')
#ax[0].scatter(2065,4, marker ='|', s=200, color='red')
ax[0].scatter(2075,4, marker ='|', s=100, color='red')

#MIROC5
ax[0].hlines(4,2059,2079, color='purple')
ax[0].scatter(2059,4, marker ='|', s=100, color='purple')
#ax[0].scatter(2069,4, marker ='|', s=200, color='purple')
ax[0].scatter(2079,4, marker ='|', s=100, color='purple')

#NORESM
ax[0].hlines(4,2068,2088, color='brown')
ax[0].scatter(2068,4, marker ='|', s=100, color='brown')
#ax[0].scatter(2078,4, marker ='|', s=200, color='brown')
ax[0].scatter(2088,4, marker ='|', s=100, color='brown')

#MIROC5
ax[0].hlines(4,2044,2064, color='pink')
ax[0].scatter(2044,4, marker ='|', s=100, color='pink')
#ax[0].scatter(2054,4, marker ='|', s=200, color='pink')
ax[0].scatter(2064,4, marker ='|', s=100, color='pink')

#CNRM_ESM2
ax[0].hlines(4,2061,2081, color='gray')
ax[0].scatter(2061,4, marker ='|', s=100, color='gray')
#ax[0].scatter(2071,4, marker ='|', s=200, color='gray')
ax[0].scatter(2081,4, marker ='|', s=100, color='gray')

#CNRM_CM6
ax[0].hlines(4,2059,2079, color='olive')
ax[0].scatter(2059,4, marker ='|', s=100, color='olive')
#ax[0].scatter(2069,4, marker ='|', s=200, color='olive')
ax[0].scatter(2079,4, marker ='|', s=100, color='olive')

#MRI
ax[0].hlines(4,2065,2085, color='cyan')
ax[0].scatter(2065,4, marker ='|', s=100, color='cyan')
#ax[0].scatter(2075,4, marker ='|', s=200, color='cyan')
ax[0].scatter(2085,4, marker ='|', s=100, color='cyan')

#UKESM
ax[0].hlines(4,2029,2049, color='navy')
ax[0].scatter(2029,4, marker ='|', s=100, color='navy')
#ax[0].scatter(2039,4, marker ='|', s=200, color='navy')
ax[0].scatter(2049,4, marker ='|', s=100, color='navy')
"""
sns.despine()

plt.savefig('Figures/temp_timeline_variation.pdf', bbox_inches='tight',dpi=300)
#"""
###---####

"""

ax[1].boxplot([ACCESS_time.year.sel(year=slice('2077','2091')),
              HADGEM_time.year.sel(year=slice('2055','2075')),
              CSIRO_time.year.sel(year=slice('2080','2091')),
              IPSL_time.year.sel(year=slice('2055','2075')),
              MIROC5_time.year.sel(year=slice('2059','2079')),
              NORESM_time.year.sel(year=slice('2068','2088')),
              CESM_time.year.sel(year=slice('2044','2064')),
              CNRM_ESM2_time.year.sel(year=slice('2061','2081')),
              CNRM_CM6_time.year.sel(year=slice('2059','2079')),
              MRI_time.year.sel(year=slice('2065','2085')),
              UKMO_time.year.sel(year=slice('2029','2049'))],xerr=10,vert=False,widths=0.3)
"""

"""

#ACCESS

ax[1].set_ylim(0,11,1)
ax[1].hlines(11,2077,2097, color='blue')
ax[1].scatter(2077,11, marker ='|', s=100, color='blue')
ax[1].scatter(2087,11, marker ='|', s=200, color='blue')
ax[1].scatter(2097,11, marker ='|', s=100, color='blue')

#HADGEM
ax[1].hlines(10,2055,2075, color='orange')
ax[1].scatter(2055,10, marker ='|', s=100, color='orange')
ax[1].scatter(2075,10, marker ='|', s=200, color='orange')
ax[1].scatter(2065,10, marker ='|', s=100, color='orange')

#CSIRO
ax[1].hlines(9,2080,2100, color='green')
ax[1].scatter(2080,9, marker ='|', s=100, color='green')
ax[1].scatter(2090,9, marker ='|', s=200, color='green')
ax[1].scatter(2100,9, marker ='|', s=100, color='green')

#IPSL
ax[1].hlines(8,2055,2075, color='red')
ax[1].scatter(2055,8, marker ='|', s=100, color='red')
ax[1].scatter(2065,8, marker ='|', s=200, color='red')
ax[1].scatter(2075,8, marker ='|', s=100, color='red')

#MIROC5
ax[1].hlines(7,2059,2079, color='purple')
ax[1].scatter(2059,7, marker ='|', s=100, color='purple')
ax[1].scatter(2069,7, marker ='|', s=200, color='purple')
ax[1].scatter(2079,7, marker ='|', s=100, color='purple')

#NORESM
ax[1].hlines(6,2068,2088, color='brown')
ax[1].scatter(2068,6, marker ='|', s=100, color='brown')
ax[1].scatter(2078,6, marker ='|', s=200, color='brown')
ax[1].scatter(2088,6, marker ='|', s=100, color='brown')

#MIROC5
ax[1].hlines(5,2044,2064, color='pink')
ax[1].scatter(2044,5, marker ='|', s=100, color='pink')
ax[1].scatter(2054,5, marker ='|', s=200, color='pink')
ax[1].scatter(2064,5, marker ='|', s=100, color='pink')

#CNRM_ESM2
ax[1].hlines(4,2061,2081, color='gray')
ax[1].scatter(2061,4, marker ='|', s=100, color='gray')
ax[1].scatter(2071,4, marker ='|', s=200, color='gray')
ax[1].scatter(2081,4, marker ='|', s=100, color='gray')

#CNRM_CM6
ax[1].hlines(3,2059,2079, color='olive')
ax[1].scatter(2059,3, marker ='|', s=100, color='olive')
ax[1].scatter(2069,3, marker ='|', s=200, color='olive')
ax[1].scatter(2079,3, marker ='|', s=100, color='olive')

#MRI
ax[1].hlines(2,2065,2085, color='cyan')
ax[1].scatter(2065,2, marker ='|', s=100, color='cyan')
ax[1].scatter(2075,2, marker ='|', s=200, color='cyan')
ax[1].scatter(2085,2, marker ='|', s=100, color='cyan')

#UKESM
ax[1].hlines(1,2029,2049, color='navy')
ax[1].scatter(2029,1, marker ='|', s=100, color='navy')
ax[1].scatter(2039,1, marker ='|', s=200, color='navy')
ax[1].scatter(2049,1, marker ='|', s=100, color='navy')


ax[1].set_xlim(1950,2100)
ax[1].set_yticks([11,10,9,8,7,6,5,4,3,2,1])#,['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'])
ax[1].set_yticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'])

#mod = np.linspace(0,10,1)
#year = np.linspace(2000,2100,1)
#plt.plot(year,mod)
#plt.hlines(1, 2020, 2040)
#plt.scatter(2030,1)
#plt.scatter(2020,1, marker ='|', s=200)
#plt.scatter(2040,1, marker ='|', s=200)
#plt.ylim()

#secax = ax[0].secondary_yaxis(1.0)
#secax.set_yticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'])

#ax[1].set_yticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'], rotation=0, fontsize = 22)

ax[0].plot(CESM_time.year,CESM_time.TT,'--',label='CESM', linewidth=1.2)
ax[0].plot(CNRM_ESM2_time.year,CNRM_ESM2_time.TT,'--',label='CNRM-ESM2', linewidth=1.2)
ax[0].plot(CNRM_CM6_time.year,CNRM_CM6_time.TT,'--',label='CNRM-CM6', linewidth=1.2)
ax[0].plot(MRI_time.year, MRI_time.TT,'--',label='MRI', linewidth=1.2)
ax[0].plot(UKMO_time.year,UKMO_time.TT,'--',label='UKMO', linewidth=1.2, color='navy')
ax[0].legend(frameon=False, ncol=2)
ax[0].hlines(4,1950,2100, color='black', linewidth= 0.7)
ax[1].set_xlabel('Year', fontsize = 12)
ax[0].set_ylabel('Near-surface temperature anomalies [$^{\circ}$C]', fontsize=14)
sns.despine()

plt.savefig('Figures/temp_timeline_rol_new.pdf', bbox_inches='tight',dpi=300)

#"""


print('ACCSS:[',ACCESS_time.TT.sel(year=slice('2077','2091')).min(),ACCESS_time.TT.sel(year=slice('2077','2091')).max(),']',
      'HADGEM:[',HADGEM_time.TT.sel(year=slice('2055','2075')).min(),HADGEM_time.TT.sel(year=slice('2055','2075')).max(),']',
      'CSIRO:[',CSIRO_time.TT.sel(year=slice('2080','2091')).min(),CSIRO_time.TT.sel(year=slice('2080','2091')).max(),']',
      'IPSL:[',IPSL_time.TT.sel(year=slice('2055','2075')).min(),IPSL_time.TT.sel(year=slice('2055','2075')).max(),']',
      'MIROC5:[',MIROC5_time.TT.sel(year=slice('2059','2079')).min(),MIROC5_time.TT.sel(year=slice('2059','2079')).max(),']',
      'NORESM:[',NORESM_time.TT.sel(year=slice('2068','2088')).min(),NORESM_time.TT.sel(year=slice('2068','2088')).max(),']',
      'CESM:[',CESM_time.TT.sel(year=slice('2044','2064')).min(),CESM_time.TT.sel(year=slice('2044','2064')).max(),']',
      'CNRM_ESM2:[',CNRM_ESM2_time.TT.sel(year=slice('2061','2081')).min(),CNRM_ESM2_time.TT.sel(year=slice('2061','2081')).max(),']',
      'CNRM_CM6:[',CNRM_CM6_time.TT.sel(year=slice('2059','2079')).min(),CNRM_CM6_time.TT.sel(year=slice('2059','2079')).max(),']',
      'MRI:[',MRI_time.TT.sel(year=slice('2065','2085')).min(),MRI_time.TT.sel(year=slice('2065','2085')).max(),']',
      'UKESM:[',UKMO_time.TT.sel(year=slice('2029','2049')).min(),UKMO_time.TT.sel(year=slice('2029','2049')).max(),']')

"""
>> output from terminal:
ACCSS:[(3.47513016)(4.18731111) ] 
HADGEM:[(3.40786517)(4.47178334) ] 
CSIRO:[(3.35052158)(3.99524498) ] 
IPSL:[(3.40198087)(4.52394821) ] 
MIROC5:[(3.41014837)(4.75877675) ] 
NORESM:[(3.28768252)(4.71527829) ] 
CESM:[(3.42487348)(4.50217443) ] 
CNRM_ESM2:[(3.39792152)(4.89087548) ] <--- størst 
CNRM_CM6:[(3.31723318)(4.8508086) ] 
MRI:[(3.50770828)(4.64107507) ] 
UKESM:[(3.07230533)(4.66408786) ] <-- minst
"""