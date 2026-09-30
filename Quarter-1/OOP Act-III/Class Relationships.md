# Class Relationships: Association and Multiplicity

## Previous Work

[Part I - Classes and Objects](https://github.com/villanueva-svg/9magnesiumcs3/tree/main/Quarter-1/OOP%20Act-I)

[Part II - Class Attributes and Methods](https://github.com/villanueva-svg/9magnesiumcs3/tree/main/Quarter-1/OOPAct-II)

## Existing Class

**Class:** Song

**Description:**
Represents a song with information such as its title, artist, duration, volume, and playing state.

## New Related Class

**Class:** Playlist

**Description:**
Represents a collection of songs that can store and manage multiple Song objects.

## Association

**Relationship:** Playlist contains Song objects.

**Explanation:**
A Playlist object contains and manages multiple Song objects. The playlist stores references to the actual Song objects so that it can access their information.

## Multiplicity

**Multiplicity:** 1 : 0..*

**Explanation:**
One Playlist can contain zero or more Song objects. This multiplicity fits because a playlist can start with no songs and have more songs added to it later.

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

The association is that a Playlist contains Song objects. The Playlist manages a collection of songs that have already been created as separate objects. This allows the playlist to organize multiple songs while the Song class still handles each song's own information and behavior.

### What multiplicity did you choose and why?

I chose a 1 : 0..* multiplicity because one Playlist can contain zero or more Song objects. This fits a playlist because it can exist before any songs are added and can later contain many songs.

### How did you implement the relationship in Python?

I implemented the relationship using the private `__songs` list inside the Playlist class. The `add_song()` method receives a Song object and stores that object in the list. This allows the Playlist to keep references to the actual Song objects.

### Why did you store an object reference instead of copying its data?

I stored the Song object itself so the Playlist can access the Song's existing attributes and methods. For example, `add_song(song1)` stores the actual `song1` object instead of only storing `"Carol of the Bells"`. This keeps the relationship between the Playlist and Song objects instead of duplicating song information.

### If your relationship uses many, why is a list appropriate?

A list is appropriate because one Playlist can contain multiple Song objects. The `__songs` list contains references to the actual Song objects that were added to the Playlist. This makes it possible to loop through the list and access each song's information.
