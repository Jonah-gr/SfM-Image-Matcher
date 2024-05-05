import plotly.graph_objs as go

def visualize(df):
    fig = go.Figure(data=[go.Scatter3d(
        x=df['CAMERA_POSITION'].apply(lambda pos: pos[0]),
        y=df['CAMERA_POSITION'].apply(lambda pos: pos[1]),
        z=df['CAMERA_POSITION'].apply(lambda pos: pos[2]),
        mode='markers',
        marker=dict(
            size=5,
            color='red',
            opacity=0.8
        )
    )])

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data'
        )
    )

    fig.update_layout(title_text='Camera Positions in 3D Space')

    fig.show()