# Flowcharts

Flowcharts are also special [node graphs](01_graphs.md). In Flowcharts, node shapes allow nodes to represent different 
elements of logic such as procedures, loops, data stores, decisions, terminators, and more. Edges help relate these 
elements to each other. Because of this, flowcharts are excellent for ***detailing logic in a procedure***.

???+ example "Let's get paged data from a REST API"

    ```mermaid
    flowchart TD
        
        start([Start])
        initialize_list[/Initialize result list/]
        call_url[[Call first page URL]]
        store_result[/Store call response/]

        subgraph Page loop
            loop[\While loop/]
            add_values[/Add response values to result list/]
            call_page_url[[Call nth page URL]]
            store_page_result[/Store call response/]
            no_values@{shape: notch-pent, label: "No values in call result"}
        end

        finish([Return result list])

        start --> initialize_list --> call_url --> store_result --> loop
        loop --> no_values -- no --> add_values --> call_page_url --> store_page_result --> loop
        no_values -- yes --> finish
    ```

    ??? abstract "Corresponding code"

        ```python
        def get_paged(url: str) -> list[dict]:
            """Get a paged URL."""
            results = []
            response = session.get(url).json()
            while True:
                if not response['values']:
                    break
                results += response['values']
                response = session.get(response['next_page']).json()
            return results
        ```

This example illustrates the process of getting data from from a paged REST API on most services. It uses rounded nodes
as terminators (start and end nodes), parallelogram nodes for storing data, rectangular nodes from actions, and 
double-barred rectangular nodes for more complex procedures that are defined elsewhere. You can follow the nodes from
"Start" to "Return result list" to see the branches of logic.

??? note "Shape cheat sheet"

    ```mermaid
    flowchart LR
        subgraph Basic Shapes
            te@{shape: stadium, label: "Terminator"}
            ac@{shape: rect, label: "Action"}
            sp@{shape: fr-rect, label: "Subprocess"}
            ev@{shape: event, label: "Event"}
            dl@{shape: delay, label: "Delay"}
        end
        
        subgraph Documents and Data
            in@{shape: lean-r, label: "Input"}
            ou@{shape: lean-l, label: "Output"}
            do@{shape: doc, label: "Document"}
            md@{shape: docs, label: "Multiple Documents"}
            db@{shape: cyl, label: "Database"}
        end
        
        subgraph Loops and Conditionals
            de@{shape: diamond, label: "Decision"}
            co@{shape: circle, label: "Connector"}
            ml@{shape: trap-t, label: "Loop"}
            ll@{shape: notch-pent, label: "Loop limit"}
            fr@{shape: fork, label: "Fork"}
        end
    ```
