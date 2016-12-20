import media
import fresh_tomatoes


"""
Create Movie Objects
Movie data is hard coded here
"""
pulp_fiction = media.Movie("Pulp Fiction",
                           "What's in the case?",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")

matrix = media.Movie("Matrix",
                     "A movie about the reality of life itself.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

true_romance = media.Movie("True Romance",
                           "Who says romance is dead?",
                           "http://ia.media-imdb.com/images/M/MV5BMTMxMTM3MDIwM15BMl5BanBnXkFtZTcwMDYyOTUyMg@@._V1_SX214_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=_wNYNDzKpuQ")

the_godfather = media.Movie("The Godfather",
                            "Every time he tries to get out,"
                            " they pull him back in",
                            "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=YBrs0wvkPls")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "A great escape from Prison",
                                   "http://t0.gstatic.com/images?"
                                   "q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",  # NOQA
                                   "https://www.youtube.com/watch?v=NmzuHjWmXOc",  # NOQA
                                   )


above_the_rim = media.Movie("Above the Rim",
                            "A promising New York City high school basketball"
                            " star and his relationships with two people.",
                            "http://upload.wikimedia.org/wikipedia/en/b/b6/Above_the_rim_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=sEsCXWD7-Cc")

# Make a list of all the movies
movies = [pulp_fiction, matrix,
          true_romance, the_godfather,
          shawshank_redemption,
          above_the_rim
          ]

# Send the movies list to 'open_movies_page' method in 'fresh_tomatoes.py'
# module
fresh_tomatoes.open_movies_page(movies)
