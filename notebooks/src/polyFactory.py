import numpy as np
from plotter import plotter

def polyFactory(plt, func, title, xv):
    
    def poly(color, a, h, k):
    
        yv = np.array(list(map(lambda x: func(x, a, h, k), xv)))

        return plotter(plt, title, color, xv, yv)
        #return plotter(plt=plt, title=title, color=color, xv=xv, yv=yv)
    
    return poly

