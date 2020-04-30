import logging
from datetime import date

from graphapi import GraphAPI
from storeindatabase import store_clickhouse
from databaseclient import ClickhouseClient
access_token = 'EAAC3hQgXvR4BABF2H3J6iddco0TNoR3YdVRqF3Btuy6Afz4byxwtWH2wbfPtsu2kmrzxkFTO19FttAtXO5pZC07YNtlrS8KUQ7jf5ePBCkw4Lmj4CXvnHTvfzHUIZCdEmb0bIwb5OjDJmVYtXjtRtPAlE7KAZCdXNOYSiMY5zeUJOx1vxZAASVg5J62LwT7ie6EKfoZCqxGuqDhYDGSku7dyrBpGFkNNPPf902qfsmriAr702zZAzm'

url = 'https://www.facebook.com/deemamiyu/posts/3001680149878521?comment_id=3003156719730864&notif_id=1588239159582467&notif_t=feed_comment&ref=notif'
def facebookconnect(url):

    obj = GraphAPI(access_token)
    start_date = "2020-02-20"
    end_date = "2020-04-29"

    # Creating database table name
    table_name = createTableName(obj,url,start_date,end_date)

    # Storing fetched data into Clickhouse
    store_clickhouse(obj,"nlp_database",url,table_name,start_date,end_date)

def get_postid(url):
    logging.info("Get post ID function")
    # Get the id of fb post
    startingindex = findSubstringIndex(url, "story_fbid") + len("story_fbid") + 1
    endingindex = findSubstringIndex(url, "&id=")
    return url[startingindex:endingindex]

def findSubstringIndex(string, substring):
    logging.info("Find substring index function")
    # Get the starting index of substring
    index = 0
    if substring in string: 
        c = substring[0]
        for ch in string:
            if ch == c:
                if string[index:index+len(substring)] == substring:
                    return index
            index += 1
    return -1

def createTableName(obj,url,starting_date,ending_date):
    logging.info("Create table name function")
    pageID = obj.getPageID()                                 # Get the page ID from GraphAPI
    postID = pageID + "_" + get_postid(url)                              # Combine page ID with postID to get correct post ID

    # To remove dashes and concatenate all the elements
    newStartingDate = ''.join((starting_date.split('-')))
    newEndingDate = ''.join((ending_date.split('-')))

    tableName = "F_" + postID + "_" + newStartingDate + '_' + newEndingDate

    return tableName

table =createTableName(access_token,url,"2020-02-20","2020-04-29")

entry = ClickhouseClient('nlp_database')
entry.createTable('nlp_database',tableName)

print()
print(__name__)   


