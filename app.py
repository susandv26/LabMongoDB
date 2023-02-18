import pymongo

from Classes import Estudiante

def main():
    user = 'susan95'
    password = '1234'
    cluster = 'pootest.czbsnmb.mongodb.net'
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

    estudiante = Estudiante("Susan","Delcid","95260937")
    print(estudiante.__dict__)
    collection.insert_one( estudiante.__dict__ )

if __name__ == "__main__":
    main()