import logging
from databaseclient import ClickhouseClient
from classifysentiment import classify_sentiment_value
from datetimerange import DateTimeRange
from googleapi import gcp_nlp
from graphapi import GraphAPI


def addSentimentProperties(listOfTuples):
    logging.info("Add sentiment properties function")
    # Add sentiment score and sentiment magnitude into the tuples

    output = []                                             # Output list
    for i in listOfTuples:
        sentiment = gcp_nlp(i[-1])
        sentimentScore = sentiment.score
        sentimentMagnitude = sentiment.magnitude

        i = i + (sentimentScore,sentimentMagnitude)         # Add sentiment score and magnitude into the tuple
        output.append(i)

    return output


def getTimeStampFromDate(date):
    logging.info("Get time stamp from data function")
    timeStamp = date + "T00:00:00+0530"
    return timeStamp

def checkTimeIsInRange(startingTime,endingTime,time):  
    logging.info("Check time is in range function") 
    # Time range creation
    timeRange = DateTimeRange(startingTime,endingTime)

    result = time in timeRange

    return result

def storeClickhouse(GraphAPIObject,database,url,tableName,startingDate,endingDate):
    logging.info("Store Clickhouse function")
    # Retrieve page comments and store them in Clickhouse
    pageID = GraphAPIObject.getPageID()                                 # Get the page ID from GraphAPI                                     
    postID = pageID + "_" + getPostID(url)                              # Combine page ID with postID to get correct post ID
    postCommentsList = GraphAPIObject.getPostCommentsList(postID)       # Get list of post comments
  
    # Connect with Clickhouse
    logging.info("Initialize database object")
    dbObject = ClickhouseClient(database)

    # Create the table
    dbObject.createTable('facebook',tableName)
    
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
    sentimentAddedList = addSentimentProperties(listOfTuples)

    # Convert list of tuples into the list of dictionaries
    listOfDict = getListOfDict(['date_time','user_id','user_name','text_id','text','score','magnitude'],sentimentAddedList)

    # Data insertion into the Clickhouse table
    dbObject.insertData("facebook",tableName,listOfDict)

    # Add sentiment value classification column and update values
    classify_sentiment_value("facebook",tableName)
        
print(__name__)  

