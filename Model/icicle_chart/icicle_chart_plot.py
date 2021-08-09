
import pandas as pd
import plotly.express as px


def icicle_chart_plot(df_aggregated: pd.DataFrame, grouping_columns: list, metric):
    """

    input: grouped data frame, [grouping columns], metric


    :return:
    :rtype:
    """

    fig_1 = px.icicle(df_aggregated, path=[px.Constant("all"), ] + grouping_columns, values=metric)
    fig_1.update_traces(root_color="lightgrey")
    fig_1.update_layout(margin=dict(t=35, l=0, r=0, b=0))

    return fig_1

