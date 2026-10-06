# Class Relationships: Association and Multiplicity

## Existing Class

**Class:** Song

**Description:**
Defines and represents the information a song object has; Like, volume, duration, playing_state (whether or not it's playing), and artist

## New Related Class

**Class:** Playlist

**Description:**
Represents a collection of songs, defining the functions like storage and management of zero, one, or multiple song objects.

## Association

**Relationship:** Playlist contains Song objects.

**Explanation:**
A Playlist object contains and manages a collection of Song objects, storing references to the stored Song objects to access their information (ie., volume, artist, playing_state, etc.).

## Multiplicity

**Multiplicity:** 1 : 0..*

**Explanation:**
One Playlist can contain zero or more Song objects. Which is useful because playlists can start with no songs and have more added later, allowing for pre-creation for songs that may be found in the future.

## UML Class Relationship Diagram

[Class Relationship Diagram](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-III/Images/classRelationshipDiagram.png)

## Python Implementation

[View Python Source](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-III/ClassRelationships.py)

## Test Run

[Relationship Test Run](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-III/Images/relationshipTestRun.png)

## Object Relationship Diagram

[Object Relationship Diagram](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-III/Images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?

The association is that a Playlist contains Song objects. The Playlist object manages multiple pre-created individual Song objects, allowing the playlist to organize multiple songs while the Song class continues to define each song's own attributes and methods.

### What multiplicity did you choose and why?

I chose a 1 : 0..* multiplicity because one Playlist can contain zero or more Song objects, which happens because a Playlist can exist before any Songs are input.

### How did you implement the relationship in Python?

I implemented the relationship by having the Playlist class contain the privated `_songs` list. The `add_song()` method allows the playlist to receive a song object and store the object in the collection, allowing  the playlist to keep references to the actual Song objects.

### Why did you store an object reference instead of copying its data?

I kept the Song object itself so the Playlisr can access the Song's existing attributes and methods. For example, `add_song(s1)` stores the actual `s1` instead of only storing the title `"Carol of the Bells"`.
Which maintains the relationship between the Playlist and Song objects without duplicating information.

### If your relationship uses many, why is a list appropriate?

A list is appropriate because one Playlist can contain multiple Song objects. The `_songs` list contains references to the actual Song objects that were added to the Playlist, making it possible to loop through the list and access each Song object's information.
