class Song:
    def __init__(self, date_of_release, title, artist, duration, volume=50):
        self.drelease = date_of_release
        self.t = title
        self.a = artist
        self.d = duration
        self._v = volume
        self.is_playing = False

    def play(self):
        self.is_playing = True
        print(f"Playing: {self.t} by {self.a}")

    def pause(self):
        self.is_playing = False
        print(f"Paused: {self.t}")

    def change_volume(self, volume):
        self._v = volume
        print(f"Volume changed to {self._v}")

    def display_info(self):
        print(f"Title: {self.t}")
        print(f"Artist: {self.a}")
        print(f"Duration: {self.d}")
        print(f"Volume: {self._v}")
        print(f"Date of Release: {self.drelease}")
        print(f"Playing: {self.is_playing}")


class Playlist:
    def __init__(self, name):
        self.name = name
        self.__songs = []

    def add_song(self, song):
        self.__songs.append(song)
        print(f"Added '{song.t}' to {self.name}")

    def display_songs(self):
        print(f"\nPlaylist: {self.name}")
        for song in self.__songs:
            print(f"- {song.t} by {song.a}")


p1 = Playlist("My Favorites")

s1 = Song("12-06-2024", "Carol of the Bells", "Geoff Castellucci", "3:14")
s2 = Song("04-08-2018", "Bulong", "December Avenue", "4:30")
s3 = Song("04-12-1971", "Country Roads", "John Denver", "3:10")

print(f"Playlist created: {p1.name}")
print("Songs have been created:")
print(s1.t)
print(s2.t)
print(s3.t)

p1.add_song(s1)
p1.add_song(s2)
p1.add_song(s3)

p1.display_songs()