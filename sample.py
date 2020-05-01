import logging
from databaseclient import ClickhouseClient
from classifysentiment import classify_sentiment_value
from datetimerange import DateTimeRange
from graphapi import GraphAPI
from getpostid import get_postid
from listdict import add_sentiment,getListOfDict
from storeindatabase import checkTimeIsInRange,getTimeStampFromDate


def storeClickhouse(graphapi_obj,database,url,tableName,startingDate,endingDate):
    logging.info("Store Clickhouse function")
    # Retrieve page comments and store them in Clickhouse
    pageID = graphapi_obj.getPageID()                                 # Get the page ID from GraphAPI                                     
    postID = pageID + "_" + get_postid(url)                              # Combine page ID with postID to get correct post ID
    postCommentsList = graphapi_obj.getPostCommentsList(postID)       # Get list of post comments
  
    # Connect with Clickhouse
    logging.info("Initialize database object")
    db_obj = ClickhouseClient(database)

    # Create the table
    db_obj.createTable(database,tableName)
    
    # List of tuples
    listOfTuples = []

    logging.info("Read post comment list")
    for i in postCommentsList:
        # Read each comment one by one
        if (checkTimeIsInRange(getTimeStampFromDate(startingDate),getTimeStampFromDate(endingDate),i['created_time'])==True):
                date_time = i['created_time']
                user_id = int(i['from']['id'])
                user_name = i['from']['name']
                text_id = i['id']
                text = i['message']
                # Tuple
                dataTuple = (date_time,user_id,user_name,text_id,text)
                # Adding created tuple into the list
                listOfTuples.append(dataTuple)
        else: pass

    # Add sentiment properties into the data tuples
    sentimentAddedList = add_sentiment(listOfTuples)

    # Convert list of tuples into the list of dictionaries
    listOfDict = getListOfDict(['date_time','user_id','user_name','text_id','text','score','magnitude'],sentimentAddedList)

    # Data insertion into the Clickhouse table
    db_obj.insertData('nlp_database',tableName,listOfDict)

    # Add sentiment value classification column and update values
    classify_sentiment_value('nlp_database',tableName)