import webbrowser
# We import this module to use it's open function
# to open a web browser to a given address.


class Movie:

    """This class can be used to store attributes and functions of a movie"""

# Using the contructor to declare and initialize the instance variables
    def __init__(self, title, story_line, poster_image_url, trailer_url):

        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url

# Following method is defined to open the movie trailer with the given url
# in the trailer_youtube_url instance variable.

    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
