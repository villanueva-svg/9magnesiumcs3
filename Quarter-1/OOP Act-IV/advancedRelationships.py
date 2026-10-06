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
        print(f"Date of Release: {self.drelease}")
        print(f"Artist: {self.a}")
        print(f"Duration: {self.d}")
        print(f"Volume: {self._v}")
        print(f"Playing: {self.is_playing}")


class LiveSong(Song):
    def __init__(self, date_of_release, title, artist, duration, venue, volume=50):
        super().__init__(date_of_release, title, artist, duration, volume)
        self.ven = venue

    def display_live_info(self):
        print(f"Title: {self.t}")
        print(f"Date of Release: {self.drelease}")
        print(f"Artist: {self.a}")
        print(f"Duration: {self.d}")
        print(f"Venue: {self.ven}")


class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)
        print(f"Added '{song.t}' to {self.name}")

    def display_songs(self):
        print(f"\nPlaylist: {self.name}")
        for song in self._songs:
            print(f"- {song.t} by {song.a}")


p1 = Playlist("My Favorites")

s1 = Song(
    "12-06-2024",
    "Carol of the Bells",
    "Geoff Castellucci",
    "3:14"
)

s2 = Song(
    "04-08-2018",
    "Bulong",
    "December Avenue",
    "4:30"
)

live_s1 = LiveSong(
    "04-12-1971",
    "Country Roads",
    "John Denver",
    "3:10",
    "Live Concert"
)


print("LiveSong inherited features from Song:")
print(f"Title: {live_s1.t}")
print(f"Artist: {live_s1.a}")
print(f"Duration: {live_s1.d}")
print(f"Venue: {live_s1.ven}")

live_s1.play()

print(f"Playlist: {p1.name}")

p1.add_song(s1)
p1.add_song(s2)
p1.add_song(live_s1)

print("\nSongs in playlist:")
p1.display_songs()