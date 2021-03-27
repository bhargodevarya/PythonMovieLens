import pymongo

client = pymongo.MongoClient('mongodb+srv://<username>:<pwd>@mongoml.j4gp9.mongodb.net/movielensdb?retryWrites=true&w=majority')

db = client['mongoml']

movies_collection = db['movies']

def insert_movies(movies):
    print(f'Inserting {len(movies)} movies')
    insert_result = movies_collection.insert_many(movies)
    print(f'Result for insertion {insert_result}')
    
