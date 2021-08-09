
import dash_core_components as dcc
import dash_html_components as html


icicle_dropdown = html.Div([

    html.H6("Icicle chart dimensions"),

    dcc.Dropdown(

        placeholder='None',

        value=['site_id', 'geo_id'],

        id='icicle',

        options=[{'label': 'site_id', 'value': 'site_id'},
                 {'label': 'ad_type_id', 'value': 'ad_type_id'},
                 {'label': 'geo_id', 'value': 'geo_id'},
                 {'label': 'order_id', 'value': 'order_id'},
                 {'label': 'line_item_type_id', 'value': 'line_item_type_id'},
                 {'label': 'os_id', 'value': 'os_id'},
                 {'label': 'integration_type_id', 'value': 'integration_type_id'},
                 {'label': 'monetization_channel_id', 'value': 'monetization_channel_id'}
                 ],
        multi=True

    ),

    # html.Br()

])

