import logging
import requests


class GraphAPI:

    def __init__(self, access_token):
        logging.info("Graph API function")
        self.access_token = access_token

    def getPageID(self):
        logging.info("Get page ID function")
        # Get the id of the page
        url = "https://graph.facebook.com/v6.0/me?access_token={}".format(self.access_token)
        result = requests.get(url).json()
        return result['id']

    def getPageName(self):
        logging.info("Get page name function")
        # Get the name of the page
        url = "https://graph.facebook.com/v6.0/me?access_token={}".format(self.access_token)
        result = requests.get(url).json()
        return result['name']

    def getPagePostsList(self,pageID):
        logging.info("Get page post list function")
        # Get the list of posts of the page
        url = "https://graph.facebook.com/v6.0/{}/posts?access_token={}".format(pageID,self.access_token)
        result = requests.get(url).json()
        return result['data']

    def getPostCommentsList(self,post_id):
        logging.info("Get page comments list function")
        # Get the list comments of the specific post
        url = "https://graph.facebook.com/v6.0/{}/comments?access_token={}".format(post_id,self.access_token)
        result = requests.get(url).json()
        return result['data']



