from pymysql import connect
import dotenv
import os

def connectDb():
  dotenv.load_dotenv()

  user=os.getenv('DB_USER')
  passwd=os.getenv('DB_PASSWORD')
  database=os.getenv('DB_NAME')
  host=os.getenv('DB_HOST')

  db = connect(
    user=user, 
    passwd=passwd,
    host=host,
    database=database
    )
  print(f'Connected to {database}')
  return db