# Class Diagrams (UML)

Class diagrams are useful for documenting class members and relationships between classes. As such, they are most useful
when there are a lot of types and especially when there is a lot of subclassing.

For example, let's say we were writing a parser convert XML tags into objects. We have XML like this:

```xml
<Library>
    <Author name="Scalzi, John">
        <Book name="Redshirts" />
        <Book name="Starter Villain" />
        <Book name="Kaiju Preservation Society" />
    </Author>
</Library>
```

We define abstract **Tag** classes to 
represent an XML tag object and **RootTag** as a subclass to represent tags that should be used as a root. Each **Tag**
will have a `load()` method to load an instance from an XML string, and `dump()` to dump the object (and its 
descendents) to an XML string. Each instance also has a `validate()` method, which can validate the object after 
parsing, and a private `_children` attribute containing the children of that tag.

From this, we build a **Library** class to represent a library, which should be built from a **RootTag**. We also build
classes off of **Tag** for **Author** and **Book**.

???+ example "An XML Parser"

    ```mermaid
    classDiagram
        direction LR
        class Tag {
            +str text
            -list~Tag~ _children

            +load(xml_string) Tag$
            +dump() str
            +validate() bool
        }

        class RootTag {
            +from_file(xml_path) RootTag$
        }

        class Author {
            +str name
        }

        class Book {
            +str name
            +int publish_year
        }

        object <|-- Tag
        Tag <|-- RootTag
        Tag <|-- Author
        Tag <|-- Book
        RootTag <|-- Library

        Library "1" ..> "*" Author: children
        Author "1" ..> "*" Book: children
    ```