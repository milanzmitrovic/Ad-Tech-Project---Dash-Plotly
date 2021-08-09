
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


scatter_plot = dbc.Col([

    dbc.Card([

        dbc.CardHeader([

            dbc.Row([

                dbc.Col(

                    html.H3("Scatter Plot"),

                    width=6

                ),

                dbc.Col([

                    dcc.Dropdown(

                        value='total_impressions',

                        id='dist-dropdown-1',

                        options=[{'label': 'total_revenue', 'value': 'total_revenue'},
                                 {'label': 'total_impressions', 'value': 'total_impressions'},
                                 {'label': 'viewable_impressions', 'value': 'viewable_impressions'},
                                 {'label': 'measurable_impressions', 'value': 'measurable_impressions'},

                                 ]

                    ),

                ], width=3),

                dbc.Col([

                    dcc.Dropdown(

                        value='total_revenue',

                        id='dist-dropdown-2',

                        options=[{'label': 'total_revenue', 'value': 'total_revenue'},
                                 {'label': 'total_impressions', 'value': 'total_impressions'},
                                 {'label': 'viewable_impressions', 'value': 'viewable_impressions'},
                                 {'label': 'measurable_impressions', 'value': 'measurable_impressions'},

                                 ]

                    ),

                ], width=3)
            ]),

        ]),

        dbc.CardBody([

            dcc.Graph(id='dist-chart')

        ])

    ])

])

