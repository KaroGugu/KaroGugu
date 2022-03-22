import sys
number_of_movies = int(input())             # Брой филми, които си е набелязала Деси

max_rating = -sys.maxsize   # най-висок рейтинг
min_rating = sys.maxsize
sum_rating = 0
max_rating_movie = ""      # име на филма с най-висок рейтинг
min_rating_movie = ""

for movie in range(1, number_of_movies + 1):        # За всеки филм се прочитат два отделни реда
    movie_name = input()
    rating = float(input())
    sum_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_rating_movie = movie_name
    if rating < min_rating:
        min_rating = rating
        min_rating_movie = movie_name

average_rating = sum_rating / number_of_movies

print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")