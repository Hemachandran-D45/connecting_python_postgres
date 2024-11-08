from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from  model.sql_model import BASE


#database configuration
db_user: str  = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = '4065'
uri:str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/to-do' #sqlalchemy use URI to connect with db


#creating engine : SQLAlchemy engine which serves as the interface to the database. 
# This engine will communicate with postgres
engine = create_engine(uri)

BASE.metadata.create_all(bind=engine)



#session 
#sessionmaker  is  factory function that create new session object.In SQLAlchemy is essentially a "workspace" where you can query and interact with the db.
session = sessionmaker( 
        bind = engine, #SQLAlchemy that the session should be connected to the previously created engine
        autoflush=True #automatically update changes , sync
)
#why use session ?
#The session abstracts database operations so that you can work with Python objects instead of SQL statements


db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print("Connected")
except Exception as e:
    print(str(e))