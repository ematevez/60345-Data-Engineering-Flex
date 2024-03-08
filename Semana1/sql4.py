import pandas as pd
import sqlite3

# Cargar datos desde archivos CSV
calls_df = pd.read_csv("calls.csv")
customers_df = pd.read_csv("customers.csv")

# Crear la base de datos SQLite y cargar DataFrames
conn = sqlite3.connect(":memory:")  # Crear base de datos en memoria
calls_df.to_sql("calls", conn, index=False)
customers_df.to_sql("customers", conn, index=False)

# Consulta SQL
query = """
SELECT Ca.CallID, Ca.CustomerID, Cu.Name, Ca.ProductSold,
    CASE
        WHEN Cu.Age >= 30 THEN 'Yes'
        WHEN Cu.Age < 30 THEN 'No'
        ELSE 'Missing Data'
    END AS Over30
FROM calls Ca
JOIN customers Cu ON Ca.CustomerID = Cu.CustomerID
WHERE Cu.Occupation LIKE '%Engineer%'
ORDER BY Cu.Name DESC;
"""

# Ejecutar la consulta y mostrar el resultado
result_df = pd.read_sql_query(query, conn)
print(result_df)
