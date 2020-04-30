import requests
import json
import sys
import time

class FacebookScraper:
    '''
    FacebookScraper class to scrape facebook info
    '''

    def __init__(self, token):
        self.token = token

    def get_feed_data(self, target_page):
        """
        This method will get the feed data
        """
        url = "https://graph.facebook.com/v6.0/{}/feed".format(target_page)
        param = dict()
        param["access_token"] = self.token

        r = requests.get(url, param)
        data = json.loads(r.text)
        
        

        return data

token = 'EAAC3hQgXvR4BAIbQnM1kZCUZBo8dxW7hHwgsaGqHCUlsvllVKlxMTlYzRqTRQodWRLZBdL7PFVc3d8g47Jvyok8ZCX09NgtCiFWC0JaWjReZBzDbMt1U5WZAy64543IoxF1ZAWmfUAYVDlyLvy9gPWKue3lnR32QBo5pZCkhZBk2jh7PLW6mI2xPpnSZA5tufOkZCH5hXtoxrY2mZBeAQzSeg44M'
obj = FacebookScraper(token)
print(obj.get_feed_data('Cat fish'))
    