# Coded by Oto Tabares

import webbrowser


class Movie():
    """Provide a way to store movie-related information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, mpaa_rating, duration, release_year):
        """
        Behavior: Construct a Movie object.
        Inputs:
            movie_title (str): Title of the movie.
            movie_storyline (str): Plot summary.
            poster_image (str): Link to an image of the movie poster.
            trailer_youtube (str): Link to the trailer in YouTube.
            mpaa_rating (str): MPAA Rating.
            duration (str): Duration in hours and minutes.
            release_year (str): Year on which the movie was released.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.mpaa_rating = mpaa_rating
        self.duration = duration
        self.release_year = release_year

    def show_trailer(self):
        """Open the movie trailer in a web browser."""
        webbrowser.open(self.trailer_youtube_url)
