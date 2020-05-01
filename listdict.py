from googleapi import gcp_nlp

def getListOfDict(keys,list_tuples):
    
     # This will get a list of tuples and return a list of dictionaries
     list_of_dict = [dict(zip(keys, values)) for values in list_tuples]
     return list_of_dict

def add_sentiment(list_tuples):
    
    # Add sentiment score and sentiment magnitude into the tuples

    output = []                                             # Output list
    for i in list_tuples:
        sentiment = gcp_nlp(i[-1])
        senti_score = sentiment.score
        senti_magnitude = sentiment.magnitude

        i = i + (senti_score,senti_magnitude)         # Add sentiment score and magnitude into the tuple
        output.append(i)

    return output

print(__name__)
