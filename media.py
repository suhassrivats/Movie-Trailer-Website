import webbrowser


class Movie:

    """ This class provides a way to store movie related information """
    # We might have class attributes here (NOT instance attributes).

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        __init__ method fetches all the arguments of this class.

        Listed below is the list of arguments for every instance of this class:
        Args:
            movie_title (str): Title of a movie
            movie_storyline (str): Caption of a movie
            poster_image (str): A URL link to the movie poster
            trailer_youtube (str): A Youtube URL for movie trailer

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens the browser and plays a trailer in Youtube based on
        the Youtube URL

        """
        webbrowser.open(self.trailer_youtube_url)
