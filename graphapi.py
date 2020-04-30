import logging
import requests


class GraphAPI:

    def __init__(self, access_token):
        logging.info("Graph API function")
        self.access_token = access_token

    def getPageID(self):
        logging.info("Get page ID function")
        # Get the id of the page
        url = "https://graph.facebook.com/v3.3/me?access_token={}".format(self.access_token)
        result = requests.get(url).json()
        return result['id']

    def getPageName(self):
        logging.info("Get page name function")
        # Get the name of the page
        url = "https://graph.facebook.com/v3.3/me?access_token={}".format(self.access_token)
        result = requests.get(url).json()
        return result['name']

    def getPagePostsList(self,pageID):
        logging.info("Get page post list function")
        # Get the list of posts of the page
        url = "https://graph.facebook.com/v3.3/{}/posts?access_token={}".format(pageID,self.access_token)
        result = requests.get(url).json()
        return result['data']

    def getPostCommentsList(self,post_id):
        logging.info("Get page comments list function")
        # Get the list comments of the specific post
        url = "https://graph.facebook.com/v6.0/{}/comments?access_token={}".format(post_id,self.access_token)
        result = requests.get(url).json()
        return result['data']

print(__name__)
# obj = GraphAPI('EAAC3hQgXvR4BAPPFaDKuZBJxSnj9KjpJzXCN35jmkpmwZCxKd1W9bqFfU73ZCFc8OVMhn36Gtuu6egAuFDgLSRVIyhF8iaqRJepeLC1X3DkBq5DaXOip6DhyrdL2ieZAZAXAi98w0RSXSWdmuAWo0jmIOdOW27eWpd4sPyDhQSrMdWU2uqRRRpwy4c8TiGXqLEfO4iO0ma89FGvue6Qo8tkipQvpZBNxQEtwHNKXPMFSzhLTmyb0Uh')

# print(obj.getPageID())
# print(obj.getPageName())
# print(obj.getPagePostsList("102636517979742"))
# print(obj.getPostCommentsList('102636517979742_102637431312984'))

