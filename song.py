class Song:
    def __init__(self, title, singer, genre, duration):
        self.title = title
        self.singer = singer
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} - {self.singer} - {self.genre} - {self.duration}"
        