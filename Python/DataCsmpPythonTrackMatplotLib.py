# python's matplotlib library :

import matplotlib.pyplot as plt

year = [1950,1920,1970,1980,1990]
pop = [2.5,2.7,3.6,4.4,5.1]

# Simple Plot
# ___________

# plt.plot(year,pop)
# plt.show()

# Note that calling show fucntion is mandatory to show your graph

# Scatter Plot
# ____________

# plt.scatter(year,pop)
# plt.show()

# To Create Logarithmic Scale on x-axis
# _____________________________________

# plt.xscale('log')
# plt.show()

# To learn about features and uses of histogram
# _____________________________________________

# help(plt.hist)

# Draw Histogram
# ______________

# y=[10,40,60,70,90,100,130,30]
# plt.hist(y,color='black',histtype='step',cumulative=True,density=True)
# plt.show()

# To Clean the plot
# _________________

# plt.clf()
# plt.show()

# formating plot
# ______________

# plt.xlabel('year')
# plt.ylabel ('population')
# plt.title('World Population')
# plt.yticks(
#     [0,2,4,6,8,10],
#     ['0','2B','4B','6B','8B','10B']
#     )
# plt.show()

# plt.text(15,7,'pak')
# plt.grid(True)
# plt.show()

