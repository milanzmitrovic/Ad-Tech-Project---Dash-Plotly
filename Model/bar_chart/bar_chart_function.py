import pandas as pd


def rnd(x):
    return round(x, 2)


def bar_chart_function(df_, dimension, measure, agg_function) -> tuple:
    """

    :param df_:
    :type df_:

    :param dimension:
    :type dimension:

    :param measure:
    :type measure:

    :param agg_function:
    :type agg_function:

    :return: (x, y, x_axis, y_axis)
    :rtype: tuple

    This function is returning X and Y values necessary for plotting bar chart.

    Inputs are: data frame, dimension (that we want to plot by), measure that we want to see, aggregation
    function that we want to apply to measure.


    """
    df_grouped: pd.DataFrame = df_[[dimension, measure]].groupby(by=dimension).agg(func=agg_function)

    # print(df_grouped.index.values.tolist())
    # print(df_grouped.values.flatten())

    df_grouped.sort_values(by=measure, inplace=True, ascending=False)

    x_lst = []
    for i in df_grouped.index.values.flatten():
        x_lst.append(str(int(i)))
    #x_lst

    return x_lst, list(map(rnd, df_grouped.values.flatten().tolist())), dimension, measure


