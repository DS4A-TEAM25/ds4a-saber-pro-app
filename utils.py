import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import textwrap
from sqlalchemy import create_engine
from textwrap import dedent

# Create Engine and connect to DB
engine = create_engine('postgresql://admin:ds4a@project.c6mkiiu8v7ky.us-east-2.rds.amazonaws.com/project_ds4a')



#SQL QUERY FORMULAS
#Unique values of column
def get_unique(connection, db, col):
    query = f"""
    SELECT DISTINCT {col}
    FROM {db};
    """
    return [x[0] for x in connection.execute(query).fetchall()]


#SQL QUERY FORMULAS
#Unique values of column by condition
def get_unique_conditional(connection, db, var, col, value, period1, period2):
    query = f"""
    SELECT DISTINCT {var}
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col} = {value};
    """
    return [x[0] for x in connection.execute(query).fetchall()]


#GENERATE QUINTLE DF
def get_pct(connection, db, var, quintile_score, score, col, value, period1, period2):
    query = f"""
    SELECT {var},(sum(CASE WHEN {quintile_score} =0.0 then 1 ELSE 0 END)) sum_quintil_1,
    (sum(CASE WHEN {quintile_score} =4.0 then 1 ELSE 0 END)) sum_quintil_5,
    (COUNT(DISTINCT estu_consecutivo)) sum_students,
    (AVG({score})) avg_score
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col} = {value}
    GROUP BY {var}
    ;
    """
    return [x for x in connection.execute(query).fetchall()]


#Average given period and column values
def get_avg(connection, db, score, col, value, period1, period2):
    query = f"""
    SELECT AVG({score})
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col} = {value}
    ;
    """
    return [x[0] for x in connection.execute(query).fetchall()]


#Average of a column given period and column values
def get_avg(connection, db, score, col, value, period1, period2):
    query = f"""
    SELECT AVG({score})
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col} = {value}
    ;
    """
    return [x[0] for x in connection.execute(query).fetchall()]






#Average grouped by column given period and column values
def get_avg_input(connection, db, score, col1, col2, value, period1, period2):
    query = f"""
    SELECT {col1},  AVG({score})
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col2} = {value}
    GROUP BY {col1}
    ;
    """
    return [x for x in connection.execute(query).fetchall()]



#Average grouped by column given period and column values
def get_avg_input2(connection, db, score, col1, col2, value, period1, period2):
    query = f"""
    SELECT {col2},{col1},  AVG({score})
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col2} = {value}
    GROUP BY {col2}, {col1}
    ;
    """
    return [x for x in connection.execute(query).fetchall()]



#Average grouped by column given period and column values
def get_avg_input3(connection, db, score, col1, col2, value, period1, period2):
    query = f"""
    SELECT {col1},  AVG({score})
    FROM {db}
    WHERE 
        (periodo BETWEEN {period1} AND {period2}) 
    AND {col1} = (SELECT {col1}  FROM {db} WHERE {col2}= {value} LIMIT 1 )
    GROUP BY {col1}
    ;
    """
    return [x for x in connection.execute(query).fetchall()]

# Cache function
def connect_read_sql(query, engine):
    connection = engine.connect()
    result = pd.read_sql(query, connection)
    connection.close()
    return result




#Text wrapper so that long labels are wrapped in legend
wrapper = textwrap.TextWrapper(width=11) 
