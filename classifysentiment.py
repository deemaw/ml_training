import logging
from databaseclient import ClickhouseClient
from nnnmodel import modelOutput

def classify_sentiment_value(db_name,table_name):
    db_object = ClickhouseClient("nlp_database")

    # Adding new column to existing table
    db_object.addColumn(db_name,table_name,"classification","Float32")

    # Read sentiment score and magnitude from the table
    # logging.info("Read score and magnitude from Clickhouse")
    score = db_object.selectColumn(db_name,table_name,'score')
    magnitude = db_object.selectColumn(db_name,table_name,'magnitude')

    # Calculate number of records
    records = len(score)

    for i in range(0,records):
        # Neural network output
        nn_output = modelOutput(score[i][0],magnitude[i][0])

        # Rounding the values according to the sentiment levels
        logging.info("Label the sentiment levels")
        if (0<=nn_output<=0.2):
            nn_output = 0
        elif (0.8<=nn_output<=1):
            nn_output = 1
        else:
            nn_output = 0.input_array # Update the table records
            
        db_object.updateColumn(db_nameinput_arraye,"classification",nn_output,"score",score[i][0],"magnitude",magnitude[i][0])






