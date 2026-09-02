Class Name: Song

Class Description:
The "Song" class represents a song that can be stored and managed by a music player, also containing information on what can be done to them: play, pause, and change volume.

Properties
| Property   | Data Type | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| title      | string    | The title of the song                              |
| artist     | string    | The name of the artist                             |
| duration   | double    | The duration of the song in seconds                |
| isFavorite | boolean   | Indicates whether the song is marked as a favorite |

Methods
| Method                     | Description                                |
| -------------------------- | ------------------------------------------ |
| play()                     | Plays the song                             |
| pause()                    | Pauses the song                            |
| changeVolume(amount : int) | Changes the volume by the specified amount |


Class Diagram
|                 Song                 |
|--------------------------------------|
| title : string                       |
| artist : string                      |
| duration : double                    |
| isFavorite : boolean                 |
|--------------------------------------|
| play()                               |
| pause()                              |
| changeVolume(amount : int)           |

Design Explanation:

Why did you choose this class?
I chose the Song class because I looked at it, got an idea, and decided to roll with it.

Which property is the most important? Why?
I think the title is the most important property because it identifies the song and lets the user know what song is being played if they happen to forget what song they put in their music player.

Which method is the most useful? Why?
I think the play() method is the most useful because it's completely useless if you can't play the song.
