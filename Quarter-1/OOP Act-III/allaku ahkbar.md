|           Playlist           |
|------------------------------|
| + name : string              |
| - songs : list               |
| + add_song(song)             |
| + display_songs()            |
              1
              ⇩
           contains
              ⇩
             0..*
              ⇩
|             Song             |
|------------------------------|
| + title : string             |
| + artist : string            |
| + duration : string          |
| - volume : int               |
| + is_playing : bool          |
| + play()                     |
| + pause()                    |
| + change_volume(volume : int)|
| + display_info()             |
