# Workflow Diagrams

Workflow diagrams are a specialization of a flowchart, but with looser rules on states, and usually used to show 
higher-level, user-directed processes. In this case, a workflow is a series of actions that a user takes to accomplish 
some task. Workflow diagrams are useful for understanding **user interaction workflows**.

???+ example "User wants to create a word document"

    ```mermaid
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

In this case, the difference between this and a flowchart or a state diagram are more abstract. The goal is not so much
to define the minutae of a program flow, but instead to chart the behavior of a program based on the user.
