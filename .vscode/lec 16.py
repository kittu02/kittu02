# lab-15

# # Task 1: using the numpy to generate random data values to input to the graph
# import plotly
# import plotly.graph_objs as G 
# import numpy as np

# num = 10
# x = np.random.randn(num)
# y = np.random.randn(num)
# print(x,y)

# follow = G.Scatter(
#     x=x,
#     y=y,
#     mode = 'lines'
# )
# output = [follow]

# plotly.offline.plot(output, filename = 'basic-scatter.html')


# # Task 2: To represent data using combination of line and scattering fashion
# import plotly
# import plotly.graph_objs as G 
# import numpy as np
# N = 20
# x = np.linspace(0,1,N)
# one_y = np.random.randn(N)+10
# two_y = np.random.randn(N)
# threee_y = np.random.randn(N)-10

# plot0 = G.Scatter(
#     x=x,
#     y=one_y,
#     mode = 'markers' 
# )
# plot1 = G.Scatter(
#     x=x,
#     y=two_y,
#     mode = 'lines+markers'
# )

# plot2 = G.Scatter(
#     x=x,
#     y=threee_y,
#     mode = 'lines'
# ) 
# output = [plot0,plot1,plot2]

# plotly.offline.plot(output, filename='line-scattering-fashion.html')

# # Task 3: Bubble scatter plot
# import plotly
# import plotly.graph_objs as G 
# import numpy as np
# img = G.Figure(data=G.Scatter(
#     x=[10,20,30,40],
#     y=[5,10,15,20],
#     mode = 'markers',
#     marker = dict(size=[10,20,30,40],
#                    color=[1,2,3,4])
# ))

# img.show()

# # Task 4: Box plot
# import plotly
# import plotly.graph_objs as G 
# import numpy as np
# a = np.random.randn(100)-10
# b = np.random.randn(100)+10
# output = G.Figure()
# output.add_trace(G.Box(y=a))
# output.add_trace(G.Box(y=b))

# output.show()

# Task 5: Histogram
import plotly
import plotly.graph_objs as G 
import numpy as np
x = np.random.randn(100)

output = G.Figure(data = [G.Histogram(x=x)])
output.show()



