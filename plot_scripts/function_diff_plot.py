"""
Write a documentation for this function here ...
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

def diff_plot(variable_CMIP6, variable_CMIP5, lon, lat,
              #vmin,vmax,
              surf_height_data = None,
              add_contour_levels = False,
              contour_levels = None,
              cbar_title=None, 
              cmap_color = 'RdBu_r',
              savefig = True,
              title_plot = None,
              file_title = None):
    

    diff_var = variable_CMIP6 - variable_CMIP5

    proj = ccrs.LambertConformal(central_longitude=-35,
                                 central_latitude=65,
                                 standard_parallels=[35])
    fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'projection': proj})

    #divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter., vmax=vmax, cbar_title=None) 

    ax.add_feature(cartopy.feature.OCEAN.with_scale(
                    '50m'), zorder=1, facecolor='white')           
    ax.add_feature(cartopy.feature.COASTLINE.with_scale(
                    '50m'), zorder=1, edgecolor='black')
    ax.set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())
    
    cont = ax.pcolormesh(lon, lat, diff_var.values,   
                                        transform=ccrs.PlateCarree(),
                                        cmap=cmap_color)#, vmin=vmin, vmax=vmax)
    #remove outer box of the plot 
    fig.patch.set_visible(False)
    ax.axis('off')


    fig.canvas.draw()
    fig.tight_layout(pad=0.01)

    plt.subplots_adjust(left=0.02, right=0.98, top=0.80, bottom=0.24)
    cbar = fig.colorbar(cont, ax=ax, shrink=0.96, orientation ='vertical')
    cbar.set_label(
        cbar_title, fontsize=20)
    plt.title(title_plot, fontsize=20)
    
    #add contour levels of 2000m and 3000m
    
    if add_contour_levels == True:
        plt.contour(lon,lat,
                    surf_height_data, 
                    contour_levels,
                    transform=ccrs.PlateCarree(),
                    colors='black',linestyles = 'dashed', alpha=0.7, linewidths=0.8)

    plt.show()
    
    
    if add_contour_levels == True:
        fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/contour/'+file_title+'_contour''.pdf',bbox_inches='tight',dpi=300)
        
    if add_contour_levels == False:
        fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/4_deg_spatial_plots/'+file_title+'.pdf',bbox_inches='tight',dpi=300)