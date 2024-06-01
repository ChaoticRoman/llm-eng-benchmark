Creating a full-fledged Markdown document viewer in Python using Tkinter involves several steps. We'll use the `markdown` library to convert Markdown content to HTML, and then render this HTML in a Tkinter window using `tkinterweb`, a wrapper around Tkinter's Text widget that can display HTML content.

Here's a step-by-step guide to create a Markdown viewer:

### Step 1: Install Required Libraries

First, you need to install the `markdown` and `tkinterweb` libraries. You can install these using pip:

```bash
pip install markdown
pip install tkinterweb
```

### Step 2: Create the Markdown Viewer

We'll create a Python script that uses Tkinter to build a GUI application. This application will include a text area for inputting Markdown and a display area for the rendered HTML.

Here's the complete code:

```python
import tkinter as tk
from tkinter import filedialog
from tkinterweb import HtmlFrame  # This is used to display HTML content
import markdown  # Markdown library to convert Markdown to HTML

class MarkdownViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Markdown Viewer")
        self.geometry("800x600")

        # Create a menu for opening files
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        # HTML Frame to display markdown content
        self.html_frame = HtmlFrame(self)
        self.html_frame.pack(fill="both", expand=True)

    def open_file(self):
        """ Open a markdown file and update the HTML frame with its content """
        filepath = filedialog.askopenfilename(
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )
        if filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                markdown_content = file.read()
                html_content = markdown.markdown(markdown_content)
                self.html_frame.set_content(html_content)

if __name__ == "__main__":
    app = MarkdownViewer()
    app.mainloop()
```

### Explanation:

1. **Imports**: We import necessary modules including `tkinter`, `tkinterweb.HtmlFrame`, and `markdown`.

2. **MarkdownViewer Class**: This class inherits from `tk.Tk` and sets up the GUI.
   - **Menu**: A simple menu to open Markdown files.
   - **HtmlFrame**: A frame to display HTML content. We use `HtmlFrame` from `tkinterweb` which can render HTML.

3. **open_file Method**: This method opens a dialog to select a Markdown file, reads the file, converts the Markdown to HTML using the `markdown` library, and then updates the `HtmlFrame` with the HTML content.

4. **Main Execution**: If the script is run directly, it creates an instance of `MarkdownViewer` and starts the Tkinter event loop.

### Running the Application

To run the application, simply execute the Python script. You can open Markdown files using the "File" menu, and the content will be rendered in the window.

This viewer handles basic Markdown syntax. For more advanced features or styling, you might need to extend the functionality or use different libraries.
