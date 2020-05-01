

from datetimerange import DateTimeRange
from graphapi import GraphAPI
from getpostid import get_postid

def createTableName(apiobj,url,start_date,end_date):
    pageID = apiobj.getPageID()                                 # Get the page ID from GraphAPI
    postID = pageID + "_" + get_postid(url)                              # Combine page ID with postID to get correct post ID

    # To remove dashes and concatenate all the elements
    newStartingDate = ''.join((start_date.split('-')))
    newEndingDate = ''.join((end_date.split('-')))

    tableName = "F_" + postID + "_" + newStartingDate + '_' + newEndingDate

    return tableName



def getTimeStampFromDate(date):

    time_stamp = date + "T00:00:00+0530"
    return time_stamp

def checkTimeIsInRange(startingTime,endingTime,time):   
    # Time range creation
    time_range = DateTimeRange(startingTime,endingTime)

    result = time in time_range

    return result

print(__name__)  
