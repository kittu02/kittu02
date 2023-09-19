#lab-14

import numpy as np
import matplotlib.tri as mtri
from matplotlib import gridspec
import matplotlib.pyplot as plt

# # Task 1: Using set_title() method
# # create data
# x = np.array([1,2,3,4,5])

# # making subplots
# fig, ax = plt.subplots(2,2)

# # set data with subplots and plot
# ax[0,0].plot(x,x)
# ax[0,1].plot(x,x*2)
# ax[1,0].plot(x,x*x)
# ax[1,1].plot(x*x*x)

# # set the title to subplots
# ax[0,0].set_title("Linear")
# ax[0,1].set_title("Double")
# ax[1,0].set_title("Sqaure")
# ax[1,1].set_title("Cube")

# # set spacing
# fig.tight_layout()
# plt.show()

# # Task 2: Using title.set_text() method
# # create data
# x = np.array([1,2,3,4,5])

# # making subplots
# fig, ax = plt.subplots(2,2)

# # set data with subplots and plot
# ax[0,0].plot(x,x)
# ax[0,1].plot(x,x*2)
# ax[1,0].plot(x,x*x)
# ax[1,1].plot(x*x*x)

# # set the title to subplots
# ax[0,0].title.set_text("Linear")
# ax[0,1].title.set_text("Double")
# ax[1,0].title.set_text("Sqaure")
# ax[1,1].title.set_text("Cube")

# # set spacing
# fig.tight_layout()
# plt.show()


# # Task 3: Using plt.gca().set_title() method
# # create data
# x=np.array([1, 2, 3, 4, 5])

# # making subplots
# fig, ax = plt.subplots(2, 2)

# # set data with subplots and plot
# title = ["Linear", "Double", "Square", "Cube"]
# y = [x, x*2, x*x, x*x*x]

# for i in range(4):
	
# 	# subplots
# 	plt.subplot(2, 2, i+1)
	
# 	# plotting (x,y)
# 	plt.plot(x, y[i])
	
# 	# set the title to subplots
# 	plt.gca().set_title(title[i])

# # set spacing
# fig.tight_layout()
# plt.show()


# # Task 4: Using plt.gca().title.set_text() method

# # create data
# x=np.array([1, 2, 3, 4, 5])
# # making subplots
# fig, ax = plt.subplots(2, 2)

# # set data with subplots and plot
# title = ["Linear","Double","Square","Cube"]
# y = [x, x*2, x*x, x*x*x]

# for i in range(4):
# 	# subplots
# 	plt.subplot(2, 2, i+1)
# 	# plotting (x,y)
# 	plt.plot(x, y[i])
# 	# set the title to subplots
# 	plt.gca().title.set_text(title[i])

# # set spacing
# fig.tight_layout()
# plt.show()

# # Task 5: reating random data by using random.randint 
# # making subplots objects
# fig, ax = plt.subplots(2, 2)
 
# # draw graph
# ax[0][0].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
# ax[0][1].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
# ax[1][0].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
# ax[1][1].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
 
# fig.suptitle(' Set a Single Main Title for All the Subplots ', fontsize=30)
# plt.show()



# # Task 6: creating data to plot our graph and using a marker
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 
# x1 = [1, 2, 3, 4, 5, 6]
# y1 = [45, 34, 30, 45, 50, 38]
# y2 = [36, 28, 30, 40, 38, 48]
 
# labels = ["student 1", "student 2"]
 
# # Add title to subplot
# fig.suptitle(' Student marks in different subjects ', fontsize=30)
# # Creating the sub-plots.
# l1 = ax1.plot(x1, y1, 'o-', color='g')
# l2 = ax2.plot(x1, y2, 'o-')
# fig.legend([l1, l2], labels=labels, loc="upper right")
# plt.subplots_adjust(right=0.9)
 
# plt.show()



# # Task 7: Using matplotlib.axes.Axes.axis() - method(1)
# # assign data
# x = np.asarray([0, 1, 2, 3, 0.5,
# 				1.5, 2.5, 1, 2,
# 				1.5])

# y = np.asarray([0, 0, 0, 0, 1.0,
# 				1.0, 1.0, 2, 2,
# 				3.0])

# triangles = [[0, 1, 4], [1, 5, 4],
# 			[2, 6, 5], [4, 5, 7],
# 			[5, 6, 8], [5, 8, 7],
# 			[7, 8, 9], [1, 2, 5],
# 			[2, 3, 6]]

# # depict illustration
# triang = mtri.Triangulation(x, y, triangles)
# z = np.cos(1.5 * x) * np.cos(1.5 * y)
	
# fig, axs = plt.subplots()
# axs.tricontourf(triang, z)
# axs.triplot(triang, 'go-', color ='white')

# # turn off the axes
# axs.set_axis_off()

# # assign title
# axs.set_title('Triangle illustration')

# plt.show()



# # Task 8: Using matplotlib.axes.Axes.set_axis_off() - method(2)
# # time series data
# geeksx = np.array([24.40, 110.25, 20.05,
#                 22.00, 61.90, 7.80,
#                 15.00])
 
# geeksy = np.array([24.40, 110.25, 20.05,
#                 22.00, 61.90, 7.80,
#                 15.00])
     
# # depict illustration   
# fig, ax = plt.subplots()
# ax.xcorr(geeksx, geeksy, maxlags = 6,
#         color ="green")
 
# # turn off the axes
# ax.set_axis_off()
 
# # assign title
# ax.set_title('Time series graph')
# plt.show()

# # Task 9: Using matplotlib.pyplot.axis() - method(3)
# # assigning x and y coordinates
# x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# y = []
 
# for i in range(len(x)):
#     y.append(max(0, x[i]))
 
# # depicting the visualization
# ax = plt.plot(x, y, color='green')
 
# # turn off the axes
# plt.axis('off')
 
# # displaying the title
# plt.title("ReLU function graph")
 
# plt.show()

# # Task 10: Create Different Subplot Sizes in Matplotlib using Gridspec
# # create a figure
# fig = plt.figure()

# # to change size of subplot's
# # set height of each subplot as 8
# fig.set_figheight(8)
# # set width of each subplot as 8
# fig.set_figwidth(8)

# # create grid for different subplots
# spec = gridspec.GridSpec(ncols=2, nrows=2,
# 						width_ratios=[2, 1], wspace=0.5,
# 						hspace=0.5, height_ratios=[1, 2])

# # initializing x,y axis value
# x = np.arange(0, 10, 0.1)
# y = np.cos(x)

# # ax0 will take 0th position in
# # geometry(Grid we created for subplots),
# # as we defined the position as "spec[0]"
# ax0 = fig.add_subplot(spec[0])
# ax0.plot(x, y)

# # ax1 will take 0th position in
# # geometry(Grid we created for subplots),
# # as we defined the position as "spec[1]"
# ax1 = fig.add_subplot(spec[1])
# ax1.plot(x, y)

# # ax2 will take 0th position in
# # geometry(Grid we created for subplots),
# # as we defined the position as "spec[2]"
# ax2 = fig.add_subplot(spec[2])
# ax2.plot(x, y)

# # ax3 will take 0th position in
# # geometry(Grid we created for subplots),
# # as we defined the position as "spec[3]"
# ax3 = fig.add_subplot(spec[3])
# ax3.plot(x, y)

# # display the plots
# plt.show()


# # Task 11: Create Different Subplot Sizes in Matplotlib gridspec_kw

# # setting different parameters to adjust each grid
# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7),
# 					gridspec_kw={
# 						'width_ratios': [3, 3],
# 						'height_ratios': [3, 3],
# 					'wspace': 0.4,
# 					'hspace': 0.4})

# # initializing x,y axis value
# x = np.arange(0, 10, 0.1)
# y = np.tan(x)

# # ax[0][0] will take 0th position in
# # geometry(Grid we created for subplots)
# ax[0][0].plot(x, y)

# # ax[0][0] will take 0th position in
# # geometry(Grid we created for subplots)
# ax[0][1].plot(x, y)

# # ax[0][0] will take 0th position in
# # geometry(Grid we created for subplots)
# ax[1][0].plot(x, y)

# # ax[0][0] will take 0th position in
# # geometry(Grid we created for subplots)
# ax[1][1].plot(x, y)

# plt.show()



# # Task 12:  Create Different Subplot Sizes in Matplotlib subplot2grid

# # creating grid for subplots
# fig = plt.figure()
# fig.set_figheight(6)
# fig.set_figwidth(6)

# ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=3)
# ax2 = plt.subplot2grid(shape=(3, 3), loc=(1, 0), colspan=1)
# ax3 = plt.subplot2grid(shape=(3, 3), loc=(1, 2), rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (2, 0))
# ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1)


# # initializing x,y axis value
# x = np.arange(0, 10, 0.1)
# y = np.cos(x)

# # plotting subplots
# ax1.plot(x, y)
# ax1.set_title('ax1')
# ax2.plot(x, y)
# ax2.set_title('ax2')
# ax3.plot(x, y)
# ax3.set_title('ax3')
# ax4.plot(x, y)
# ax4.set_title('ax4')
# ax5.plot(x, y)
# ax5.set_title('ax5')

# # automatically adjust padding horizontally
# # as well as vertically.
# plt.tight_layout()

# # display plot
# plt.show()
 

# Task 13: 

# create data
x=np.array([1, 2, 3, 4, 5])
# making subplots
fig, ax = plt.subplots(2, 2)

# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)
# plt.show()


# Task 14 : Using tight_layout() method to set the spacing between subplots
# set the spacing between subplots
fig.tight_layout()
# plt.show()

# Task 15: Using subplots_adjust() method to set the spacing between subplots
# set the spacing between subplots
plt.subplots_adjust(left=0.1,
					bottom=0.1,
					right=0.9,
					top=0.9,
					wspace=0.4,
					hspace=0.4)
# plt.show()

# Task 16: Using subplots_tool() method to set the spacing between subplots
# set the spacing between subplots
plt.subplot_tool()
# plt.show()

# Task 17: Using constrained_layout() to set the spacing between subplots
# making subplots with constrained_layout=True
fig, ax = plt.subplots(2, 2,
					constrained_layout = True)

# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)
plt.show()







