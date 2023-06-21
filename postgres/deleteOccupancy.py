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

def deleteOccupancy(city):
    
    dic = {"LA": "losangelesoccupancy",
           "SF": "sanfrancisco"}

    cur.execute("DELETE FROM " + dic[city])
    conn.commit()
    conn.close()
