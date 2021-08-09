
import dash_bootstrap_components as dbc
import dash_html_components as html


PLOTLY_LOGO = "https://milanzmitrovic.github.io/assets/images/mbr-168x160.png"


header_component = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(
                        dbc.NavbarBrand("Ad Tech Dataset", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://milanzmitrovic.github.io",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        # dbc.Collapse(
        #     search_bar, id="navbar-collapse", navbar=True, is_open=False
        # ),
    ],
    color="dark",
    dark=True,
)

