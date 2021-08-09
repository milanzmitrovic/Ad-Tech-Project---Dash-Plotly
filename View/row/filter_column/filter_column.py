
import dash_bootstrap_components as dbc
import dash_html_components as html

from View.row.filter_column.dropdowns.agg_function_dropdown import agg_function_dropdown
from View.row.filter_column.dropdowns.dimension_dropdown import dimensions_dropdown
from View.row.filter_column.dropdowns.measure_dropdown import measure_dropdown

filter_column = dbc.Col([

    dbc.Col(),

    # Filter column
    dbc.Col([

        html.Br(),

        dimensions_dropdown,

        measure_dropdown,

        agg_function_dropdown,

        # icicle_dropdown,

    ],
        # md=2,
        # sm=12,
        # style={'display': 'none'},
        # style={'margin-left': '1px'}
    )

],
    sm=12, md=2, lg=2)


