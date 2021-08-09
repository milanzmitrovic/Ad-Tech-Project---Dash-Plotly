from View.row.chart_column.first_row.bar_chart.bar_chart import bar_chart
from View.row.chart_column.first_row.line_chart.line_chart import line_chart
import dash_bootstrap_components as dbc


first_row = dbc.Row([
    bar_chart,

    line_chart

])

