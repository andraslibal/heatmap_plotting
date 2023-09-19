import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N_values = [48,207,572,864,1216,1512,1794,2150]
fpin_values =[0.0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1.0,1.125,1.25,1.375,1.5,1.625,1.75,1.875,2.0,2.125,2.25,2.375,2.5,2.625,2.75,2.875,3.0,3.125,3.25,3.375, 3.5,3.625,3.75,3.875,4.0,4.125,4.25,4.375,4.5]

SX = 36.0
SY = 36.0

imax = len(N_values)
jmax = len(fpin_values) 
vx_data = np.zeros((imax,jmax))
vy_data = np.zeros((imax,jmax))

i = imax-1
i_array = []
j_array = []

for N in N_values:
    filename = 'dataforfig/N.{}'.format(N)
    filename2 = 'vydata/N.y.{}'.format(N)
    #print('Read in',filename)
    fpread, vxread = np.loadtxt(filename,unpack=True)
    fpread2, vyread = np.loadtxt(filename2,unpack=True)
    for j in range(len(fpread)):
        vx_data[i][j] = vxread[j]
    for j in range(len(fpread2)):
        vy_data[i][j] = vyread[j]

    i_array.append(i)
    i = i - 1

x_labels_decimation = 4

for j in range(len(fpread)):
    if j%x_labels_decimation==0:
        j_array.append(j)

fp_labels = []
j = 0
for fpin_value in fpin_values:
    if j%x_labels_decimation==0:
        fp_labels.append('{}'.format(fpin_value))
    j = j + 1


rho_labels = []
for N_value in N_values:
    rho_labels.append('{:.2}'.format(N_value/SX/SY))


print('Rho labels = ',rho_labels)


colors = [ "#053061", "#2166AC", "#4393C3", "#92c5de", "#d1e5f0" , "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]
values = [ -0.025 ,    -0.02,     -0.015,    -0.01,     -0.005   ,   0.0,      0.015,     0.03,     0.045,     0.06,     0.075]
norm = mpl.colors.Normalize(vmin=min(values), vmax=max(values))  
normed_vals = norm(values)
cmap = LinearSegmentedColormap.from_list("mypalette", list(zip(normed_vals, colors)), N=1000) 

heatmap = plt.imshow(vx_data, cmap = cmap, norm = norm, aspect = 2)
plt.xlabel(r'$F_p$', rotation = 0 )
plt.xticks(ticks = j_array, labels = fp_labels)
plt.ylabel(r'$\rho$', rotation = 0 )
plt.yticks(ticks = i_array, labels = rho_labels)
colorbar = plt.colorbar(heatmap, shrink = 0.45, aspect = 6)
colorbar.ax.set_title(r'$v_x$', pad = 10)
plt.savefig('Fig_vx.png',dpi = 300)

plt.close()


colors = [ "#053061", "#2166AC", "#4393C3", "#92c5de", "#d1e5f0" , "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]
values = [ -0.075 ,    -0.06,     -0.045,    -0.03,     -0.015   ,   0.0,      0.005,     0.01,     0.015,     0.02,     0.025]
norm = mpl.colors.Normalize(vmin=min(values), vmax=max(values))  
normed_vals = norm(values)
cmap = LinearSegmentedColormap.from_list("mypalette", list(zip(normed_vals, colors)), N=1000) 


heatmap2 = plt.imshow(vy_data, cmap = cmap, norm = norm, aspect = 2)
plt.xlabel(r'$F_p$', rotation = 0 )
plt.xticks(ticks = j_array, labels = fp_labels)
plt.ylabel(r'$\rho$', rotation = 0 )
plt.yticks(ticks = i_array, labels = rho_labels)
colorbar2 = plt.colorbar(heatmap2, shrink = 0.45, aspect = 6)
colorbar2.ax.set_title(r'$v_y$', pad = 10)
plt.savefig('Fig_vy.png',dpi = 300)