import webbrowser
import video

class Movie(video.Video):
    """This class is doc"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
        video.Video.__init__(self,movie_title, movie_storyline, poster_image,
                    trailer_youtube)
