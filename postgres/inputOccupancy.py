import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
load_dotenv()
import os
from sql import spotsQuery

conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    port=os.getenv('DB_PORT'))

cur = conn.cursor()

def inputOccupancyLosAngeles(data):
    values = [[value for value in datum.values()] for datum in data]
    execute_values(cur, spotsQuery.inputOccupancyLosAngeles, values)   
    
    conn.commit()
    conn.close()

def inputOccupancySanFrancisco(data):
    print(list(data[0].values())[:28])
    values = [[value for value in list(datum.values())[:28]] for datum in data]
    #for value in values[0]: print(type(value))
    print(values)
    execute_values(cur, spotsQuery.inputOccupancySanFrancisco, values)   
    
    conn.commit()
    conn.close()
