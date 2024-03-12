import pandas as pd
from sqlalchemy import create_engine, text

# Conexión a la base de datos PostgreSQL
source_engine = create_engine("postgresql://postgres:12345@localhost/postgres")
destination_engine = create_engine("postgresql://postgres:12345@localhost/postgres1")

# Definir la fecha particular para la consulta (ajusta según tus necesidades)
fecha_particular = '2024-03-06'

# Consulta SQL para obtener transacciones de un día particular
query = text(f"SELECT * FROM calls_with_dates WHERE DATE(transaction_date) = '{fecha_particular}';")

# Ejecutar la consulta en la base de datos de origen
with source_engine.connect() as source_connection:
    result = source_connection.execute(query)
    rows = result.fetchall()

# Convertir los resultados a un DataFrame de pandas
df = pd.DataFrame(rows, columns=result.keys())

# Almacenar los resultados en la nueva base de datos
with destination_engine.connect() as destination_connection:
    df.to_sql('calls_filtered', destination_connection, if_exists='replace', index=False)

# Cierra las conexiones de los motores de SQLAlchemy
source_engine.dispose()
destination_engine.dispose()
