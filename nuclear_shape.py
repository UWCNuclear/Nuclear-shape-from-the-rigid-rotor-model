# Generate Shape of Nucleus

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from scipy.special import sph_harm
import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.colors as mcolors

# Define Constants

Z = 38      # Atomic number
A = 82      # Atomic mass number

r0 = 1.2    

# Average Radius
R_ave = r0*pow(A, 1/3)      # (fm)
R_ave2 = 0.0144*pow(A, 2/3) # (b)


# Deformation paramteters

Q0 = 0 # Intrinsic Quadrupole moment (input value)

beta = (np.sqrt(5*np.pi)/3)*(Q0/(Z*R_ave2))

# Calculating Surface

# R_surf(theta,phi)=R_ave()*(1+beta*Y20(theta,phi))

## Define angles
theta = np.linspace(0, np.pi, 51)
phi = np.linspace(0, 2*np.pi, 51)

(Theta, Phi) = np.meshgrid(theta, phi)


## Calculate Spherical Harmonic Y20
l = 2
m = 0

Y20 = abs(sph_harm(m, l, Phi, Theta))   # Spherical Harmonic from scipy          
y20 = (1/4)*np.sqrt(5/np.pi)*(3*pow(np.cos(Theta),2)-1) # Spherical Harmonic from formula

## Calculate R_surf
#R_surf = R_ave*(1 + beta*Y20)
R_surf = R_ave*(1 + beta*y20)



## Cartesian Cooridnates

x = R_surf*np.sin(Theta)*np.cos(Phi)
y = R_surf*np.sin(Theta)*np.sin(Phi)
z = R_surf*np.cos(Theta)


# Plot surface

## Surface color map and gradient
cmap = plt.get_cmap('viridis')
levels = 8
cmap= plt.cm.get_cmap("afmhot_r", levels+1)



fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot((111), projection='3d')
ax.plot_surface(
                x, y, z, 
                rstride=1, 
                cstride=1, 
                cmap=plt.get_cmap('viridis'),
                linewidth=0.2,
                edgecolors='k',
                alpha=1
                )



ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.set_facecolor('white')
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.line.set_visible(False)
#ax.xaxis.pane.grid(False)

ax.xaxis.pane.set_edgecolor('r')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

ax.set_xlim3d(-6,6)
ax.set_ylim3d(-6,6)
ax.set_zlim3d(-6,6)

ax.set_box_aspect((1,1,1))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

# Show Grid
ax.grid(False)
# Hide the axes
ax.axis('off')

# Customize the view angle so it's easier to understand the plot.
#ax.view_init(elev=0, azim=0.)






'''
# 2D Contour

x1D = (R_surf*np.sin(Theta)*np.cos(Phi)).flatten()
y1D = (R_surf*np.sin(Theta)*np.sin(Phi)).flatten()
z1D = (R_surf*np.cos(Theta)).flatten()


print(x1D)
ax2 = fig.add_subplot((122))

print(x1D)
triang = tri.Triangulation(x1D, y1D)
ax2.tricontour(triang, z1D, cmap=plt.cm.CMRmap)


#ax2.contourf(
             x, y, z, 
             zdir='x', 
             offset=-6, 
             levels=8, 
             cmap='viridis_r'
             )



#ax2.contour(
            x, y, z, 
            zdir='x', 
            offset=-6, 
            levels=8, 
            colors='k', 
            linewidths=0.2
            )   



ax2.set_aspect('equal', adjustable='box')
#ax2.axis('off')
'''
plt.show()