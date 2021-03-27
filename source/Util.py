def read_movies():
    count = 0
    res = []
    with open('path_to_ movie_file', encoding="utf8") as movies:
        for line in movies:
            if count > 0:
                count += 1
                data = line.split(",")
                if (len(data) == 3):
                    count += 1
                    genres_from_file = data[2].split("|")
                    size = len(genres_from_file)
                    for ind in range(len(genres_from_file)):
                        if genres_from_file[ind].endswith('\n'):
                            genres_from_file[ind] = genres_from_file[ind][:-1]
                    
                    movieId = data[0]
                    title = data[1]
                    genres = genres_from_file
                    movie = {"movieId" : movieId, "title" : title, "genres" : genres}
                    res.append(movie)                    
            else:
                count += 1
        print(f'read {len(res)} movies')        
    return res
