import psycopg2
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

def get_spots(city):
    dic = {"LA": spotsQuery.getSpotsLosAngeles,
           "SF": spotsQuery.getSpotsSanFrancisco}
    cur.execute(dic[city])
    

    spotdata = cur.fetchall()
    conn.commit()
    conn.close()
    return spotdata
