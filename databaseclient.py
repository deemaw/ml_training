import logging
from clickhouse_driver import Client

client = Client('10.0.0.30')


def create_db(database):
    # create databases in clickhouse server
    query = 'CREATE DATABASE {}'.format(database)
    client.execute(query)

def show_db():
   
    # Return databases in clickhouse server
    query = "SHOW DATABASES;"
    client.execute(query)

def drop_db(database):
    # create databases in clickhouse server
    query = 'DROP DATABASE {}'.format(database)
    client.execute(query)

        
class ClickhouseClient:

    def __init__(self,database):
        self.database = database
        
    # Queries for tables
    def show_table(self,database):
        logging.info("Show tables function")
        # Return tables in specific database
        query = 'SHOW TABLES FROM {};'.format(database)
        return client.execute(query)

    def createTable(self,database,tableName):
        # Create a new table in clickhouse server
        # Drop the table if table name already exists
        self.dropTable(database,tableName)
        # Create the table
        query = 'CREATE TABLE {}.{} (date Date DEFAULT today(), date_time String, user_id UInt64, user_name String, text_id String, text String, score Float32, magnitude Float32) ENGINE = MergeTree(date, (date), 8192);'.format(database,tableName)
        client.execute(query)
        

    def insertData(self,database,tableName,listOfDict):
        query = 'INSERT INTO {}.{} (date_time,user_id,user_name,text_id,text,score,magnitude) VALUES'.format(database,tableName)
        client.execute(query,listOfDict)
     

    def selectData(self,database,tableName):
        # Retrive table data
        query = 'SELECT * FROM {}.{};'.format(database,tableName)
        return client.execute(query)

    def dropTable(self,database,tableName):
        logging.info("Drop table function")
        # Drop the table
        query = 'DROP TABLE IF EXISTS {}.{};'.format(database,tableName)
        client.execute(query)
        logging.info("Table is dropped successfully")

    # Additional Functions
    def dropAllTables(self,database):
        logging.info("Drop all tables function")
        # Drop all all tables from database
        # Drop current database
        self.dropDatabase(database)
        # Create a new database
        self.createDatabase(database)

    def addColumn(self,database,tableName,columnName,dataType):
        logging.info("Add new column function")
        # Add column to existing table
        query = 'ALTER TABLE {}.{} ADD COLUMN {} {};'.format(database,tableName,columnName,dataType)
        client.execute(query)

    def updateColumn(self,database,tableName,updateColumnName,updateColumnValue,fWhereColumnName,fWhereColumnValue,sWhereColumnName,sWhereColumnValue):
        
    
        query = "ALTER TABLE {}.{} UPDATE {}={} WHERE {}={} AND {}={};".format(database,tableName,updateColumnName,updateColumnValue,fWhereColumnName,fWhereColumnValue,sWhereColumnName,sWhereColumnValue)
        client.execute(query)

    def selectColumn(self,database,tableName,columnName):
        logging.info("Select column function")
        query = 'SELECT {} FROM {}.{};'.format(columnName,database,tableName)
        return client.execute(query)

# db = DB('red')
# drop = drop_db('rat')

# obj = ClickhouseClient("nlp_database")
# # li=dict[date_time: '2020-03-18+0000' ,user_id:'102636517979742',user_name:'Cat fish', text_id:'102637387979655_125871205656273',text:'Extant catfish'] 
# obj.createTable("nlp_database","facebook")
# # obj.insertData('twitter','facebook',listOfDictionari)
# liste =[("102637387979655","Cat fish","102637387979655_125871205656273","Extant catfish",0.008,0.099)]

# obj.insertData("nlp_database","facebook",liste)




# obj.updateColumn("facebook","F_102699651071355_105714230769897_20190501_2019123","classifiaction",)
 


print(__name__)   