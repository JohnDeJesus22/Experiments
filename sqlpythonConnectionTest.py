#Test psycopg2 connection

#import psycopg2
import psycopg2

#establish connection
conn=psycopg2.connect(database='Test Database',
                            user='postgres',password='password',host='localhost')
#set cursor
cursor=conn.cursor()

#test a query
purchases = cursor.execute("SELECT * FROM purchases")

#print rows of purchases table
for row in cursor:
    print(row)

###########################################################################################
#import objects from sqlalchemy
from sqlalchemy import create_engine,Table, MetaData,select

#establish connection
engine=create_engine('postgresql+psycopg2://postgres:password@localhost/Test Database')

#print table names
print(engine.table_names())

#import table by initializing metadata container object
metadata=MetaData()
purchases_sqlal = Table('purchases',metadata, autoload=True, autoload_with=engine)

#get columns
print(purchases_sqlal.columns.keys())

#assign query to a variable with python sqlalchemy select
result=select([purchases_sqlal])

#print table rows and assign to a variable
print(engine.execute(result).fetchall())
results= engine.execute(result).fetchall()

#get second row and print the row and the entry in the third column
second_row=results[1]
print(second_row)
print(second_row[2])
