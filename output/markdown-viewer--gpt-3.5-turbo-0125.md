To create a full-fledged markdown document viewer in Python using Tkinter, you can use the `markdown` library to parse the markdown content and display it in a Tkinter window. Here's a simple example to get you started:

```python
import tkinter as tk
from tkinter import scrolledtext
import markdown

class MarkdownViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Viewer")
        
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        self.load_button = tk.Button(root, text="Load Markdown File", command=self.load_file)
        self.load_button.pack()
        
    def load_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                html_content = markdown.markdown(content)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, html_content)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownViewer(root)
    root.mainloop()
```

In this code, we create a `MarkdownViewer` class that initializes a Tkinter window with a scrolled text area to display the markdown content. We also add a button to load a markdown file and display its content in the text area after converting it to HTML using the `markdown` library.

You can further enhance this viewer by adding features like saving the HTML content to a file, customizing the appearance of the rendered markdown, and adding support for more markdown features.
