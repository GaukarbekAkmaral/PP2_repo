#3
def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'].lower() == category.lower()]

# Example usage:
romance_movies = get_movies_by_category(movies, "Romance")
for m in romance_movies:
    print(m['name'])




#1
def is_good_movie(movie):
    return movie['imdb'] > 5.5

# Example:
print(is_good_movie({
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
}))  # Output: True



#2
def get_good_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# Example usage:
good_movies = get_good_movies(movies)
for m in good_movies:
    print(m['name'])




#4
def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie['imdb'] for movie in movies) / len(movies)

# Example usage:
print("Average IMDb score:", average_imdb(movies))




#5
def average_imdb_by_category(movies, category):
    filtered = get_movies_by_category(movies, category)
    return average_imdb(filtered)

# Example usage:
print("Average IMDb in Romance:", average_imdb_by_category(movies, "Romance"))
