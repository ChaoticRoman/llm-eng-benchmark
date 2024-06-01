Creating a full-fledged Markdown document viewer in Python using Tkinter involves several steps. Below is a comprehensive example that demonstrates how to achieve this. This example uses the `markdown` library to convert Markdown text to HTML and the `tkhtmlview` library to render the HTML in a Tkinter application.

First, ensure you have the necessary libraries installed:
```sh
pip install markdown tkhtmlview
```

Here's the complete code for a Markdown document viewer using Tkinter:

```python
import tkinter as tk
from tkinter import filedialog, messagebox
from tkhtmlview import HTMLLabel
import markdown

class MarkdownViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Markdown Viewer")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Create a menu
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

        # Create a frame for the HTML content
        self.html_frame = tk.Frame(self, bg="white")
        self.html_frame.pack(fill=tk.BOTH, expand=True)

        # Create an HTMLLabel to display the converted Markdown
        self.html_label = HTMLLabel(self.html_frame, html="<h1>Welcome to Markdown Viewer</h1>")
        self.html_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Open Markdown File",
            filetypes=(("Markdown files", "*.md"), ("All files", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    markdown_text = file.read()
                    html_content = markdown.markdown(markdown_text)
                    self.html_label.set_html(html_content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

if __name__ == "__main__":
    app = MarkdownViewer()
    app.mainloop()
```

### Explanation:

1. **Imports**:
   - `tkinter` for the GUI.
   - `filedialog` and `messagebox` for file operations and error handling.
   - `HTMLLabel` from `tkhtmlview` to render HTML content.
   - `markdown` to convert Markdown text to HTML.

2. **MarkdownViewer Class**:
   - Inherits from `tk.Tk` to create the main application window.
   - `__init__` method initializes the window and calls `create_widgets` to set up the UI components.

3. **create_widgets Method**:
   - Creates a menu bar with options to open a file and exit the application.
   - Sets up a frame to hold the HTML content.
   - Initializes an `HTMLLabel` with a welcome message.

4. **open_file Method**:
   - Opens a file dialog to select a Markdown file.
   - Reads the file content and converts it to HTML using the `markdown` library.
   - Updates the `HTMLLabel` with the converted HTML content.

5. **Main Execution**:
   - Creates an instance of `MarkdownViewer` and starts the Tkinter main loop.

This example provides a basic Markdown viewer with file opening capabilities. You can extend it further by adding more features like syntax highlighting, better error handling, and additional formatting options.
