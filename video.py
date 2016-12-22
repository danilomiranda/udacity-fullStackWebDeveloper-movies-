class Video():
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
