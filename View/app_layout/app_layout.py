import dash_html_components as html
import dash_bootstrap_components as dbc

from View.footer.footer_component import footer_component
from View.header.a2_header_component import header_component
from View.row.chart_column.chart_column import chart_columns

from View.row.filter_column.filter_column import filter_column

app_layout = html.Div([

    header_component,

    # %%
    dbc.Row([

        filter_column,

        chart_columns

    ]),

    footer_component

])
