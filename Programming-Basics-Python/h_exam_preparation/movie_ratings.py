import sys

number_of_movies = int(input())

max_rating = -sys.maxsize
max_rating_movie_name = ''
min_rating = sys.maxsize
min_rating_movie_name = ''

average_rating = 0

for _ in range(number_of_movies):             # _ - няма да ни трябва име на променливата
                                              # for i / film / name ....
    name_of_move = input()                # За всеки филм се прочитат два отделни реда: Име на филма и Рейтинг на филма
    rating = float(input())
    average_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_rating_movie_name = name_of_move

    if rating < min_rating:
        min_rating = rating
        min_rating_movie_name = name_of_move

average_rating = average_rating / number_of_movies

print(f"{max_rating_movie_name} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie_name} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")