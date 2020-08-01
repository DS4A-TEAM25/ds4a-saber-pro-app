import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def get_unique(connection, db, col):
    query = f"""
    SELECT DISTINCT {col}
    FROM {db};
    """
    return [x[0] for x in connection.execute(query).fetchall()]



#Text wrapper so that long labels are wrapped in legend
wrapper = textwrap.TextWrapper(width=11) 
