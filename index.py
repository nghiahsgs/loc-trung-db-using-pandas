  
from high_order_framework_requests_python import utils_class
# from utils_db import *
from sqlalchemy import create_engine
import pymysql
import pandas as pd

# db_connection_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM product', con=db_connection)


df=df.drop_duplicates(subset=['href'])
df.to_csv('b.csv')
