import media
import fresh_tomatoes

# definitions for the three movies.
toy_story = media.Movie("Toy Story", "Andy's toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "Humans attempt to mine on an alien planet and deal with the native life",  # noqa
                     "https://resizing.flixster.com/wmwaS9C76fnLpML3UAj0i3l6djw=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDU0OzEyMDA7ODAwOzEyMDA",  # noqa
                     "https://www.youtube.com/watch?v=Bl8fkc4HsSs")
no_country_for_old_men = media.Movie("No Country For Old Men",
                                     "A Sheriff on the brink of retirement must catch a Serial Killer",  # noqa
                                     "http://static.rogerebert.com/uploads/movie/movie_poster/no-country-for-old-men-2007/large_6o0UWX2naW7HK45PDNYmoMIk5qs.jpg",  # noqa
                                     "https://www.youtube.com/watch?v=qnwNuG1ayno")  # noqa

# putting the movies into a list and supplying the list to the website.
movies = [toy_story, avatar, no_country_for_old_men]
fresh_tomatoes.open_movies_page(movies)
