
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


bar_chart = dbc.Col([
    # html.H1("Row 1, chart 1"),

    html.Br(),

    dbc.Card([

        dbc.CardHeader(

            dbc.Row([

                dbc.Col([

                    html.H4("Bar Chart")

                ])

            ])

        ),

        dbc.CardBody(

            dcc.Graph(id='bar-chart')

        ),

        # dbc.CardFooter("This is place for Legend")

    ]),

], sm=12, md=6, lg=6)


