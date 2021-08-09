
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


line_chart = dbc.Col([
    # html.H1("Row 1, chart 2"),

    html.Br(),

    dbc.Card([

        dbc.CardHeader(

            dbc.Row([

                dbc.Col([
                    html.H4("Line Chart")

                ])

            ]),

        ),

        dbc.CardBody(
            dcc.Graph(id='line-chart')
        )

    ]),

], sm=12, md=6, lg=6)


