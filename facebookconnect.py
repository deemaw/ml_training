
from datetime import date
from sample import storeClickhouse
from graphapi import GraphAPI
from storeindatabase import createTableName
access_token = 'EAAC3hQgXvR4BABF2H3J6iddco0TNoR3YdVRqF3Btuy6Afz4byxwtWH2wbfPtsu2kmrzxkFTO19FttAtXO5pZC07YNtlrS8KUQ7jf5ePBCkw4Lmj4CXvnHTvfzHUIZCdEmb0bIwb5OjDJmVYtXjtRtPAlE7KAZCdXNOYSiMY5zeUJOx1vxZAASVg5J62LwT7ie6EKfoZCqxGuqDhYDGSku7dyrBpGFkNNPPf902qfsmriAr702zZAzm'



def facebookconnect(url):

    obj = GraphAPI(access_token)
    start_date = "2020-02-20"
    end_date = "2020-04-29"

    # Creating database table name
    table_name = createTableName(obj,url,start_date,end_date)

    # Storing fetched data into Clickhouse
    storeClickhouse(obj,"nlp_database",url,table_name,start_date,end_date)



print(__name__)   


