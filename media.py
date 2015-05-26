class Movie():
    """The Movie class stores data about movies"""
    
    def __init__(self, title, poster_url, trailer_url, story_line, imdb_rating):
        """ Initialize a Movie object """    
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.story_line = story_line
        self.imdb_rating = imdb_rating
