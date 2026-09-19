# Class Attributes and Methods

## Previous Design

Link: [classObjectUML.md](classObjectUML.md)

## Design Revision

Changes from my previous design:

* I made the `volume` attribute private so it can be safely changed through a method.
* I added the `is_playing` attribute to keep track of whether a song is playing or paused.

## Visibility Decisions

| Attribute  | Data Type | Visibility  | Why Public/Private?                                                               |
| ---------- | --------- | ----------- | --------------------------------------------------------------------------------- |
| title      | string    | Public (+)  | The title can be accessed directly to identify the song.                          |
| artist     | string    | Public (+)  | The artist can be accessed directly to identify who made the song.                |
| duration   | string    | Public (+)  | The duration can be accessed directly to show how long the song is.               |
| volume     | int       | Private (-) | The volume should be changed through a method instead of being changed directly.  |
| is_playing | bool      | Public (+)  | The playing state can be accessed to check whether the song is playing or paused. |

## Updated UML Class Diagram

[Class Diagram](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOPAct-II/Images/Class-DiagramSG5.png)

## Python Implementation

[View Python Source](classImplementation.py)

## Test Run

[Test Run](https://github.com/villanueva-svg/9magnesiumcs3/tree/main/Quarter-1/OOPAct-II/Images/classTestRun)

## Object Diagram

[Object Diagram](https://github.com/villanueva-svg/9magnesiumcs3/blob/main/Quarter-1/OOPAct-II/Images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?

I made the volume attribute private because it should be changed through the `change_volume()` method instead of being changed directly. This allows the class to control how the volume is modified. If it were changed directly, the volume could be given an invalid value or changed without using the intended method.

### Which method changes the state of your object?

The `change_volume()` method changes the state of the object by changing its private `volume` attribute. In the test, I called `song1.change_volume(75)`, which changed Song 1's volume from default to 75.

### How did your two objects demonstrate that instances are independent?

The two objects were created from the same `Song` class but had different song information. When I changed Song 1's volume to 75, Song 2's volume remained at default. This shows that each object has its own separate state.

### What is the difference between your class diagram and your object diagram?

The class diagram shows the design of the `Song` class, including its attributes, methods, and visibility. The object diagram shows the actual `song1` and `song2` objects and their current values after the test. The class diagram is the blueprint, while the object diagram shows instances created from that blueprint.
