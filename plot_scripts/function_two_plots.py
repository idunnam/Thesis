"""
The function allows you to plot two map plots side by side with a shared colorbar. 


var_left: dataarray
    
var_right: dataarray

lon: dataarray 

lat: datarray

vmin: int 
    specifies the minimum value of the colour bar

vcenter: int 
    specifies the center value of the colour bar

vmax: int 
    specifies the maximum value of the colour bar

title_fig_l = 'left figure': str, optional 

title_fig_r = 'right figure': str, optional

fontsize_title_fig = 16: int, optional 

cbar_title = None: str, optional

cmap_color = 'RdBu_r', optional
    
suptitle = 'str', optional    

savefig: bool, optional
    if True (default) figure will be saved, otherwise figure is only showed

file_title = None: str, optional 
   
"""

import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy

plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 20})


def two_plots(var_left, var_right, lon, lat, 
              vmin,vmax,
              surf_height_data = None,
              add_contour_levels = False,
              contour_levels = None,
              title_fig_l = 'left figure',  
              title_fig_r = 'right figure',
              fontsize_title_fig = 16,
              cbar_title = None , cmap_color = 'RdBu_r', 
              suptitle= None,
              #savefig = True,
              file_title = None):
    
    proj = ccrs.LambertConformal(central_longitude=-35,
                                 central_latitude=65,
                                 standard_parallels=[35])

    fig, axes = plt.subplots( ncols=2, figsize=(8, 10), subplot_kw={'projection': proj})

    ax = axes.ravel().tolist()

    for i in [0,1]:
        ax[i].add_feature(cartopy.feature.OCEAN.with_scale(
                     '50m'), zorder=1, facecolor='white')           
        ax[i].add_feature(cartopy.feature.COASTLINE.with_scale(
                     '50m'), zorder=1, edgecolor='black')
        ax[i].set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())
    
        
    #divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
    #divnorm=colors(vmin=vmin, vcenter=vcenter, vmax=vmax)
    
    #CMIP5 model mean
    cont = ax[0].pcolormesh(lon, lat, var_left,   
                                        transform=ccrs.PlateCarree(),
                                        cmap=cmap_color, vmin=vmin, vmax=vmax)#, norm=divnorm)
    if add_contour_levels == True:
        ax[0].contour(lon,lat,
                    surf_height_data, 
                    contour_levels,
                    transform=ccrs.PlateCarree(),
                    colors='black',linestyles = 'dashed', alpha=0.7, linewidths=0.8)
    #CMIP6 model mean
    cont2 = ax[1].pcolormesh(lon, lat, var_right,   
                                        transform=ccrs.PlateCarree(),
                                        cmap=cmap_color, vmin=vmin, vmax=vmax)#, norm=divnorm)
    
    plt.rcParams.update({
    "text.usetex": True,
    "font.family": 'DejaVu Sans',
    "font.serif": ["Computer Modern Roman"]})

    ax[0].set_title(title_fig_l, fontsize= fontsize_title_fig)
    #ax[0].set_fontname("Computer Modern Roman")
    ax[1].set_title(title_fig_r, fontsize= fontsize_title_fig)



    #remove outer box of the plot 
    fig.patch.set_visible(False)
    ax[0].axis('off')
    ax[1].axis('off')

    fig.canvas.draw()
    fig.tight_layout(pad=0.01)
    fig.tight_layout(pad=0.01)
    
   

    plt.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.24)
    cbar = fig.colorbar(cont2, ax=ax, shrink=0.7, orientation ='vertical')
    cbar.set_label(cbar_title, fontsize=20)

    plt.suptitle(suptitle, fontsize = 20, y=0.95, x=0.40)
    
    if add_contour_levels == True:
        ax[1].contour(lon,lat,
                    surf_height_data, 
                    contour_levels,
                    transform=ccrs.PlateCarree(),
                    colors='black',linestyles = 'dashed', alpha=0.7, linewidths=0.8)

    plt.show()
    
    
    if add_contour_levels == True:
        fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/contour/'+file_title+'contour.pdf',bbox_inches='tight',dpi=300)
        
    if add_contour_levels == False:
        fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/'+file_title+'.pdf',bbox_inches='tight',dpi=300)
        
    