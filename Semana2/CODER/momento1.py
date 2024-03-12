import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos PostgreSQL
engine = create_engine("postgresql://postgres:12345@localhost/postgres")

# Cargar datos desde archivos CSV usando pandas
csv_files = ["agents.csv", "calls.csv", "customers.csv"]
#csv_files = ["agents.csv", "calls.csv", "customers.csv","calls_with_dates.csv"]

for csv_file in csv_files:
    table_name = csv_file.split(".")[0]  # Tomar el nombre del archivo sin la extensión
    df = pd.read_csv(csv_file)

    # Utilizar el motor de SQLAlchemy para escribir en PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Cierra la conexión del motor de SQLAlchemy
engine.dispose()
