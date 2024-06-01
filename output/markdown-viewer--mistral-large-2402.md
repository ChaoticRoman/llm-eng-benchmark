Creating a full-fledged Markdown document viewer in Python using Tkinter involves several steps. Here's a simple example to get you started. This example will not cover all Markdown syntax, but it will give you a basic idea of how to proceed.

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox
import markdown

class MarkdownViewer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Markdown Viewer")

        self.markdown_text = scrolledtext.ScrolledText(self, wrap = 'word', width = 80, height = 20)
        self.markdown_text.pack(pady = 20)

        self.html_text = tk.Text(self, wrap = 'word', width = 80, height = 20, padx = 10, pady = 10, relief = 'sunken', bd = 5)
        self.html_text.pack(pady = 20)

        self.convert_button = tk.Button(self, text = "Convert Markdown to HTML", command = self.convert_markdown_to_html)
        self.convert_button.pack(pady = 10)

    def convert_markdown_to_html(self):
        try:
            md = markdown.Markdown()
            html = md.convert(self.markdown_text.get("1.0",'end-1c'))
            self.html_text.insert('1.0', html)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = MarkdownViewer()
    app.mainloop()
```

This script creates a simple Tkinter application with two text boxes and a button. The top text box is for entering Markdown text, and the bottom text box displays the converted HTML. The button triggers the conversion.

Please note that this is a very basic example. It doesn't handle errors gracefully, and it doesn't display HTML as formatted text - it just displays the raw HTML. To display the HTML with formatting, you would need a web view component, which Tkinter does not provide. You might want to look into other GUI libraries like PyQt or PySide, which can embed a WebKit view.

Also, this example uses the Python-Markdown library to convert Markdown to HTML. You can install it with pip:

```bash
pip install markdown
```
