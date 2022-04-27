import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

if len(sys.argv) < 3:
    raise Exception("No arguments are presented")
title = "Visual Representation of " + str(sys.argv[1]) + " plane"
axe = str(sys.argv[1]) + "/"
name = str(sys.argv[2]) + ".npy"

pathAxial = "/home/snake/Desktop/mrnet/data/train/"+axe + name
#pathCoronal = "/home/snake/Desktop/mrnet/data/train/coronal/" + name
#pathSagittal = "/home/snake/Desktop/mrnet/data/train/sagittal/" + name

axial = np.load(pathAxial)
lengthAxial = len(axial)
r, c = axial[0].shape

# coronal = np.load(pathCoronal)
# lengthCoronal = len(coronal)
# r2, c2 = coronal[0].shape
#
# sagittal = np.load(pathSagittal)
# lengthSagittal = len(sagittal)
# r3, c3 = sagittal[0].shape



#fig = make_subplots(rows=1, cols=3,subplot_titles=("Axial","Coronal","Sagittal"))
fig = go.Figure(frames=[go.Frame(data=go.Surface(
    z=(6.7 - k * 0.1) * np.ones((r, c)),
    surfacecolor=np.flipud(axial[lengthAxial - 1 - k]),
    cmin=0, cmax=250
),
    name=str(k)
)
    for k in range(lengthAxial)])
fig.add_trace(go.Surface(
    z= 6.7 * np.ones((r, c)),
    surfacecolor=np.flipud(axial[lengthAxial - 1]),
    colorscale='Gray',
    cmin=0, cmax=250,
    colorbar=dict(thickness=20, ticklen=4)
))


def frame_args(duration):
    return {
        "frame": {"duration": duration},
        "mode": "immediate",
        "fromcurrent": True,
        "transition": {"duration": duration, "easing": "linear"},
    }
sliders = [
    {
        "pad": {"b": 10, "t": 60},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [
            {
                "args": [[f.name], frame_args(0)],
                "label": str(k),
                "method": "animate",
            }
            for k, f in enumerate(fig.frames)
        ],
    }
]

fig.update_layout(
    title=title,
    width=600,
    height=600,
    scene=dict(
        zaxis=dict(range=[-0.1, 6.8], autorange=False),
        aspectratio=dict(x=1, y=1, z=1),
    ),
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, frame_args(50)],
                    "label": "&#9654;",  # play symbol
                    "method": "animate",
                },
                {
                    "args": [[None], frame_args(0)],
                    "label": "&#9724;",  # pause symbol
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 70},
            "type": "buttons",
            "x": 0.1,
            "y": 0,
        }
    ],
    sliders=sliders
)

fig.show()
