import pandas as pd


def line_chart_function(df_: pd.DataFrame, measure, agg_function):

    """

    :param df_:
    :type df_:
    :param measure:
    :type measure:
    :param agg_function:
    :type agg_function:
    :return:
    :rtype:
    """

    df_grouped = df_[measure].groupby(pd.Grouper(freq='D')).agg(agg_function)

    return df_grouped.index, df_grouped.values, measure


