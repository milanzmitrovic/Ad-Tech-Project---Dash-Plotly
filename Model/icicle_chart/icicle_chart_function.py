
import pandas as pd


def icicle_chart_function(df_: pd.DataFrame, grouping_columns: list, metric: str, agg_func: str):
    """

    input: raw data frame, [grouping columns], metric, agg_func (sum VS avg)

    :return: data frame grouped
    :rtype:
    """

    # print("**************")
    # print(grouping_columns)
    # print('*****************')

    dff = df_.groupby(by=grouping_columns).agg(agg_func)[[metric]]

    dff.reset_index(inplace=True)

    # print(dff)

    return dff

