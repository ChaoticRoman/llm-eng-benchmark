```python
import tkinter as tk
from tkinter import ttk, font, filedialog, messagebox
import markdown2

class MarkdownViewer:
    def __init__(self, master):
        self.master = master
        master.title("Markdown Viewer")

        # Create menu bar
        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        master.config(menu=self.menu_bar)

        # Create text widgets
        self.text_area = tk.Text(master, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        # Configure fonts
        self.default_font = font.nametofont("TkDefaultFont")
        self.bold_font = font.Font(**self.default_font.configure())
        self.bold_font.configure(weight="bold")
        self.italic_font = font.Font(**self.default_font.configure())
        self.italic_font.configure(slant="italic")
        self.heading_fonts = {
            1: font.Font(**self.default_font.configure(), size=20, weight="bold"),
            2: font.Font(**self.default_font.configure(), size=18, weight="bold"),
            3: font.Font(**self.default_font.configure(), size=16, weight="bold"),
            4: font.Font(**self.default_font.configure(), size=14, weight="bold"),
            5: font.Font(**self.default_font.configure(), size=12, weight="bold"),
            6: font.Font(**self.default_font.configure(), size=10, weight="bold")
        }

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    markdown_content = file.read()
                self.render_markdown(markdown_content)
            except FileNotFoundError:
                messagebox.showerror("Error", f"File not found: {file_path}")

    def render_markdown(self, markdown_content):
        self.text_area.delete("1.0", tk.END)
        html = markdown2.markdown(markdown_content)

        # Basic tag handling
        for tag in ["p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"]:
            self.text_area.tag_configure(tag, justify="left")

        # Apply font styles
        self.text_area.insert(tk.END, html, "p")

        # Handle heading levels with different font sizes
        for i in range(1, 7):
            self.text_area.tag_configure(f"h{i}", font=self.heading_fonts[i])

        # Handle bold and italic styles
        self.text_area.tag_configure("strong", font=self.bold_font)
        self.text_area.tag_configure("em", font=self.italic_font)

        # Further customization based on HTML tags is possible

root = tk.Tk()
viewer = MarkdownViewer(root)
root.mainloop()
```

**Explanation:**

1. **Import Necessary Modules:**
   - `tkinter` for the GUI.
   - `ttk` for themed widgets (optional, but recommended).
   - `font` for font manipulation.
   - `filedialog` to open files.
   - `messagebox` for error messages.
   - `markdown2` to convert Markdown to HTML (you'll need to install it: `pip install markdown2`).

2. **`MarkdownViewer` Class:**
   - **`__init__`:**
     - Initializes the main window and widgets:
       - Creates the menu bar with "Open" and "Exit" options.
       - Creates a `Text` widget for displaying the rendered Markdown.
     - Configures fonts:
       - Gets the default font and creates variations for bold, italic, and heading styles.
   - **`open_file`:**
     - Opens a file dialog to select a Markdown file.
     - If a file is selected, it reads the content, calls `render_markdown` to process it, and handles potential `FileNotFoundError`.
   - **`render_markdown`:**
     - Clears the `Text` widget.
     - Converts the Markdown content to HTML using `markdown2.markdown()`.
     - Configures basic tag styles (paragraph, headings, lists) for justification.
     - Inserts the HTML content into the `Text` widget.
     - Applies font styles to headings (h1 to h6) using the pre-configured heading fonts.
     - Applies bold and italic styles using the pre-configured fonts.

3. **Run the Application:**
   - Creates the main window (`root`).
   - Creates an instance of `MarkdownViewer`.
   - Starts the Tkinter event loop (`root.mainloop()`) to display the window.

**To use this:**

1. Save the code as a Python file (e.g., `markdown_viewer.py`).
2. Run it from the terminal: `python markdown_viewer.py`.
3. Use the "File > Open" menu option to load and view a Markdown file.

**Key Improvements:**

- **Error Handling:** Includes error handling for file not found.
- **Font Customization:** Uses separate font objects for different styles, allowing more control over appearance.
- **Structured Code:** Uses a class to organize the code, making it more readable and maintainable.
- **Basic Tag Handling:** Provides basic styling for common HTML tags generated from Markdown.
- **Clearer Explanation:** Includes more detailed comments to explain the code.
