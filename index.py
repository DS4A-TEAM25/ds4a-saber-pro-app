import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app
from apps import home, model2, about_us,  by_location, by_university, model1

# building the navigation bar
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            html.Span([html.I(className="fas fa-home ml-0"), " Home"]), href="/home"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Describe", header=True),
        dbc.DropdownMenuItem(
            html.Span([html.I(className="fas fa-map-marked-alt ml-0"), " Explore by Location"]), href="/by_location"),
        dbc.DropdownMenuItem(
            html.Span([html.I(className="fas fa-university ml-0"), " Explore by University"]), href="/by_university"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Estimate", header=True),
        dbc.DropdownMenuItem(
            html.Span([html.I(className="fas fa-chart-line ml-0"), " Predict Scores"]), href="/model1"),
        dbc.DropdownMenuItem(
            html.Span([html.I(className="fas fa-chart-bar ml-0"), " Which factors matter?"]), href="/model2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem(
            html.Span([html.I(className="fas fa-info-circle ml-0"), " About Us"]), href="/about_us"),
    
    ],
    nav = True,
    in_navbar = True,
    bs_size="lg",
    right=True,
    label = "Explore",
)



#Create navigation bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/ds4A-logo.png", height="25px")),
                        dbc.Col(dbc.NavbarBrand("", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="#395CA3", #Company color
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


#Making the links on the navbar reactive

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about_us':
        return about_us.layout
    elif pathname == '/model1':
        return model1.layout
    elif pathname == '/by_location':
        return by_location.layout
    elif pathname == '/model2':
        return model2.layout 
    elif pathname == '/by_university':
        return by_university.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
