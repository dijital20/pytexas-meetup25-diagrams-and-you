# Truth Tables

Truth tables are criminally underused, in my opinion. Are you arguging about what should happen given a set of 
conditions? Then a truth table is for you, my friend! They aren't fancy... they're simply a table... rows and columns...
like the Excel of old. Columns are in for different variables, and a column for the expected output.

Truth tables are good at **illustrating behavior for a given set of conditions**.

The name comes from these types of tables you do to explain bitwise operators

???+ example "How does AND work"

    |                      A                      |                      B                      |                   A and B                   |
    | :-----------------------------------------: | :-----------------------------------------: | :-----------------------------------------: |
    | :octicons-check-circle-fill-12:{.true} True | :octicons-check-circle-fill-12:{.true} True | :octicons-check-circle-fill-12:{.true} True |
    | :octicons-check-circle-fill-12:{.true} True |  :octicons-x-circle-fill-12:{.false} False  |  :octicons-x-circle-fill-12:{.false} False  |
    |  :octicons-x-circle-fill-12:{.false} False  | :octicons-check-circle-fill-12:{.true} True |  :octicons-x-circle-fill-12:{.false} False  |
    |  :octicons-x-circle-fill-12:{.false} False  |  :octicons-x-circle-fill-12:{.false} False  |  :octicons-x-circle-fill-12:{.false} False  |

??? example "How does OR work"

    |                      A                      |                      B                      |                   A or B                    |
    | :-----------------------------------------: | :-----------------------------------------: | :-----------------------------------------: |
    | :octicons-check-circle-fill-12:{.true} True | :octicons-check-circle-fill-12:{.true} True | :octicons-check-circle-fill-12:{.true} True |
    | :octicons-check-circle-fill-12:{.true} True |  :octicons-x-circle-fill-12:{.false} False  | :octicons-check-circle-fill-12:{.true} True |
    |  :octicons-x-circle-fill-12:{.false} False  | :octicons-check-circle-fill-12:{.true} True | :octicons-check-circle-fill-12:{.true} True |
    |  :octicons-x-circle-fill-12:{.false} False  |  :octicons-x-circle-fill-12:{.false} False  |  :octicons-x-circle-fill-12:{.false} False  |

When you start getting multiple variables with multiple states, these charts can get really busy. One pro tip is to 
consolidate alike rows and use wildcards such as `*` or `All`.

??? example "What do we have for dinner?"

    |                 Leftovers                  |                 Groceries                  |                   Money                    | Result         |
    | :----------------------------------------: | :----------------------------------------: | :----------------------------------------: | -------------- |
    | :octicons-check-circle-fill-12:{.true} Yes |                     *                      |                     *                      | Eat leftovers. |
    |   :octicons-x-circle-fill-12:{.false} No   | :octicons-check-circle-fill-12:{.true} Yes |                     *                      | Make food.     |
    |   :octicons-x-circle-fill-12:{.false} No   |   :octicons-x-circle-fill-12:{.false} No   | :octicons-check-circle-fill-12:{.true} Yes | Eat out.       |

In the above, we could have listed out all 8 combinations, but there's really no need when every row where "Leftovers" 
is "Yes" will have the same result.
