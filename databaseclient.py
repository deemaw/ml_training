
from clickhouse_driver import Client

client = Client('10.0.0.30')


def create_db(database):
    query = 'CREATE DATABASE {}'.format(database)
    client.execute(query)

def drop_db(database):
    # create databases in clickhouse server
    query = 'DROP DATABASE {}'.format(database)
    client.execute(query)

        
class ClickhouseClient:

    def __init__(self,database):
        self.database = database

    def createTable(self,database,tableName):
        
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

        query = 'DROP TABLE IF EXISTS {}.{};'.format(database,tableName)
        client.execute(query)

    # Additional Functions
    def dropAllTables(self,database):

        self.dropDatabase(database)
        # Create a new database
        self.createDatabase(database)

    def addColumn(self,database,tableName,columnName,dataType):
  
        # Add column to existing table
        query = 'ALTER TABLE {}.{} ADD COLUMN {} {};'.format(database,tableName,columnName,dataType)
        client.execute(query)

    def updateColumn(self,database,tableName,updateColumnName,updateColumnValue,fWhereColumnName,fWhereColumnValue,sWhereColumnName,sWhereColumnValue):
        
    
        query = "ALTER TABLE {}.{} UPDATE {}={} WHERE {}={} AND {}={};".format(database,tableName,updateColumnName,updateColumnValue,fWhereColumnName,fWhereColumnValue,sWhereColumnName,sWhereColumnValue)
        client.execute(query)

    def selectColumn(self,database,tableName,columnName):
        query = 'SELECT {} FROM {}.{};'.format(columnName,database,tableName)
        return client.execute(query)



# obj = ClickhouseClient("nlp_database")

# liste =[("102637387979655","Cat fish","102637387979655_125871205656273","Extant catfish",0.008,0.099)]


