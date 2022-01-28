"""File for getting 2D maps of temporal trends of a certain variable. You need to extract the variable, e.g. ds['TT'] first, before doing the trend.
"""
import xarray as xr
import pandas as pd
import numpy as np

import cartopy.crs as ccrs
import cartopy.feature

import matplotlib.pyplot as plt
import seaborn as sns


ds = xr.open_dataset('/projects/NS9600K/shofer/Paper_CMIP6/MAR/monthly_all_072021/MARv3.9-ACCESS13-1994.nc',decode_times=False)

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 20})

proj = ccrs.LambertConformal(central_longitude=-35,
                             central_latitude=65,
                             standard_parallels=[35])
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(
    8, 10), subplot_kw={'projection': proj})

# The commented part is where you would plot your MAR data etc
# You need to uncomment the line below and edit to the variable you want to plot :)
cont = axes.pcolormesh(ds['LON'], ds['LAT'], ds['SH'].values,
                                transform=ccrs.PlateCarree(), vmin=0, vmax=3500,
                                cmap=sns.color_palette("mako", as_cmap=True))
axes.add_feature(cartopy.feature.OCEAN.with_scale(
            '50m'), zorder=1, facecolor='white')
axes.add_feature(cartopy.feature.COASTLINE.with_scale(
            '50m'), zorder=1, edgecolor='black')
axes.set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())

axes.gridlines()

#geo_axes = plt.axes(projection=cartopy.crs.PlateCarree())

# Wait for figure to be drawn before applying the tight layout
fig.tight_layout(pad=0.1)
cbar = fig.colorbar(cont, ax=axes, shrink=0.96, orientation ='vertical')
cbar.set_label('Surface Height [m]', fontsize=20)

plt.contour(ds['LON'],ds['LAT'],
                    ds.SH, 
                    [500,1000,1500,2000,2500,3000,3500],
                    transform=ccrs.PlateCarree(),
                    colors='black',linestyles = 'dashed', alpha=0.7, linewidths=0.8)

    
fig.patch.set_visible(False)
axes.axis('off')

plt.savefig('domain_test.pdf',bbox_inches='tight',dpi=300)
