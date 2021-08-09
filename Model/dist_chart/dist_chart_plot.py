
import pandas as pd
import plotly.express as px


def dist_chart_plot(df_: pd.DataFrame, x_values, y_values):
    dff = df_.sample(n=500)

    fig = px.scatter(data_frame=dff,
                     x=x_values,
                     y=y_values,
                     marginal_x="histogram",
                     marginal_y="histogram"
                     )

    # fig.update_layout(
    #
    #     margin=dict(
    #         l=0,
    #         r=0,
    #         t=35,
    #         b=0
    #
    #     )
    #
    # )

    fig.update_layout(margin=dict(t=35, l=0, r=0, b=0))

    return fig


