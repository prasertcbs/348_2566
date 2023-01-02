# experiment with for loop

import numpy as np
import plotly.express as px


def heart():
    # http://mathworld.wolfram.com/HeartCurve.html
    t = np.linspace(0, 2 * np.pi, 360)
    # print(t)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    # return px.scatter(x=x, y=y)
    fig = px.scatter(x=x, y=y, width=600)
    fig.add_scatter(x=x + 10, y=y)
    fig.update_layout(showlegend=False)
    return fig


fig = heart()
fig.show()
