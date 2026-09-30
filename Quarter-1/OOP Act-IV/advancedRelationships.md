# Advanced Class Relationships

## Previous Activities

[Part II - Class Attributes and Methods](https://github.com/villanueva-svg/9magnesiumcs3/tree/main/Quarter-1/OOPAct-II)

[Part III - Class Relationships](https://github.com/villanueva-svg/9magnesiumcs3/tree/main/Quarter-1/OOPAct-II)

## Existing System Description

The existing system contains a `Song` class that represents individual songs and a `Playlist` class that stores references to multiple Song objects. The system already uses an association between the two classes. However, the previous design did not demonstrate inheritance or a more specific ownership relationship.

## Inheritance Relationship

**Parent:** Song

**Child:** LiveSong

**Explanation:**
A `LiveSong` is a type of `Song` because it has the same basic information and behavior as a regular song while also having additional information about its live performance. The `LiveSong` class inherits the attributes and methods of the `Song` class and adds a `venue` attribute and a `display_live_info()` method.

## Inheritance UML

[Inheritance](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-IV/Images/inheritanceDiagram.png)

## Composition/Aggregation

**Relationship:** Aggregation

**Explanation:**
The `Playlist` class aggregates `Song` objects because the songs can exist independently from the playlist that contains them. The Playlist receives already existing Song objects through the `add_song()` method instead of creating the Song objects itself. Therefore, deleting a Playlist would not require the Song objects to be deleted.

## Advanced UML Diagram

[Advanced UML](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-IV/Images/advancedClassDiagram.png)

## Python Implementation

[Source Code](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-IV/advancedRelationships.py)

## Test Run

[Test](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-IV/Images/advancedTestRun.png)

## Object Diagram

[Objects](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOP%20Act-IV/Images/advancedObjectDiagram.png)

## Reflection

### 1. Why did you choose your inheritance relationship?

I chose `Song` as the parent class and `LiveSong` as the child class because a live song is still a type of song. `LiveSong` uses the same basic song information such as title, artist, and duration. It also adds a `venue` attribute that is specific to live performances.

### 2. How did inheritance reduce duplicate code?

Inheritance allowed `LiveSong` to reuse the constructor and methods already defined in `Song`. The `super().__init__()` call initializes the inherited attributes without requiring the same code to be written again. Methods such as `play()` and `pause()` can also be used by a `LiveSong` object without being rewritten.

### 3. Why is your HAS-A relationship Composition or Aggregation?

The relationship between `Playlist` and `Song` is aggregation because the Song objects can exist independently from the Playlist. The Playlist receives already existing Song objects through its `add_song()` method instead of creating them itself. This means the lifecycle of a Song is not dependent on the lifecycle of the Playlist.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?

In Part III, the relationship between Playlist and Song was represented as a general association, meaning the classes were connected and the Playlist stored references to Song objects. In Part IV, the relationship is specifically modeled as aggregation because the Song objects can exist independently from the Playlist. Aggregation gives the HAS-A relationship a clearer meaning about object ownership and lifecycle.

### 5. How does your design follow the DRY principle?

The design follows the DRY principle by placing common song attributes and behavior in the `Song` parent class instead of repeating them in `LiveSong`. The `LiveSong` class reuses the existing constructor through `super().__init__()` and inherits methods such as `play()` and `pause()`. This reduces duplicated code while allowing the child class to add its own specialized behavior.
