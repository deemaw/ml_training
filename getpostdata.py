import facebook
import json



class GetPost:

    def __init__(self, api):
        token = api["access_token"]
        id = api["id"]
        self.graph = facebook.GraphAPI('EAAC3hQgXvR4BANL1cWZCCrDBB4aeJTFJUMfk98gyA2QBZAA1uaeWEa6AaPY6csb27vultbx7WW0IcRei5eIlozHok7bOBZC3YCInoaKJd10LtS3vGdj32oZC37BO6Mc3BkVJ1BZBUhKBWWrR0YZBq0uQZAsIAg9r9ZBZAyes6145PAOl7LMsNrISOoM6q8Gekw018eOEIwz3gFQZDZD')
# curl -i -X GET "https://graph.facebook.com/{page-id}?fields=access_token&access_token={user-access-token}"

        def fetch_facebook_post_comments(
            self,
            graph,
            id,
            limit=20):
       

        # search post based on post id
            post = self.graph.get_object(id,
                                     fields='full_picture,message,caption,created_time,comments{id,from,message,created_time}')

        # get the data for array of comments
            comment_data = post['comments']['data']





        
