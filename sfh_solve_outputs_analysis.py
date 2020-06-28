import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import sys as sys
from matplotlib.gridspec import GridSpec
from astropy.io import fits
import matplotlib.colors as colors
import matplotlib.patches as patches
from matplotlib.path import Path
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon

b = [[[1.009,0.252,0.212,0.757,1.822,2.237,2.082,1.269,1.09,1.017,1.009], [0.568,0.177,-0.972,-2.63,-3.739,-3.674,-3.374,-1.05,-0.254,0.542,0.568]],
    [[-0.582,0.394,0.475,0.564,1.069,0.995,-0.143,-0.314,-0.59,-0.582], [2.878,1.416,1.743,2.63,3.962,4.484,4.471,3.531,2.865,2.878]],
    [[-0.992,-0.366,-0.1,0.212,0.391,-0.593,-0.699,-0.927,-1.008,-0.992], [-3.87,-3.87,-0.189,0.594,1.403,2.865,2.317,-1.207,-3.87,-3.87]],
    [[-0.145,-0.314,-0.6,-0.684,-0.937,-1.307,-1.274,-0.785,-0.145], [4.494,3.556,2.852,2.354,-1.223,-1.194,1.562,4.523,4.494]],
    [[0.484,0.569,1.079,1.163,1.196,1.222,1.32,0.589,0.478,0.484], [1.752,2.595,3.933,3.668,3.587,2.606,0.725,0.39,1.717,1.752]],
    [[1.329,1.435,2.061,2.549,3.484,2.24,2.093,1.248,1.101,1.02,1.329,1.329], [0.712,0.111,-1.546,-2.121,-2.747,-3.661,-3.387,-0.959,-0.267,0.568,0.686,0.712]],
    [[1.271,1.365,2.783,3.224,1.28,1.271], [4.079,0.719,-1.84,2.014,4.079,4.079]]]
vertex_list = []
for item in b:
    vertex_list.append(np.array(item).T)

file_type = 'png'

def CMD_comaprison_plot(colour1, mag1, colour2, mag2, colour3, mag3, vertex_list, region, file_type):
    distance_modulus = 18.9
    scale = 2
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rcParams.update({'font.size':scale*18})
    fig = plt.figure(figsize=(scale*16,scale*7.45))
    gs = GridSpec(1, 4, figure=fig, wspace=0)
    #gs.tight_layout(fig, w_pad=0.)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax4 = fig.add_subplot(gs[3])
    axis_list = [ax1, ax2, ax3, ax4]

    xbinsize = 0.01
    ybinsize = 0.03
    xbins = np.arange( start = -2, stop = 3.5+xbinsize, step = xbinsize)
    ybins = np.arange( start = 13.-distance_modulus, stop = 24-distance_modulus+ybinsize, step = ybinsize)
    density1 = ax1.hist2d(colour1, mag1, bins=[xbins, ybins], cmap='magma', norm=colors.LogNorm(vmin=1), rasterized = True)
    density2 = ax2.hist2d(colour2, mag2, bins=[xbins, ybins], cmap='magma', norm=colors.LogNorm(vmin=1), rasterized = True)
    density3 = ax3.hist2d(colour3, mag3, bins=[xbins, ybins], cmap='magma', norm=colors.LogNorm(vmin=1), rasterized = True)
    ax4.imshow(density1[0].T-density2[0].T-density3[0].T, extent=[np.min(xbins), np.max(xbins), np.min(ybins), np.max(ybins)], origin='lower', cmap='seismic_r', norm=colors.DivergingNorm(vcenter=0.), rasterized=True)

    xy = (-1.6,-4.1)
    ax1.annotate('Observed', xy)
    ax2.annotate('Galaxy model', xy)
    ax3.annotate('Field model', xy)
    ax4.annotate('Residuals', xy)

    colour_polygons = 'cyan'
    for pol in vertex_list:
        for axs in axis_list:
            polygon = Polygon(pol, edgecolor=colour_polygons, fill=False, linewidth=scale*1.2, ls='--')
            axs.add_patch(polygon)

    for axs in axis_list:
        axs.minorticks_on()
        axs.tick_params(which='both', direction='inout')
        axs.tick_params(which='major', length=scale*6)
        axs.tick_params(which='minor', length=scale*3)
        axs.set_xlabel('$(g-i)_0$')
        axs.set_ylabel('$I_{0}$')
        axs.set_xlim((-2,3.5))
        axs.set_ylim((24-distance_modulus, 14.-distance_modulus))
        axs.autoscale(False)
        axs.label_outer()

    fig.savefig('/home/polmassana/Documents/PhD/SFH/Plots/CMD_comparison_plots/CMD_comparison_sfh_solve_%s.%s'%(region, file_type), bbox_inches='tight')
    plt.close()

for i in np.arange(1, 75):
    region =  str(int(i))
    observed_data = fits.getdata('/home/polmassana/Documents/PhD/SFH/SMC_test5_field/outputs/region_%s_CMD_abs.fits.gz'%(region))
    sfh_solve_data = np.loadtxt('/home/polmassana/Documents/PhD/SFH/SMC_test5_field/sfh_solve/%s/solution_cmd.out'%(region))
    sfh_solve_data_fld = np.loadtxt('/home/polmassana/Documents/PhD/SFH/SMC_test5_field/sfh_solve/%s/solution_fld.out'%(region))

    mag_obs = observed_data['I']
    colour_obs = observed_data['G'] - observed_data['I']
    mag_sfh = sfh_solve_data.T[1]
    colour_sfh = sfh_solve_data.T[0]
    mag_fld = sfh_solve_data_fld.T[1]
    colour_fld = sfh_solve_data_fld.T[0]

    CMD_comaprison_plot(colour_obs, mag_obs, colour_sfh, mag_sfh, colour_fld, mag_fld, vertex_list, region, file_type)
    print('Region '+region+' done.')
