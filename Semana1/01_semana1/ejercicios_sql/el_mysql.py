from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd


# Load environment variables from .env
load_dotenv()


# Access the variables
passw = os.getenv('localhost_pass')

# Creo engine
engine = create_engine(
    f"mysql+pymysql://root:{passw}@localhost/coder_house_semana_1"
)

agents = pd.read_csv(r"G:\My Drive\02_education\07_coderHouse\01_semana1\ejercicios_sql\datasets\agents.csv")
calls = pd.read_csv(r"G:\My Drive\02_education\07_coderHouse\01_semana1\ejercicios_sql\datasets\calls.csv")
customers = pd.read_csv(r"G:\My Drive\02_education\07_coderHouse\01_semana1\ejercicios_sql\datasets\customers.csv")

agents.to_sql(con=engine, name = 'agents',if_exists='append',index=False)
calls.to_sql(con=engine, name = 'calls',if_exists='append',index=False)
customers.to_sql(con=engine, name = 'customers',if_exists='append',index=False)