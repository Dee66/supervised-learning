import numpy as np
import plotly.graph_objects as go

def animate_failure_propagation(failure_points, duration=5):
    frames = []
    for point in failure_points:
        frame = go.Frame(data=[
            go.Scatter(
                x=point['x'],
                y=point['y'],
                mode='markers',
                marker=dict(size=10, color='red', opacity=0.6),
                name='Failure Point'
            )
        ])
        frames.append(frame)

    return frames

def update_animation_state(fig, current_frame):
    fig.frames = current_frame
    fig.update_layout(updatemenus=[{
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }])
    return fig