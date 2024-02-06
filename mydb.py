import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

dataBase = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
)

cursorObject = dataBase.cursor()

db_name = os.getenv('DB_NAME')

cursorObject.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')

print('Database created successfully')
