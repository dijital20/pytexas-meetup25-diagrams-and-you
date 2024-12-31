# State Diagrams

State diagrams are a special kind of node graph that shows various exclusive states of a system, and how those states
related to each other. In a State diagram, nodes represent the states, and edges represent the triggers that signal 
state change. State diagrams are good for showing ***the relationships between states and the triggers that transition 
between them***.

Here's an example of the states of water.

???+ example "States of water"

    ```mermaid
    stateDiagram-v2
        steam: Steam (gas)
        water: Water (liquid)
        ice: Ice (solid)

        direction LR

        ice --> water: Heat above 0 degrees celsius (melting)
        water --> steam: Heat above 100 degrees celsius (evaporating)
        steam --> water: Cool below 100 degrees celsius (condensing)
        water --> ice: Cool below 0 degrees celsius (freezing)
    ```

Diagrams can get more complex. Here's a coffee pot:

???+ example "Making coffee"

    ```mermaid
    stateDiagram-v2
        off: Off

        state On {
            waiting: Waiting
            brewing: Brewing
            keepWarm: Keep warm

            direction LR

            waiting --> brewing: Add coffee, water, and press Brew.
            brewing --> keepWarm: Finish brew
            keepWarm --> waiting: Time expired
        }

        direction LR

        [*] --> off
        off --> On: Turn on
        On --> off: Turn off
    ```
