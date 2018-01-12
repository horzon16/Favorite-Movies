# Created by Gerald Ding (horzon16@gmail.com)


class Movie():

    """Class uses to store the informations of my favorite movies.

    The __init__ method is the only part of this class. It will
    help do the storing work for all the movies with the movie's
    title, poster, and trailer.

    Args:
        movie_title(str): The title of the movies.
        poster_image(str): A URL link to a image of the movie's poster.
        trailer_youtube(str): A URL link of Youtube to the movie's trailer.

    Attributes:
        title(str):The title of the movies.
        poster_image_url(str): A URL link to a image of the movie's poster.
        trailer_youtube(str): A URL link of Youtube to the movie's trailer.

    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

