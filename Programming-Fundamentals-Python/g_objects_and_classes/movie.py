class Movie:
    __watched_movies = 0  # There should also be a class attribute -  the number of all the watched movies

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):  # changes the name of the movie
        self.name = new_name

    def change_director(self, new_director: str):  # changes the director of the movie
        self.director = new_director

    def watch(self):  # change the watched attribute to True
        if not self.watched:  # if the movie is not already watched
            self.watched = True
            Movie.__watched_movies += 1  # increase the total watched movies class attribute

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. " \
               f"Total watched movies: {self.__watched_movies}"



first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
