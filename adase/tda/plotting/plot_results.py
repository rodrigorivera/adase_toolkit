import plotly.graph_objs as go

def plot_results(transformed_data, title, color):
    trace1 = go.Scatter3d(
        x=transformed_data[:, 0],
        y=transformed_data[:, 1],
        z=transformed_data[:, 2],
        mode='markers',
        marker=dict(
            size=3,
            color=color,
            #             color_scheme = color_scheme,
            opacity=0.8))

    data_to_plot = [trace1]
    layout = go.Layout(title=title, margin=dict(l=0, r=0, b=10, t=30))

    fig = go.Figure(data=data_to_plot, layout=layout)

    fig.show()