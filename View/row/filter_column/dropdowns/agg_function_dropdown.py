
import dash_html_components as html
import dash_core_components as dcc

agg_function_dropdown = html.Div([

    html.H6("Agg Function"),

    dcc.Dropdown(

        placeholder='all',

        value='sum',

        id='agg-function',

        options=[{'label': 'min', 'value': 'min'},
                 {'label': 'max', 'value': 'max'},
                 {'label': 'sum', 'value': 'sum'},
                 {'label': 'mean', 'value': 'mean'},
                 {'label': 'std', 'value': 'std'},
                 ]

    ),

    html.Br()

])