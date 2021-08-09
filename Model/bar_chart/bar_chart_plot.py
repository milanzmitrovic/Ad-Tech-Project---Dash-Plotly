import plotly.express as px
import plotly.graph_objects as go


def bar_chart_plot(x_values, y_values, x_axis, y_axis):
    # fig = px.bar(x=x_values, y=y_values, orientation='v')

    fig = go.Figure()

    fig.add_trace(go.Bar(x=x_values, y=y_values, orientation='v', text=y_values, textposition='outside'))

    fig.update_layout(margin=dict(l=0, r=0, t=35, b=0))

    fig.update_xaxes(title_text=x_axis)

    fig.update_yaxes(title_text=y_axis)

    return fig

