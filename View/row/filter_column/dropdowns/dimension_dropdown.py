
import dash_core_components as dcc
import dash_html_components as html


dimensions_dropdown = html.Div([

    html.H6("Dimensions"),

    dcc.Dropdown(

        placeholder='all',

        value='site_id',

        id='dimensions',

        options=[{'label': 'site_id', 'value': 'site_id'},
                 {'label': 'ad_type_id', 'value': 'ad_type_id'},
                 {'label': 'geo_id', 'value': 'geo_id'},
                 {'label': 'order_id', 'value': 'order_id'},
                 {'label': 'line_item_type_id', 'value': 'line_item_type_id'},
                 {'label': 'os_id', 'value': 'os_id'},
                 {'label': 'integration_type_id', 'value': 'integration_type_id'},
                 {'label': 'monetization_channel_id', 'value': 'monetization_channel_id'}
                 ]

    ),

    html.Br()

])