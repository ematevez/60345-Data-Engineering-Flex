
import pandas as pd
import sqlite3

# Abrir el archivo CSV con pandas
df = pd.read_csv('customers.csv')

# Crear una conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(':memory:')

# Guardar el DataFrame en la base de datos SQLite
df.to_sql('customers', conn, index=False)

# Ejecutar una consulta SQL
query = "SELECT customerid, Name, CASE WHEN Age >= 30 THEN 'Yes' WHEN Age < 30 THEN 'No' ELSE 'Missing Data' END AS Over30 FROM customers ORDER BY Name DESC"
resultado = pd.read_sql_query(query, conn)
# Mostrar el resultado
print(resultado)

# Cerrar la conexión
conn.close()