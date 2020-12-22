from sqlalchemy import create_engine

# GCP--Base
user = 'root'
passw = 'MTIzNDVhcm0='
host =  '34.87.1.57'  
port = 3306 
database = 'stocks_db'

# # armpc
# user = 'root'
# passw = 'wE1dhomxef'
# host =  'localhost'  # either localhost or ip e.g. '172.17.0.2' or hostname address
# port = 3306 
# database = 'stocks_db'

# time zone

engine = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
print(engine)