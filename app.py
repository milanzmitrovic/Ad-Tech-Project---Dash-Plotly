import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

from Model.bar_chart.bar_chart_function import bar_chart_function
from Model.dist_chart.dist_chart_plot import dist_chart_plot
from Model.icicle_chart.icicle_chart_function import icicle_chart_function
from Model.line_chart.line_chart_function import line_chart_function
from Memory_data.in_memory_data import df
from Model.bar_chart import bar_chart_plot
from Model.bar_chart.bar_chart_plot import bar_chart_plot
from Model.icicle_chart.icicle_chart_plot import icicle_chart_plot
from Model.line_chart.line_chart_plot import line_chart_plot
from View.app_layout.app_layout import app_layout

app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = app_layout


# Bar Chart and Line Chart
@app.callback([
                Output(component_id='bar-chart', component_property='figure'),
                Output(component_id='line-chart', component_property='figure')
               ],
              [
                  Input(component_id='dimensions', component_property='value'),
                  Input(component_id='measure', component_property='value'),
                  Input(component_id='agg-function', component_property='value')
               ]
              )
def f1(input_dimension, input_measure, input_agg_function):
    print(input_dimension, )

    x_bar, y_bar, x_axis_bar, y_axis_bar = bar_chart_function(df_=df, dimension=input_dimension, measure=input_measure, agg_function=input_agg_function)

    x_line, y_line, y_axis_line = line_chart_function(df_=df, measure=input_measure, agg_function=input_agg_function)

    return bar_chart_plot(x_values=x_bar, y_values=y_bar, x_axis=x_axis_bar, y_axis=y_axis_bar), line_chart_plot(x_values=x_line, y_values=y_line, y_axis=y_axis_line)


# Icicle Chart
@app.callback(
    Output(component_id='test7', component_property='figure')
    ,
    [
        Input(component_id='icicle', component_property='value'),
        Input(component_id='measure', component_property='value')

    ]
)
def f2(icicle_dimensions, measure):

    dff = icicle_chart_function(df_=df, grouping_columns=icicle_dimensions, metric=measure, agg_func='sum')

    figg = icicle_chart_plot(df_aggregated=dff, grouping_columns=icicle_dimensions, metric=measure)

    return figg


@app.callback(

    Output(component_id='dist-chart', component_property='figure'),

    [
        Input(component_id='dist-dropdown-1', component_property='value'),
        Input(component_id='dist-dropdown-2', component_property='value')
    ]
)
def f3(input_x, input_y):
    return dist_chart_plot(df_=df, x_values=input_x, y_values=input_y)


# @app.callback(
#
#     Output(component_id='bar-chart', component_property='figure'),
#     [
#         Input(component_id='bar-chart', component_property='figure'),
#         Input(component_id='dimensions', component_property='value'),
#         Input(component_id='agg-function', component_property='value')
#
#     ]
#
# )
# def axis_bar_chart(fig, x_axis, y_axis):
#     pass
#


@app.callback(

    Output(component_id='icicle-title', component_property='children'),
    [Input(component_id='measure', component_property='value')]
)
def f43(input_title):
    return "Icicle Chart: sum of " + input_title


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')


