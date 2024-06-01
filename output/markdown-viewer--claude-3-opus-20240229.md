Here's a Python script that creates a full-fledged Markdown document viewer using Tkinter:

```python
import tkinter as tk
from tkinter import filedialog
from markdown2 import Markdown

class MarkdownViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Markdown Viewer")
        self.geometry("800x600")

        # Create a text widget to display the Markdown content
        self.text_widget = tk.Text(self, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create a menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Create a file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
        if file_path:
            with open(file_path, "r") as file:
                markdown_text = file.read()
                self.display_markdown(markdown_text)

    def display_markdown(self, markdown_text):
        # Convert Markdown to HTML
        markdown = Markdown()
        html_text = markdown.convert(markdown_text)

        # Clear the text widget and insert the HTML content
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, html_text)

        # Configure the text widget to display HTML
        self.text_widget.tag_configure("html", wrap=tk.WORD)
        self.text_widget.tag_add("html", "1.0", tk.END)

if __name__ == "__main__":
    viewer = MarkdownViewer()
    viewer.mainloop()
```

This script creates a Markdown document viewer using Tkinter. Here's how it works:

1. We import the necessary modules: `tkinter` for creating the GUI, `filedialog` for opening file dialogs, and `markdown2` for converting Markdown to HTML.

2. We define a `MarkdownViewer` class that inherits from `tk.Tk`. This class represents the main window of the application.

3. In the `__init__` method, we set up the window title, size, and create a text widget (`self.text_widget`) to display the Markdown content. We also create a menu bar (`self.menu_bar`) with a file menu that contains options to open a file and exit the application.

4. The `open_file` method is called when the user selects the "Open" option from the file menu. It opens a file dialog to allow the user to select a Markdown file (with the `.md` extension). If a file is selected, it reads the content of the file and calls the `display_markdown` method to display the Markdown content.

5. The `display_markdown` method takes the Markdown text as input. It uses the `markdown2` module to convert the Markdown text to HTML. It then clears the text widget, inserts the HTML content, and configures the text widget to display the HTML properly.

6. Finally, we create an instance of the `MarkdownViewer` class and start the Tkinter event loop using `mainloop()`.

To use this Markdown viewer, run the script and select a Markdown file using the "Open" option from the file menu. The Markdown content will be displayed in the text widget, rendered as HTML.

Note: Make sure you have the `markdown2` module installed. You can install it using `pip install markdown2`.
