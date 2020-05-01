
from datetime import date
from sample import storeClickhouse
from graphapi import GraphAPI
from storeindatabase import createTableName
access_token = 'EAAC3hQgXvR4BAGyrn3W4vAaEfxeZBSxrB8h1QbUQSILoqflPBSS5mwLeluB0Bgdm2cRkqe2AqZB6wy4jV1gAe9vV1kkZCQEr786zhr0JNIjtwrPtlODvG9JZBxn6ili7FOI1W7ZBReDhxxqrQefplZCNKKPXmSstbWhYl2Y3PpkveQEdnno7uf9N7ccp7ffv08IA1ko0TGYHn9U3hVuK1W'

fbu = 'https://www.facebook.com/Cat-fish-102637431312984/?__tn__=kC-R&eid=ARA5wgpmbCDnN2Lc0zzzzbmq0ZfbkLvoC8dFO-3MFpXB3gUGVvZNQV8qqrbvZdK_EE7PMKnCSis9qLer&hc_ref=ARRpO11OeMJAh9Z5SNUlzhheF65P9BMofB8c0SIPbvoayMQ8mpfYslQIDbQFAFPQi2s&fref=nf&__xts__[0]=68.ARCg1mDXEY-xGbkXtpocC5EyblVeJkdh6kD2ynxFnyV9mqWtxbaP0vTPdnG1AuFeZAhM8P8Mv20U34s4ax7BZkaRL_UaVdzcSkKX21M4O_lGo1WAYVjLxzFxcitTzy4wIBXTXgkpYSuldjhg0JrqfkznvOzc0ftynPzFsjs_-jm87Rsm4ovswAMC-BFSKPoqvPy3MIKnoOb4Xv0LGh1DiKPEPb-ofjHAliXJoRLcVFwmChtplIlvXVMed6fbV0a0cEUXZOoC2rSz6ZOt0i72nPdcxKVRIjboZWVxHh91uUZ14kwDqTKBuKKI4GKWeYyf3pL175tQ9DRpZ65CoRg'

def facebookconnect(url):

    obj = GraphAPI(access_token)
    start_date = "2020-02-20"
    end_date = "2020-04-29"

    # Creating database table name
    table_name = createTableName(obj,url,start_date,end_date)

    # Storing fetched data into Clickhouse
    storeClickhouse(obj,"nlp_database",url,table_name,start_date,end_date)



print(__name__)   


det =  facebookconnect(fbu)

print(det) 