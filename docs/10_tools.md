# Tools of the Trade

## Mermaid

[Mermaid](https://mermaid.js.org) is an amazing toolkit for creating diagrams from a code-like language. Mermaid was
used in this to create the graphs, state diagrams, flowcharts, workflow diagrams, class diagrams, and sequence diagrams.
There are a lot of tools and plugins out there to add mermaid rendering into various products (mkdocs does this here),
and syntax highlighting and live preview for editors.

??? example "Mermaid language"

    ```plaintext
    flowchart TB
        openNotepad(["Open **Notepad**"])
        addText["Add text to the document"]
        clickFile["Click **File** menu"]
        chooseSave["Choose **Save** menu item"]
        displaySaveDialog("*Save dialog appears*")
        enterFileName["Enter name in file name text box"]
        clickSave["Click **Save** button"]
        pressCtrlEnter["Press **CTRL+Enter**"]
        savedDocument(["Saved Document"])
        pressCtrlS["Press **CTRL+S**"]

        openNotepad --> addText
        addText --> pressCtrlS --> displaySaveDialog
        addText --> clickFile --> chooseSave --> displaySaveDialog
        displaySaveDialog --> enterFileName --> clickSave --> savedDocument
        enterFileName --> pressCtrlEnter --> savedDocument
    ```

## Graphviz (and pydot)

[Graphviz](https://graphviz.org) is old hat by now, but is a mature toolkit for creating diagrams of all types. While 
its DOT language is a bit more cumbersome to learn and use, it's age and maturity mean that there is a wealth of tools 
out there to work with. Also, since Graphviz is based in C (as opposed to Mermaid, which is JavaScript), it has higher 
limits for things like diagram complexity.

??? example "DOT language"

    ```dot
    digraph workflow {
        splines=curved;
        label="User saves new Notepad document";
        
        openNotepad [label=<Open <b>Notepad</b>>, shape=box, style=rounded];
        addText [label="Add text to the document", shape=note];
        clickFile [label=<Click <b>File</b> menu>, shape=note];
        chooseSave [label=<Choose <b>Save</b> menu item>, shape=note];
        displaySaveDialog [label=<<i>Save dialog appears</i>>, shape=box];
        enterFileName [label="Enter name in the file name text box", shape=note];
        clickSave [label=<Click <b>Save</b> button>, shape=note];
        pressCtrlEnter [label=<Press <b>CTRL + Enter</b>>, shape=note];
        savedDocument [label="Saved Document", shape=box, style=rounded];
        pressCtrlS [label=<Press <b>CTRL + S</b>>, shape=note];
        
        openNotepad -> addText;
        addText -> pressCtrlS;
        pressCtrlS -> displaySaveDialog;
        addText -> clickFile;
        clickFile -> chooseSave;
        chooseSave -> displaySaveDialog;
        displaySaveDialog -> enterFileName;
        enterFileName -> clickSave;
        clickSave -> savedDocument;
        enterFileName -> pressCtrlEnter;
        pressCtrlEnter -> savedDocument;
    }
    ```

The `pydot` bindings add in a Python-based object-oriented mechanism to create Graphviz diagrams. The `pydot` Python
code you produce can simplify to Graphviz's DOT language, which can be consumed by Graphviz commands to produce diagrams.

??? example "pydot"

    ```python
    """Just the workflow example in PyDot."""

    from pathlib import Path
    from pydot import Dot, Node, Edge

    NODES = [
        (
            "openNotepad",
            {
                "label": "<Open <b>Notepad</b>>",
                "shape": "box",
                "style": "rounded",
            },
        ),
        (
            "addText",
            {
                "label": "Add text to the document",
                "shape": "note",
            },
        ),
        (
            "clickFile",
            {
                "label": "<Click <b>File</b> menu>",
                "shape": "note",
            },
        ),
        (
            "chooseSave",
            {
                "label": "<Choose <b>Save</b> menu item>",
                "shape": "note",
            },
        ),
        (
            "displaySaveDialog",
            {
                "label": "<<i>Save dialog appears</i>>",
                "shape": "box",
            },
        ),
        (
            "enterFileName",
            {
                "label": "Enter name in the file name text box",
                "shape": "note",
            },
        ),
        (
            "clickSave",
            {
                "label": "<Click <b>Save</b> button>",
                "shape": "note",
            },
        ),
        (
            "pressCtrlEnter",
            {
                "label": "<Press <b>CTRL + Enter</b>>",
                "shape": "note",
            },
        ),
        (
            "savedDocument",
            {
                "label": "Saved Document",
                "shape": "box",
                "style": "rounded",
            },
        ),
        (
            "pressCtrlS",
            {
                "label": "<Press <b>CTRL + S</b>>",
                "shape": "note",
            },
        ),
    ]
    EDGES = [
        ("openNotepad", "addText"),
        ("addText", "pressCtrlS"),
        ("pressCtrlS", "displaySaveDialog"),
        ("addText", "clickFile"),
        ("clickFile", "chooseSave"),
        ("chooseSave", "displaySaveDialog"),
        ("displaySaveDialog", "enterFileName"),
        ("enterFileName", "clickSave"),
        ("clickSave", "savedDocument"),
        ("enterFileName", "pressCtrlEnter"),
        ("pressCtrlEnter", "savedDocument"),
    ]


    if __name__ == "__main__":
        graph = Dot(
            "workflow",
            splines="curved",
            label="User saves new Notepad document",
        )

        for name, kwargs in NODES:
            graph.add_node(Node(name, **kwargs))

        for src, dst in EDGES:
            graph.add_edge(Edge(src, dst))

        print(graph.to_string())

        p = Path("workflow.png").resolve()
        graph.write(path=str(p), prog="dot", format="png")
        print("Wrote", p)
    ```

## PyTM

The OWASP group maintains [`PyTM`](https://github.com/OWASP/pytm), a Python library for representing Data Flow diagrams.
The `pytm` Python code you produce can simplify to Graphviz's DOT language, which can also be consumed by Graphviz to
produce diagrams.

??? example "pytm"

    ```python
    """Example data flow diagram."""

    from pytm.pytm import Boundary, Actor, Server, TM, Dataflow

    if __name__ == "__main__":
        tm = TM("example")
        tm.description = "Example Threat Model"
        tm.isOrdered = True

        user_boundary = Boundary("user")
        app_boundary = Boundary("app")
        service_boundary = Boundary("service")

        user = Actor("user")
        user.inBoundary = user_boundary

        app = Server("app")
        app.inBoundary = app_boundary

        service = Server("mobile service")
        service.inBoundary = service_boundary

        identity = Server("identity service")
        identity.inBoundary = service_boundary

        Dataflow(
            user,
            app,
            "User provides username and password.",
        )
        Dataflow(
            app,
            service,
            "App calls login API with username and password.",
        )
        Dataflow(
            service,
            identity,
            "Service calls authentication check in identity service.",
        )
        Dataflow(
            identity,
            service,
            "Identity service authenticates user.",
        )
        Dataflow(
            service,
            app,
            "Service authenticates the user and returns a token.",
        )
        Dataflow(
            app,
            user,
            "User is logged in.",
        )

        tm.process()

    ```

## Microsoft Threat Modeling Tool

Microsoft has a free [Threat Modeling tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool), 
which can be used to draw Data Flow diagrams. The tool also provides some analysis of the diagram, although in my 
experience, that is a noisy experience and not as useful.

## PyReverse

If you have written Python code and you have `pylint`, did you know you also have `pyreverse`, a tool that can generate a 
class diagram from the code? You do! Try it out!

## Miro / Draw.io / Gliffy / etc.

There are a number of web-based diagram platforms that can do a wealth of different types of diagrams. 

## Pen and Paper (or whiteboard, or whatever)

At the end of the day, communication is the key. Tools are cool but pen and paper often does the job just as well.
