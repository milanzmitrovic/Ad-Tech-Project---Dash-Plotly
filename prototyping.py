import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

# %%

df = pd.read_csv("data/AD-Tech.csv")

# %%

# Correlation matrix

corr = df.corr()

fig_1 = go.Figure()

fig_1.add_trace(

    go.Heatmap(z=corr.values,
               x=corr.index.values,
               y=corr.columns.values
               )

)

fig_1.show()

# %%

df['date'] = pd.to_datetime(df['date'])

# %%
# Should be added functionality: sum, mean, median, st_dev to choose
#
# total_revenue per site_id

df['site_id'].unique()

df_grouped: pd.DataFrame = df[['site_id', 'total_revenue']].groupby(by=['site_id']).sum()

# %%


df_grouped.sort_values(by='total_revenue', inplace=True, ascending=False)

# %%

lst = []
for i in df_grouped.index.values.flatten():
    lst.append(str(int(i)))
lst

# %%

fig = px.bar(x=lst, y=df_grouped.values.flatten())

fig.show()

# %%

df.columns

# %%

print("site_id")
print(len(df['site_id'].unique()))

print("ad_type_id")
print(len(df['ad_type_id'].unique()))

print('geo_id')
print(len(df['geo_id'].unique()))

# unique per line
print("device_category_id")
print(len(df['device_category_id']))

# unique per line
print('advertiser_id')
print(len(df['advertiser_id']))

print('order_id')
print(len(df['order_id'].unique()))

print('line_item_type_id')
print(len(df['line_item_type_id'].unique()))

print('os_id')
print(len(df['os_id'].unique()))

print('integration_type_id')
print(len(df['integration_type_id'].unique()))

print('monetization_channel_id')
print(len(df['monetization_channel_id'].unique()))

# unique per line
print('ad_unit_id')
print(len(df['ad_unit_id']))

# %%

print('min date')
print(df['date'].min())

print('max date')
print(df['date'].max())

# %%

# Ideja

# Biramo metriku: total_impression, total_revenue, viewable_impressions, measurable_impressions, revenue_share_percent

# Biramo agregaciju metrike: sum, mean, max, min, sd_dev, count

## Biramo dimenziju za stubice:

## Biramo sta ce se prikazati na linijskom dijagramu

### Odvojeno biramo sta ce se prikazati na hijerarhijskom grafikonu

# Imamo vremenski filter

# %%


# Imaju dva interfejsa:
#   1. Koji pravi grafikon
#       inputi:
#            x - osa
#            y - osa
#       autput:
#           grafikon
#
#   2. Koji vraca podatke
#
#       autputi:
#           x - osa
#           y - osa
#       inputi:
#           naziv metrike
#           naziv dimenzije
#
#
#


# %%


# icicle chart

#
# %%

df.dtypes

df['date'] = pd.to_datetime(df['date'])

# %%


dff = df.set_index(df['date'])

df_grouped = dff['total_revenue'].groupby(pd.Grouper(freq='D')).agg(func=['sum', 'min', 'max', 'mean', 'count'])

df_grouped_min = dff['total_revenue'].groupby(pd.Grouper(freq='D')).min()

df_grouped_max = dff['total_revenue'].groupby(pd.Grouper(freq='D')).max()

# %%


df_grouped.sort_index(inplace=True)

# %%

px.line(x=df_grouped.index, y=df_grouped.values).show()

# %%

import plotly.io as pio

pio.renderers.default = 'browser'

import plotly.express as px

df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()

# %%


df.groupby(by='day').sum()

# %%


import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()

# %%

df_grouped_1 = df.groupby(by=['day', 'time', 'sex']).sum()['total_bill']

# %%

import pandas as pd

df_grouped_1: pd.DataFrame

ss = df_grouped_1.reset_index()

# %%


fig_1 = px.icicle(ss, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()

# %%


# %%


[1, 2, 3, ] + ['3', 'ss']

# %%


fig = px.line(data_frame=df_grouped, x=df_grouped.index.values, y='max', render_mode='lines+markers')

fig.show()

# %%

fig = px.scatter(data_frame=df_grouped, x=df_grouped.index.values, y='max')

fig.layout

fig.show()

# %%
import numpy as np

df_grouped.replace(to_replace=np.nan, value='nan')

# %%


type(df_grouped.iloc[1]['sum'])

# %%
import plotly.graph_objects as go

fig = go.Figure()

fig.add_traces(go.Scatter(x=df_grouped.index.values, y=df_grouped['max'].values, mode='lines'))

fig.show()

# %%


t = df[['site_id', 'total_revenue']].groupby(by='site_id').agg(func='min')

# %%


df.query("os_id == '55'")['total_revenue'].min()

# %%

t = df.groupby(by='os_id').min()['total_revenue']

px.bar(x=t.index.values, y=t.values).show()


# %%

def icicle_chart_function(df_: pd.DataFrame, grouping_columns: list, metric: str, agg_func: str):
    """

    input: raw data frame, [grouping columns], metric, agg_func (sum VS avg)

    :return: data frame grouped
    :rtype:
    """

    dff = df_.groupby(by=grouping_columns).agg(agg_func)[[metric]]

    dff.reset_index(inplace=True)

    return dff


def icicle_chart_plot(df_aggregated: pd.DataFrame, grouping_columns: list, metric):
    """

    input: grouped data frame, [grouping columns], metric


    :return:
    :rtype:
    """

    fig_1 = px.icicle(df_aggregated, path=[px.Constant("all"), ] + grouping_columns, values=metric)
    fig_1.update_traces(root_color="lightgrey")
    fig_1.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig_1


# %%


ff = icicle_chart_function(df_=df, grouping_columns=['site_id', 'geo_id'], metric='total_revenue', agg_func='sum')

# %%

icicle_chart_plot(df_aggregated=ff, grouping_columns=['site_id', 'geo_id'], metric='sum')

# %%

fig_1 = px.icicle(ff, path=[px.Constant("all"), ] + ['site_id', 'geo_id'], values='total_revenue')

# %%

fig_1.update_traces(root_color="lightgrey")
fig_1.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig_1.show()

# %%

import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

df = pd.read_csv("data/AD-Tech.csv")


def icicle_chart_plot(df_aggregated: pd.DataFrame, grouping_columns: list, metric):
    """

    input: grouped data frame, [grouping columns], metric


    :return:
    :rtype:
    """

    fig_1 = px.icicle(df_aggregated, path=[px.Constant("all"), ] + grouping_columns, values=metric)
    fig_1.update_traces(root_color="lightgrey")
    fig_1.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig_1


def icicle_chart_function(df_: pd.DataFrame, grouping_columns: list, metric: str, agg_func: str):
    """

    input: raw data frame, [grouping columns], metric, agg_func (sum VS avg)

    :return: data frame grouped
    :rtype:
    """

    print("**************")
    print(grouping_columns)
    print('*****************')

    dff = df_.groupby(by=grouping_columns).agg(agg_func)[[metric]]

    dff.reset_index(inplace=True)

    print(dff)

    return dff


# %%

col = ['site_id', 'geo_id']

metric = 'total_revenue'

fnc = 'sum'

ff = icicle_chart_function(df_=df, grouping_columns=col, metric=metric, agg_func=fnc)

fig = icicle_chart_plot(df_aggregated=ff, grouping_columns=col, metric=metric)

fig.show()

# %%


import plotly.express as px

data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.icicle(
    data,
    names='character',
    parents='parent',
    values='value',
    width=200,
    height=200
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig.show()

# %%

dff = df.sample(n=500)

px.histogram(data_frame=dff, x='total_impressions', histnorm='probability density').show()

# %%

dff = df.sample(n=500, random_state=1)

px.scatter(data_frame=dff, x='total_impressions', y='measurable_impressions').show()

# %%

import plotly.express as px

import plotly.io as pio

pio.renderers.default = 'browser'

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", marginal_x="histogram", marginal_y="histogram")
fig.show()


# %%


