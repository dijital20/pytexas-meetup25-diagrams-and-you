# Sequence Diagram

Congratulations! You've made it to the first diagram that isn't a node graph variation! How's it feel?

A sequence diagram is a special type of diagram that **illustrates a sequence of actions between 2 or more entities in a
system**. It does this by assigning each entity a column, and then draw lines between columns to illustrate actions 
between those entities.

???+ example "How to order a Burger"

    ```mermaid
    sequenceDiagram
        participant Me
        box Burger Shack
            participant Cashier
            participant Cook
        end

        Me ->>+ Cashier: I would like a burger please.
        Cashier ->> Me: Yes. Would you like to make that a combo?
        Me ->> Cashier: Yes, please.
        Cashier ->> Me: Would you like to super-size that combo?
        Me ->> Cashier: No, thank you.
        Cashier ->>+ Cook: I need a burger and fries.
        Cashier ->> Me: That'll be $8.95.
        Me ->> Cashier: *Hands $10*
        Cashier ->>- Me: Here's your $1.05 change.
        Cook ->>- Cashier: *Hands burger*
        Cashier ->> Me: *Hands burger*
    ```

For flows that are primarily linear and involving 8 entities or less, sequence diagrams are more useful than
flowcharts. Sequence diagrams can also contain loop, exception, and decision bits.
