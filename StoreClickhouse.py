import logging
from ClickhouseClient import ClickhouseClient
from classifysentiment import sentimentValueClassification
from datetimerange import DateTimeRange
from googleapi import gcp_nlp
from facebookconnect import getPostID



def time_stamp_fromdate(date):
    logging.info("Get time stamp from data function")
    timeStamp = date + "T00:00:00+0530"
    return timeStamp

def check_time_range(startingTime,endingTime,time):  
    logging.info("Check time is in range function") 
    # Time range creation
    timeRange = DateTimeRange(startingTime,endingTime)

    result = time in timeRange

    return result

def get_list_dict(keys, list_of_tuples):
     # This will get a list of tuples and return a list of dictionaries
     list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
     return list_of_dict
     
def add_sentiment_value(list_of_tuple):
    logging.info("Add sentiment properties function")
    output = []                                             #A list
    for i in list_of_tuple:
        sentiment = gcp_nlp(i[-1])
        sentimentScore = sentiment.score
        sentimentMagnitude = sentiment.magnitude

        i = i + (sentimentScore,sentimentMagnitude)         # Add sentiment score and magnitude into the tuple
        output.append(i)

    return output

def store_clickhouse(GraphAPIObject,database,url,tableName,startingDate,endingDate):
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
        if (check_time_range(time_stamp_fromdate(startingDate),time_stamp_fromdate(endingDate),i['created_time'])==True):
                date_time = i['created_time']
                user_id = int(i['from']['id'])
                user_name = i['from']['name']
                text_id = i['id']
                text = i['message']
                # Tuple
                dataTuple = (date_time,user_id,user_name,text_id,text)
                # Adding created tuple into the list
                listOfTuples.append(dataTuple)
        

    # Add sentiment properties into the data tuples
    sentiment_list = add_sentiment_value(listOfTuples)

    # Convert list of tuples into the list of dictionaries
    list_dict = get_list_dict(['date_time','user_id','user_name','text_id','text','score','magnitude'],sentiment_list)

    # Data insertion into the Clickhouse table
    dbObject.insertData("facebook",tableName,list_dict)

    # Add sentiment value classification column and update values
    sentimentValueClassification("facebook",tableName)
        


