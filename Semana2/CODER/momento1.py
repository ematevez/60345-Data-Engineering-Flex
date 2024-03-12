import pandas as pd
from sqlalchemy import create_engine

#CONEXION CON LA BASE DE DATOS
engine = create_engine("postgresql://postgres:12345@localhost/basedatos")

#CARGAR DATOS DE LOS CSV
cvs_files = ['agents.csv','calls.csv','customers.csv','calls_with_dates.csv']

for csv_file in cvs_files:
    table_name = csv_file.split('.')[0]
    df = pd.read_csv(csv_file)
    
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    
engine.dispose()