
import dash_core_components as dcc
import dash_html_components as html


measure_dropdown = html.Div([

    html.H6("Measures"),

    dcc.Dropdown(

        placeholder='all',

        value='total_revenue',

        id='measure',

        options=[{'label': 'total_impressions', 'value': 'total_impressions'},
                 {'label': 'total_revenue', 'value': 'total_revenue'},
                 {'label': 'viewable_impressions', 'value': 'viewable_impressions'},
                 {'label': 'measurable_impressions', 'value': 'measurable_impressions'},
                 ]

    ),

    html.Br()

])

