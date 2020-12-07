  
from sqlalchemy import create_engine
import pymysql
import pandas as pd

# B1: loc trung

ip_vps='45.77.36.114'
db_name='auto_spam_ib_cho_tot'
username='nghiahsgs4'
password='261997'

db_connection_str = 'mysql+pymysql://%s:%s@%s/%s'%(username,password,ip_vps,db_name)

db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM spam_user', con=db_connection)


df=df.drop_duplicates(subset=['link_chat'])
# df.to_csv('b.csv')


# B2: import nguoc lai db