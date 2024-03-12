import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos PostgreSQL
engine = create_engine("postgresql://postgres:12345@localhost/postgres")

# Consulta SQL para obtener la duración de la venta más rápida para cada agente
sql_query = """
    SELECT
        a.name AS agent_name,
        cu.name AS customer_name,
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

# Utilizando pandas para ejecutar la consulta y obtener un DataFrame
df = pd.read_sql_query(sql_query, engine)

# Muestra los resultados en la consola
print("Resultados de la consulta OLAP:")
print(df)

# Cierra la conexión del motor de SQLAlchemy
engine.dispose()
