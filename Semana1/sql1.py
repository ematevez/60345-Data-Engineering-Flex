import pandas as pd
import sqlite3

# Abrir el archivo CSV con pandas
df = pd.read_csv('agents.csv')

# Crear una conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(':memory:')

# Guardar el DataFrame en la base de datos SQLite
df.to_sql('agents', conn, index=False)

# Ejecutar una consulta SQL
query = "SELECT * FROM agents WHERE name LIKE 'M%' OR name LIKE '%o'"


resultado = pd.read_sql_query(query, conn)

# Mostrar el resultado
print(resultado)

# Cerrar la conexión
conn.close()