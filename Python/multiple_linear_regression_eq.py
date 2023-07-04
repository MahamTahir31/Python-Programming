import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

### Define the range of X1 and X2
X1 = np.arange(-10, 10, 0.5)
X2 = np.arange(-5, 5, 0.25)

# Create a grid of X1 and X2 values
X1, X2 = np.meshgrid(X1, X2)

# Compute the predicted values of Y cap for each combination of X1 and X2
Y_cap = -6.808 + 3.1478*X1 - 1.659*X2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add a scatter plot of X1, X2, and Y cap
ax.scatter(X1, X2, Y_cap, c='r', marker='o')

# Add a surface plot to visualize the regression plane
surf = ax.plot_surface(X1, X2, Y_cap, cmap='coolwarm', alpha=0.5)

# Set the axis labels
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y_cap')

# Show the plot
plt.show()


# Define the range of X1
##X1 = np.arange(-10, 10, 0.5)
##
### Compute the predicted values of Y cap for each X1
##Y_cap = -6.808 + 3.1478*X1 - 1.659*0
##
### Plot the regression line for X1
##plt.plot(X1, Y_cap, label='X2=0')
##
### Compute the predicted values of Y cap for each X1 while holding X2 constant at 2
##Y_cap = -6.808 + 3.1478*X1 - 1.659*2
##
### Plot the regression line for X1 while holding X2 constant at 2
##plt.plot(X1, Y_cap, label='X2=2')
##
### Compute the predicted values of Y cap for each X1 while holding X2 constant at -2
##Y_cap = -6.808 + 3.1478*X1 - 1.659*(-2)
##
### Plot the regression line for X1 while holding X2 constant at -2
##plt.plot(X1, Y_cap, label='X2=-2')
##
##plt.xlabel('X1')
##plt.ylabel('Y_cap')
##plt.legend()
##plt.show()


##import numpy as np
##import matplotlib.pyplot as plt

# Define the range of X2
X2 = np.arange(-5, 5, 0.25)

# Compute the predicted values of Y cap for each X2
Y_cap = -6.808 + 3.1478*0 - 1.659*X2

# Plot the regression line for X2
plt.plot(X2, Y_cap, label='X1=0')

# Compute the predicted values of Y cap for each X2 while holding X1 constant at 2
Y_cap = -6.808 + 3.1478*2 - 1.659*X2

# Plot the regression line for X2 while holding X1 constant at 2
plt.plot(X2, Y_cap, label='X1=2')

# Compute the predicted values of Y cap for each X2 while holding X1 constant at -2
Y_cap = -6.808 + 3.1478*(-2) - 1.659*X2

# Plot the regression line for X2 while holding X1 constant at -2
plt.plot(X2, Y_cap, label='X1=-2')

plt.xlabel('X2')
plt.ylabel('Y_cap')
plt.legend()
plt.show()




