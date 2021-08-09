
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from View.row.filter_column.dropdowns.icicle_dropdown import icicle_dropdown

icicle_chart = dbc.Col([

    dbc.Card([

        dbc.CardHeader([

            dbc.Row([

                dbc.Col(

                    html.H3("Icicle Chart", id='icicle-title'),

                ),

                dbc.Col(

                    icicle_dropdown

                )

            ])

        ]),

        dbc.CardBody([

            dcc.Graph(id='test7')

        ])

    ])

])

