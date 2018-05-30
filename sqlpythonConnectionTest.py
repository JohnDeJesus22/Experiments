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
from sqlalchemy import create_engine,Table, MetaData,select,insert

#establish connection
engine=create_engine('postgresql+psycopg2://postgres:password@localhost:/Test Database')

#connection
conn=engine.connect()

#print table names
print(engine.table_names())

#import table by initializing metadata container object
metadata=MetaData()
purchases_sqlal = Table('purchases',metadata, autoload=True, autoload_with=engine)

#get columns
print(purchases_sqlal.columns.keys())
columns=list(purchases_sqlal.columns.keys())

#assign query to a variable with python sqlalchemy select
result=select([purchases_sqlal])

#print table rows and assign to a variable
print(conn.execute(result).fetchall())
results= conn.execute(result).fetchall()

#get second row and print the row and the entry in the third column
second_row=results[1]
print(second_row)
print(second_row[2])

#practice with a where clause
result=result.where(purchases_sqlal.columns.id <= 5)
results=conn.execute(result).fetchall()

#print out info from results after where clause
for result in results:
    print(result.id, result.item_id,result.customer_id)
    
#get total number of rows
print(results.rowcount)

#insert an item into the table
stmt=insert(purchases_sqlal).values(id=11,item_id=7,customer_id=20,valid=True)

#execute query
new_result=conn.execute(stmt)