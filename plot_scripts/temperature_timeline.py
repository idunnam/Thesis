import xarray as xr 
import matplotlib.pyplot as plt 
import numpy as np


#== import seasonal amonalies ==#
#seasonal_anomaly/ACCESS_anomaly_JJA.nc
#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_JJA.nc')
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA_cloud.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CSIRO_anomaly_JJA.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/IPSL_anomaly_JJA.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MIROC5_anomaly_JJA.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/NORESM_anomaly_JJA.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CESM_anomaly_JJA.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_JJA.nc')
CNRM_CM6= xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_JJA.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_JJA.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_JJA.nc')


cmip5 = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]
cmip5_name = ('ACCESS', 'HADGEM', 'CSIRO', 'IPSL', 'MIROC5','NORESM')

cmip6 = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]
cmip6_name = ('CESM', 'CNRM_ESM2', 'CNRM_CM6', 'MRI', 'UKMO')




#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod)

TT_CMIP5     = []
for i in range(len(cmip5)):
    TT_CM5      = cmip5[i].TT.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    
TT_CMIP5     = model_mean(TT_CMIP5)


TT_CMIP6     = []
for i in range(len(cmip6)):
    TT_CM6      = cmip6[i].TT.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP6.append(TT_CM6)
    
TT_CMIP6     = model_mean(TT_CMIP6)

#STD
TT_CMIP5_std = np.std(TT_CMIP5)
TT_CMIP5_std = np.round(TT_CMIP5_std)

TT_CMIP6_std = np.std(TT_CMIP6)
TT_CMIP6_std = np.round(TT_CMIP6_std)

"""
#for k in cmip5:
#    plt.plot(k.year,k.TT.mean(dim=['X10_105','Y21_199']), '-', alpha = 0.8)
plt.plot(ACCESS.year, TT_CMIP5, color='orange', label= 'CMIP5 - model mean')
#plt.fill_between(ACCESS.year,TT_CMIP5 + TT_CMIP5_std, TT_CMIP5 -TT_CMIP5_std, alpha=0.5, color='orange')
#plt.legend(cmip5_name)
plt.title('Seasonal (JJA) Near-surface temperature')
plt.xlabel('Year')
plt.ylabel('Near-surface temperature [$^{\circ}$C]')
#plt.savefig('tim.png')



#for j in cmip6:
#     plt.plot(j.year,j.TT.mean(dim=['X10_105','Y21_199']), '--', alpha=0.8)
plt.plot(ACCESS.year, TT_CMIP6, '--',color='blue', label='CMIP6 model mean')
#plt.fill_between(ACCESS.year,TT_CMIP6 + TT_CMIP6_std, TT_CMIP6 -TT_CMIP6_std, alpha=0.5, color='blue')
#plt.legend(cmip6_name)
plt.legend(loc='upper left')
plt.title('Seasonal (JJA) Near-surface temperature')
plt.xlabel('Year')
plt.ylabel('Near-surface temperature [$^{\circ}$C]')

plt.savefig('timeline.png')
"""
#"""
##========== TT- timeline CMIP5 CMIP6 side-by-side ================
fig, ax = plt.subplots(1,2, figsize =(30,10))
for k in cmip5:
    ax[0].plot(k.year,k.TT.mean(dim=['X10_105','Y21_199']), '-', alpha = 0.8)
ax[0].plot(ACCESS.year, TT_CMIP5, color='black')
#ax[0].fill_between(ACCESS.year,TT_CMIP5 + TT_CMIP5_std, TT_CMIP5 -TT_CMIP5_std, alpha=0.5, color='grey')
ax[0].legend(cmip5_name)
ax[0].set_title('CMIP5 - Seasonal (JJA) Near-surface temperature',fontsize = 18)
ax[0].set_xlabel('Year',fontsize = 12)
ax[0].set_ylabel('Near-surface temperature [$^{\circ}$C]',fontsize = 12)
ax[0].set_ylim(-3,10)

for j in cmip6:
     ax[1].plot(j.year,j.TT.mean(dim=['X10_105','Y21_199']), '-', alpha=0.8)
ax[1].plot(ACCESS.year, TT_CMIP6, '-',color='black')
#ax[1].fill_between(ACCESS.year,TT_CMIP6 + TT_CMIP6_std, TT_CMIP6 -TT_CMIP6_std, alpha=0.5, color='grey')
ax[1].legend(cmip6_name)
#ax[1].legend(loc='upper left')
ax[1].set_title('CMIP6 - Seasonal (JJA) Near-surface temperature',fontsize = 18)
ax[1].set_xlabel('Year',fontsize = 12)
ax[1].set_ylabel('Near-surface temperature [$^{\circ}$C]',fontsize = 12)
ax[1].set_ylim(-3,10)

plt.savefig('Figures/timeline_JJA_side_by_side.png')
#========================================================
fig,ax = plt.subplots(1,2, figsize = (20,10),gridspec_kw={'width_ratios': [3, 1]})


ax[1].boxplot([TT_CMIP5[-30:],TT_CMIP6[-30:]])
ax[1].set_xticklabels(['CMIP5','CMIP6'])
ax[1].set_ylim(-3,9)
ax[1].set_title('(2071-2100)', fontsize = 18)

ax[0].plot(ACCESS.year, TT_CMIP5, color='orange', label= 'CMIP5 - model mean')
ax[0].fill_between(ACCESS.year,TT_CMIP5 + TT_CMIP5_std, TT_CMIP5 -TT_CMIP5_std, alpha=0.5, color='orange')
ax[0].plot(ACCESS.year, TT_CMIP6, '--',color='black', label='CMIP6 model mean')
ax[0].fill_between(ACCESS.year,TT_CMIP6 + TT_CMIP6_std, TT_CMIP6 -TT_CMIP6_std, alpha=0.5, color='grey')
#ax[0].legend(loc='upper left')
ax[0].set_title('Seasonal (JJA) Near-surface temperature',fontsize = 18)
ax[0].set_xlabel('Year', fontsize = 12)
ax[0].set_ylabel('Near-surface temperature [$^{\circ}$C]', fontsize = 12)
ax[0].set_ylim(-3,9)

plt.savefig('Figures/Seasonal_temperature_timeline_boxplot.png')
print('SEASONAL:','CMIP5 in 2100:',TT_CMIP5[-1].values,'CMIP6 in 2100:',TT_CMIP6[-1].values)
#"""

"""
SEASONAL:
CMIP5 in 2100: 5.2749132401609975 
CMIP6 in 2100: 7.234658144621008
"""



#=#=#=#=#==#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=# 
#======================= ANNUAL ======================================= #
#== import seasonal amonalies ==#
#seasonal_anomaly/ACCESS_anomaly_JJA.nc
#CMIP5 models
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/ACCESS_anomaly_annual.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/HADGEM_anomaly_annual.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CSIRO_anomaly_annual.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/IPSL_anomaly_annual.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/MIROC5_anomaly_annual.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/NORESM_anomaly_annual.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CESM_anomaly_annual.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CNRM_ESM2_anomaly_annual.nc')
CNRM_CM6= xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/CNRM_CM6_anomaly_annual.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/MRI_anomaly_annual.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_annual/UKMO_anomaly_annual.nc')


cmip5 = [ACCESS, HADGEM, CSIRO, IPSL, MIROC5, NORESM]
cmip5_name = ['ACCESS', 'HADGEM', 'CSIRO', 'IPSL', 'MIROC5','NORESM','Model mean']

cmip6 = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]
cmip6_name = ['CESM', 'CNRM_ESM2', 'CNRM_CM6', 'MRI', 'UKESM', 'Model mean']



#=== CMIP5 component model mean ===
def model_mean(mod):
    return sum(mod)/ len(mod)

TT_CMIP5     = []
for i in range(len(cmip5)):
    TT_CM5      = cmip5[i].TT.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP5.append(TT_CM5)
    
TT_CMIP5     = model_mean(TT_CMIP5)


TT_CMIP6     = []
for i in range(len(cmip6)):
    TT_CM6      = cmip6[i].TT.mean(dim=["X10_105","Y21_199"])
    
    TT_CMIP6.append(TT_CM6)
    
TT_CMIP6     = model_mean(TT_CMIP6)

#STD
TT_CMIP5_std = np.std(TT_CMIP5)
print(TT_CMIP5_std)
TT_CMIP5_std = np.round(TT_CMIP5_std)

TT_CMIP6_std = np.std(TT_CMIP6)
TT_CMIP6_std = np.round(TT_CMIP6_std)
"""

##========== TT- timeline CMIP5 CMIP6 side-by-side ================
fig, ax = plt.subplots(1,2, figsize =(30,10))
for k in cmip5:
    ax[0].plot(k.year,k.TT.mean(dim=['X10_105','Y21_199']), '-', alpha = 0.8)
ax[0].plot(ACCESS.year, TT_CMIP5, color='black')
#ax[0].fill_between(ACCESS.year,TT_CMIP5 + TT_CMIP5_std, TT_CMIP5 -TT_CMIP5_std, alpha=0.5, color='grey')
ax[0].legend(cmip5_name)
ax[0].set_title('CMIP5 - Annual Near-surface temperature',fontsize = 18)
ax[0].set_xlabel('Year',fontsize = 12)
ax[0].set_ylabel('Near-surface temperature [$^{\circ}$C]',fontsize = 12)
ax[0].set_ylim(-3,11)

for j in cmip6:
     ax[1].plot(j.year,j.TT.mean(dim=['X10_105','Y21_199']), '-', alpha=0.8)
ax[1].plot(ACCESS.year, TT_CMIP6, '-',color='black')
#ax[1].fill_between(ACCESS.year,TT_CMIP6 + TT_CMIP6_std, TT_CMIP6 -TT_CMIP6_std, alpha=0.5, color='grey')
ax[1].legend(cmip6_name)
#ax[1].legend(loc='upper left')
ax[1].set_title('CMIP6 - Annual Near-surface temperature',fontsize = 18)
ax[1].set_xlabel('Year',fontsize = 12)
ax[1].set_ylabel('Near-surface temperature [$^{\circ}$C]',fontsize = 12)

plt.savefig('Figures/timeline_ANNUAL_side_by_side.png')
#============================================#


#========================= Filled timelline with boxplot ====================
fig,ax = plt.subplots(1,2, figsize = (20,10),gridspec_kw={'width_ratios': [3, 1]})


ax[1].boxplot([TT_CMIP5[-30:],TT_CMIP6[-30:]])
ax[1].set_xticklabels(['CMIP5','CMIP6'])
ax[1].set_ylim(-3,9)
ax[1].set_title('(2071-2100)',fontsize = 18)

ax[0].plot(ACCESS.year, TT_CMIP5, color='brown', label= 'CMIP5 - model mean')
ax[0].fill_between(ACCESS.year,TT_CMIP5 + TT_CMIP5_std, TT_CMIP5 -TT_CMIP5_std, alpha=0.5, color='brown')
ax[0].plot(ACCESS.year, TT_CMIP6, '--',color='black', label='CMIP6 model mean')
ax[0].fill_between(ACCESS.year,TT_CMIP6 + TT_CMIP6_std, TT_CMIP6 -TT_CMIP6_std, alpha=0.5, color='grey')
ax[0].legend(loc='upper left')
ax[0].set_title('Annual Near-surface temperature',fontsize = 18)
ax[0].set_xlabel('Year',fontsize = 12)
ax[0].set_ylabel('Near-surface temperature [$^{\circ}$C]',fontsize = 12)
ax[0].set_ylim(-3,9)

plt.savefig('Figures/Annual_temperature_timeline_boxplot.png')
print('ANNUAL:''CMIP5 in 2100:',TT_CMIP5[-1].values,'CMIP6 in 2100:',TT_CMIP6[-1].values)

"""
"""
CMIP5 in 2100: 5.8197954181416165 
CMIP6 in 2100: 7.24926913910457
"""

""""

#======================= PLOT TAS[4,5] SCATTER PLOT TIMELINE ===================

ACCESS_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/ACCESS_1_deg_anomalies.nc')
#HADGEM_cloud_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies_cloud.nc')
HADGEM_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/HADGEM_1_deg_anomalies.nc')
CSIRO_1_deg  = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CSIRO_1_deg_anomalies.nc')
IPSL_1_deg   = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/IPSL_1_deg_anomalies.nc')
MIROC5_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/MIROC5_1_deg_anomalies.nc')
NORESM_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/NORESM_1_deg_anomalies.nc')

#CMIP6 models
CESM_1_deg      = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CESM_1_deg_anomalies.nc')
CNRM_ESM2_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CNRM_ESM2_1_deg_anomalies.nc')
CNRM_CM6_1_deg = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/CNRM_CM6_1_deg_anomalies.nc')
MRI_1_deg       = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/MRI_1_deg_anomalies.nc')
UKMO_1_deg      = xr.open_dataset('/projects/NS9600K/idunnam/src/1_deg_anomalies/UKMO_1_deg_anomalies.nc')
"""
############


plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"]})
#===================== PLOT temperature timeline + 20yr interval =========================
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/ACCESS_anomaly_JJA.nc')
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA_cloud.nc')
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA.nc')
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CSIRO_anomaly_JJA.nc')
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/IPSL_anomaly_JJA.nc')
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MIROC5_anomaly_JJA.nc')
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/NORESM_anomaly_JJA.nc')

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CESM_anomaly_JJA.nc')
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_JJA.nc')
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_JJA.nc')
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/MRI_anomaly_JJA.nc')
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/SEB_anomalies_seasonal/UKMO_anomaly_JJA.nc')


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
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/ACCESS_rol_4.nc')
HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_rol_4.nc')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/HADGEM_cloud_rol_4.nc')
CSIRO_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CSIRO_rol_4.nc')
IPSL_rol_4   = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/IPSL_rol_4.nc')
MIROC5_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MIROC5_rol_4.nc')
NORESM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/NORESM_rol_4.nc')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CESM_rol_4.nc')
CNRM_ESM2_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_ESM2_rol_4.nc')
CNRM_CM6_rol_4  = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/CNRM_CM6_rol_4.nc')
MRI_rol_4       = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/MRI_rol_4.nc')
UKMO_rol_4      = xr.open_dataset('/projects/NS9600K/idunnam/Thesis/src/rol_mean_3_5_deg/UKMO_rol_4.nc')

fig, ax = plt.subplots(2,1, figsize=(10,15),sharex=True, gridspec_kw={'height_ratios': [1.5, 1]})

ax[0].set_title('Near-surface temperature anomalies (1950-2100)')
ax[0].plot(ACCESS_time.year,ACCESS.TT.mean(dim=['X10_105','Y21_199']),label='ACCESS')
ax[0].plot(HADGEM_time.year,HADGEM.TT.mean(dim=['X10_105','Y21_199']), label='HADGEM')
ax[0].plot(CSIRO_time.year,CSIRO.TT.mean(dim=['X10_105','Y21_199']),label='CSIRO')
ax[0].plot(IPSL_time.year,IPSL.TT.mean(dim=['X10_105','Y21_199']),label='IPSL')
ax[0].plot(MIROC5_time.year,MIROC5.TT.mean(dim=['X10_105','Y21_199']),label='MIROC5')
ax[0].plot(NORESM_time.year,NORESM.TT.mean(dim=['X10_105','Y21_199']),label='NORESM')


"""
ax[1].boxplot([ACCESS_rol_4.year,
              HADGEM_rol_4.year,
              CSIRO_rol_4.year,
              IPSL_rol_4.year,
              MIROC5_rol_4.year,
              NORESM_rol_4.year,
              CESM_rol_4.year,
              CNRM_ESM2_rol_4.year,
              CNRM_CM6_rol_4.year,
              MRI_rol_4.year,
              UKMO_rol_4.year], vert=False ,widths=0.01)
"""
ax[1].boxplot([UKMO_rol_4.year,
              MRI_rol_4.year,
              CNRM_CM6_rol_4.year,
              CNRM_ESM2_rol_4.year,
              CESM_rol_4.year,
              NORESM_rol_4.year,
              MIROC5_rol_4.year,
              IPSL_ESM2_rol_4.year,
              CSIRO_CM6_rol_4.year,
              HADGEM_rol_4.year,
              ACCESS_rol_4.year], vert=False ,widths=0.01)
#secax = ax[0].secondary_yaxis(1.0)
#secax.set_yticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'])
#ax[1].set_yticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'])
ax[1].set_yticklabels(['UKESM','MRI','CNRM_CM6','CNRM_ESM2','CESM','NORESM','MIROC5','IPSL','CSIRO','HADGEM','ACCESS'])

ax[1].set_xlabel('Year')
ax[1].set_title('+4$^\circ$C Near-surface warming ($\pm$10years)')

ax[0].plot(CESM_time.year,CESM.TT.mean(dim=['X10_105','Y21_199']),'--',label='CESM')
ax[0].plot(CNRM_ESM2_time.year,CNRM_ESM2.TT.mean(dim=['X10_105','Y21_199']),'--',label='CNRM-ESM2')
ax[0].plot(CNRM_CM6_time.year,CNRM_CM6.TT.mean(dim=['X10_105','Y21_199']),'--',label='CNRM-CM6')
ax[0].plot(MRI_time.year, MRI.TT.mean(dim=['X10_105','Y21_199']),'--',label='MRI')
ax[0].plot(UKMO_time.year,UKMO.TT.mean(dim=['X10_105','Y21_199']),'--',label='UKMO')
ax[0].legend()
ax[0].set_xlabel('Year',fontsize = 22)
ax[0].set_ylabel('Near-surface temperature anomalies [$^{\circ}$C]',fontsize=22)
plt.savefig('Figures/temp_timeline_20yr.png')



#===================== PLOT rolling mean 4 plot timeline + STD =========================
ACCESS = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/ACCESS_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
HADGEM_cloud = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA_cloud.nc').mean(dim=['X10_105','Y21_199'])
HADGEM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/HADGEM_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
CSIRO  = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CSIRO_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
IPSL   = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/IPSL_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
MIROC5 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/MIROC5_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
NORESM = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/NORESM_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])

#CMIP6 models
CESM      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CESM_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
CNRM_ESM2 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CNRM_ESM2_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
CNRM_CM6 = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/CNRM_CM6_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
MRI       = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/MRI_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])
UKMO      = xr.open_dataset('/projects/NS9600K/idunnam/src/SEB_anomalies_seasonal/UKMO_anomaly_JJA.nc').mean(dim=['X10_105','Y21_199'])


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
ACCESS_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/ACCESS_rol_4.nc').mean(dim='year')
HADGEM_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/HADGEM_rol_4.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('/projects/NS9600K/idunnam/src/rol_mean_3_5_deg/HADGEM_cloud_rol_4.nc').mean(dim='year')
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

fig, ax = plt.subplots(1,2, figsize=(20,10),sharey=True,gridspec_kw={'width_ratios': [2, 1]})

ax[0].plot(ACCESS_time.year,ACCESS_time.TT,label='ACCESS')
ax[0].plot(HADGEM_time.year,HADGEM_time.TT, label='HADGEM')
ax[0].plot(CSIRO_time.year,CSIRO_time.TT,label='CSIRO')
ax[0].plot(IPSL_time.year,IPSL_time.TT,label='IPSL')
ax[0].plot(MIROC5_time.year,MIROC5_time.TT,label='MIROC5')
ax[0].plot(NORESM_time.year,NORESM_time.TT,label='NORESM')

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
ax[1].set_xticklabels(['ACCESS','HADGEM','CSIRO','IPSL','MIROC5','NORESM','CESM','CNRM-ESM2','CNRM-CM6','MRI','UKESM'], rotation=45)

ax[0].plot(CESM_time.year,CESM_time.TT,'--',label='CESM')
ax[0].plot(CNRM_ESM2_time.year,CNRM_ESM2_time.TT,'--',label='CNRM-ESM2')
ax[0].plot(CNRM_CM6_time.year,CNRM_CM6_time.TT,'--',label='CNRM-CM6')
ax[0].plot(MRI_time.year, MRI_time.TT,'--',label='MRI')
ax[0].plot(UKMO_time.year,UKMO_time.TT,'--',label='UKMO')
ax[0].legend()
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Near-surface temperature anomalies')
plt.savefig('Figures/temp_timeline_std.png')

