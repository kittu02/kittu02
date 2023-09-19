import plotly
import plotly.graph_objs as G 
import numpy as np

a = np.random.randn(10)
b = np.random.randn(10)
print(a,b)

follow = G.Scatter(
    x=a,
    y=b,
    mode = 'lines'
)

img = G.Figure(data=G.Scatter(
    a=a,
    b=b,
    mode = 'markers',
    marker = dict(size=[10,20,30,40,10,20,30,40,30,50],
                   color=[1,2,3,4,1,2,3,4,1,6])
))

output = [follow] + [img]

plotly.offline.plot(output, filename='abc.html')



