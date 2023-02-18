import pymongo

def main():
    user = 'susan26'
    password = 'Poke262414'
    cluster = 'testpoo.0m9cazy.mongodb.net'
    query_string = 'retryWrites=true&w=majority'


    ## Connection String
    uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
        user
        , password
        , cluster
        , query_string
    )

    client = pymongo.MongoClient(uri)
    db = client['unah']
    collection = db['estudiante']