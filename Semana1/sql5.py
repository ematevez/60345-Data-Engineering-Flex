import pandas as pd
import sqlite3

# Cargar datos desde archivos CSV
calls_df = pd.read_csv("calls.csv")
customers_df = pd.read_csv("customers.csv")

# Crear la base de datos SQLite y cargar DataFrames
conn = sqlite3.connect(":memory:")  # Crear base de datos en memoria
calls_df.to_sql("calls", conn, index=False)
customers_df.to_sql("customers", conn, index=False)

# Consulta 1: Ventas totales y llamadas totales para clientes de la profesión de ingeniería
query_engineer = """
SELECT SUM(Ca.ProductSold) AS TotalSales,
       COUNT(*) AS NCalls
FROM calls Ca
JOIN customers Cu ON Ca.CustomerID = Cu.CustomerID
WHERE Cu.Occupation LIKE '%Engineer%';
"""

result_engineer_df = pd.read_sql_query(query_engineer, conn)
print("Resultados para clientes de la profesión de ingeniería:")
print(result_engineer_df)
print()

# Consulta 2: Ventas totales y llamadas totales para toda la base de clientes
query_all = """
SELECT SUM(Ca.ProductSold) AS TotalSales,
       COUNT(*) AS NCalls
FROM calls Ca;
"""

result_all_df = pd.read_sql_query(query_all, conn)
print("Resultados para toda la base de clientes:")
print(result_all_df)
