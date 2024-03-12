import pandas as pd
from sqlalchemy import create_engine, text

#CONEXION CON LA BASE DE DATOS
sourse_engine = create_engine("postgresql://postgres:12345@localhost/basedatos")
destino_engine = create_engine("postgresql://postgres:12345@localhost/basedatos1")

fecha_particular = '2024-11-10'

query = text(f"SELECT * FROM calls_with_dates WHERE DATE (transaction_date)= '{fecha_particular}';")

with sourse_engine.connect() as sourse_connection:
    result = sourse_connection.execute(query)
    rows = result.fetchall()
    
df = pd.DataFrame(rows, columns=result.keys())

with destino_engine.connect() as destino_connection:
    df.to_sql('calls_filtered', destino_connection, if_exists='replace', index=False)
    
sourse_engine.dispose()
destino_engine.dispose()