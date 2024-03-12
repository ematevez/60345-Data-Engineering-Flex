import pandas as pd
from sqlalchemy import create_engine, text

#CONEXION CON LA BASE DE DATOS
engine = create_engine("postgresql://postgres:12345@localhost/basedatos")


#CONSULTA SQL
query = """ 
    SELECT
        a.name AS agent_name,
        cu.name AS customet_name,
        c.duration AS fastest_sale_duration
    FROM (
        SELECT 
            agentid,
            MIN(duration) AS fastest_duration
        FROM calls
        WHERE productsold = 1
        GROUP BY agentid
    ) AS min_duration
    JOIN calls c ON c.agentid = min_duration.agentid AND c.duration = min_duration.fastest_duration
    JOIN agents a ON a.agentid = c.agentid
    JOIN customers cu ON cu.customerid = c.customerid
    WHERE c.productsold = 1;
"""

df = pd.read_sql_query(query, engine)

print("Resultados Consulta")
print(df)

engine.dispose()

"""
Momento 3 OLAP: extraer información para cada agente de: duración de venta más rápida, a qué cliente fue y el nombre del agente. Todo esto para poder otorgar bonos a los agentes.  
"""