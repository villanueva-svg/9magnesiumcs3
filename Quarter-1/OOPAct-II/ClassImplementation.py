class Song:
    def __init__(self, title, artist, duration, volume=50):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.__volume = volume
        self.is_playing = False

    def play(self):
        self.is_playing = True
        print(f"Playing: {self.title} by {self.artist}")

    def pause(self):
        self.is_playing = False
        print(f"Paused: {self.title}")

    def change_volume(self, volume):
        self.__volume = volume
        print(f"Volume changed to {self.__volume}")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Duration: {self.duration}")
        print(f"Volume: {self.__volume}")
        print(f"Playing: {self.is_playing}")


song1 = Song("Carol of the Bells", "Geoff Castellucci", "3:14")

song1.play()
song1.display_info()
song1.change_volume(70)
song1.pause()

song2 = Song("Bulong", "December Avenue", "4:30")

song2.play()
song2.display_info()
song2.pause()