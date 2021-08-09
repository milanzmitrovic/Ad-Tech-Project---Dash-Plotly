
import dash_bootstrap_components as dbc

from View.row.chart_column.first_row.first_row import first_row
import dash_html_components as html

from View.row.chart_column.second_row.second_row import second_row
from View.row.chart_column.third_row.third_row import third_row

chart_columns = dbc.Col([

    first_row,

    html.Br(),

    second_row,

    html.Br(),

    third_row,

    html.Br(),
    html.Br(),


])

