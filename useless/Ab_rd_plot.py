from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
 
 
fig = plt.figure()
ax = fig.gca(projection='3d')
 
# Make data.
r = np.arange(0.05, 1, 0.01)
d = np.arange(0.5, 3, 0.01)
r, d = np.meshgrid(r, d)

# Z = np.sin(R)
Zr = (1/(1/d + r))*(2/3)
Zd = (1/(1/r + d))*(4/3)


# Plot the surface.
surf1 = ax.plot_surface(r, d, Zr, cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf2 = ax.plot_surface(r, d, Zd, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
 
# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)
 
plt.show()