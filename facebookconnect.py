
from datetime import date
from sample import storeClickhouse
from graphapi import GraphAPI
from storeindatabase import createTableName
access_token = ''



def facebookconnect(url):

    obj = GraphAPI(access_token)
    start_date = "2020-02-20"
    end_date = "2020-05-03"

    # Creating database table name
    table_name = createTableName(obj,url,start_date,end_date)

    # Storing fetched data into Clickhouse
    storeClickhouse(obj,"nlp_database",url,table_name,start_date,end_date)



print(__name__)   




