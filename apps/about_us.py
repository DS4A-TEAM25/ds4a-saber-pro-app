import dash_bootstrap_components as dbc
import dash_html_components as html


#Cards storing information of team members
card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/IMG_0641.png", top=True),
        dbc.CardBody(
            [
                html.H4("Nohora Diaz Pinedo", className="card-title"),
                html.P(
                    "Cartagena. "
                    "Director II Data Science, East and West predictive modeling at Liberty Mutual Insurance",
                    className="card-text",
                ),
                dbc.Button(html.Span([html.I(className="fab fa-linkedin ml-0"), " LinkedIn"]),
               href="https://www.linkedin.com/in/nohoradiaz", target="_blank", color="primary"),
            ]
        ),
    ],
)


card2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/IMG_0640.png", top=True),
        dbc.CardBody(
            [
                html.H4("Maria Paula Aroca", className="card-title"),
                html.P(
                    "Barranquilla. "
                    "PhD Candidate Political Science, Rice University",
                    className="card-text",
                ),
                dbc.Button(html.Span([html.I(className="fab fa-linkedin ml-0"), " LinkedIn"]),
               href="https://www.linkedin.com/in/maria-paula-aroca-42a0a5166", target="_blank", color="primary"),
            ]
        ),
    ],
)


card3 = dbc.Card(
    [
        dbc.CardImg(src="/assets/IMG_0639.png", top=True),
        dbc.CardBody(
            [
                html.H4("Santiago Cortés Ocaña", className="card-title"),
                html.P(
                    "Cartagena. "
                    "Coordinator Electronic and Biomedical Engineering, Universidad Antonio Nariño",
                    className="card-text",
                ),
                dbc.Button(html.Span([html.I(className="fab fa-linkedin ml-0"), " LinkedIn"]),
               href="https://www.linkedin.com/in/santiago-cortés-ocaña-55122917a", target="_blank", color="primary"),
            ]
        ),
    ],
)


card4 = dbc.Card(
    [
        dbc.CardImg(src="/assets/IMG_0642.png", top=True),
        dbc.CardBody(
            [
                html.H4("Eugenia Luz Arrieta", className="card-title"),
                html.P(
                    "Cartagena. "
                    "Research Coordinator School of Engineering, Universidad del Sinú",
                    className="card-text",
                ),
                dbc.Button(html.Span([html.I(className="fab fa-linkedin ml-0"), " LinkedIn"]),
               href="https://www.linkedin.com/in/eugenia-arrieta-rodríguez-98797659", target="_blank", color="primary"),
            ]
        ),
    ],
)


card5 = dbc.Card(
    [
        dbc.CardImg(src="/assets/IMG_0647.png", top=True),
        dbc.CardBody(
            [
                html.H4("Rafael Vicente Deaguas", className="card-title"),
                html.P(
                    "Cartagena. "
                    "Quality and Process Manager, KNAUF",
                    className="card-text",
                ),
                dbc.Button(html.Span([html.I(className="fab fa-linkedin ml-0"), " LinkedIn"]),
               href="https://www.linkedin.com/in/rafael-d-8236b2136", target="_blank", color="primary"),
            ]
        ),
    ],
)


card6 = dbc.Card(
    [
        dbc.CardImg(src="/assets/IMG_0646.png", top=True),
        dbc.CardBody(
            [
                html.H4("Paula Almonacid", className="card-title"),
                html.P(
                    "Medellin. " "Assistant professor, Universidad EAFIT.",
                    className="card-text",
                ),
                dbc.Button(html.Span([html.I(className="fab fa-linkedin ml-0"), " LinkedIn"]),
               href="https://www.linkedin.com/in/paula-almonacid-802997100", target="_blank", color="primary"),
            ]
        ),
    ],
)


#Layout
layout = html.Div(
    [
        dbc.Row([dbc.Col(card1, width=2), dbc.Col(card2, width=2), dbc.Col(card3, width=2)], justify="center"), 
        dbc.Row([dbc.Col(card4, width=2), dbc.Col(card5, width=2), dbc.Col(card6, width=2)], justify="center")
        
    ]
    
)