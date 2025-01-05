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
