import plotly.express as px
import plotly.graph_objects as go


def line_chart_plot(x_values, y_values, y_axis):

    # fig = px.line(x=x_values, y=y_values)

    fig = go.Figure()

    fig.add_traces(go.Scatter(x=x_values, y=y_values, mode='lines+markers'))

    fig.update_layout(margin=dict(l=0, r=0, t=35, b=0))

    fig.update_yaxes(
        title_text=y_axis
    )

    return fig

