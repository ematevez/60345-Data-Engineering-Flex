import pandas as pd
import sqlite3

# Cargar datos desde archivos CSV
calls_df = pd.read_csv("calls.csv")
customers_df = pd.read_csv("customers.csv")
agents_df = pd.read_csv("agents.csv")  # Corregí la variable

# Crear la base de datos SQLite y cargar DataFrames
conn = sqlite3.connect(":memory:")  # Crear base de datos en memoria
calls_df.to_sql("calls", conn, index=False)
customers_df.to_sql("customers", conn, index=False)
agents_df.to_sql("agents", conn, index=False)  # Agregué esta línea

# Consulta 1: Ventas totales y llamadas totales para clientes de la profesión de ingeniería
query_engineer = """
SELECT A.Name AS AgentName, 
       COUNT(*) AS NCalls, 
       MIN(C.Duration) AS Shortest, 
       MAX(C.Duration) AS Longest, 
       ROUND(AVG(C.Duration), 2) AS AvgDuration, 
       SUM(C.ProductSold) AS TotalSales
FROM calls C
JOIN customers Cu ON C.CustomerID = Cu.CustomerID
JOIN agents A ON C.AgentID = A.AgentID
WHERE C.PickedUp = 1
GROUP BY A.Name
ORDER BY A.Name;
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


