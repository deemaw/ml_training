from googleapi import gcp_nlp

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
