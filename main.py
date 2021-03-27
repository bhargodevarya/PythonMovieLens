import mongo.Util as ds
import source.Util as source

movies = source.read_movies()

ds.insert_movies(movies)