# Graphs

Graphs consist of **Nodes** and **Edges**. Nodes represent things... ideas, people, steps... and the edges relate the
nodes to each other. 

???+ example "The most basic example"

    ```mermaid
    graph LR
        node1
        node2
        
        node1---node2
    ```

As you can guess, graphs are very good for ***showing relationships***.

???+ example "Relationships, Star Wars style"

    ```mermaid
    graph TD

        lukeSkywalker[Luke Skywalker]
        darthVader[Darth Vader]
        princessLeia[Princess Leia]
        hanSolo[Han Solo]
        chewbacca[Chewbacca]
        obiWanKenobi[Obi-wan Kenobi]

        obiWanKenobi-->|trains|lukeSkywalker
        darthVader<-->|father/son|lukeSkywalker
        darthVader<-->|father/daughter|princessLeia
        obiWanKenobi-->|trains|darthVader
        hanSolo<-->|friends|lukeSkywalker
        hanSolo<-->|friends|princessLeia
        hanSolo<-->|friends|chewbacca
    ```

Edges can be directed or non-directed. Graphs can be open (any given node leads to other nodes without leading back to 
itself) or closed (nodes can lead back to themselves).

One of the most common kinds of graphs that we learn early on, is the mind map (otherwise called webbing). These node
graphs are developed when trying to brainstorm an idea.

???+ example "Mindmapping this presentation, how meta..."

    ```mermaid
    mindmap
        Diagrams
            Node graphs
                State diagrams
                Flowcharts
                Workflow diagrams
                Data Flow diagrams
            Class diagrams
            Sequence diagrams
            Tables
                Truth tables
            Storyboards
    ```

Maps are, at the end of the day, node graphs... with locations as the nodes and roads as the edges connecting them.

Either way, if you need to show the relationships between things, a node graph is a darn good way to do it.