import openai
import tkinter as tk
from tkinter import filedialog

# Set the API key
openai.api_key =  ""

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title
        self.title("SCP-603 Morphic Compiler - Flames LLC")
        self.resizable(False, False)

        # Add a triangle at the center
        self.canvas = tk.Canvas(self, width=200, height=200, bg="white")
        self.canvas.pack()
        self.canvas.create_polygon(100, 10, 10, 190, 190, 190, fill="blue")

        # Create a text input for the user to enter a description of the desired code
        self.description_input = tk.Entry(self, width=30)
        self.description_input.pack()
        self.description_input.insert(0, "Enter code description")

        # Create a dropdown menu to select the programming language
        self.language_var = tk.StringVar(self)
        self.language_var.set("Select Language")  # default value
        self.language_dropdown = tk.OptionMenu(self, self.language_var, "Python", "HTML", "C#", "Rust","GPT4 Chatbot" "Morphic Compiler", "Assembly", "Autotranslate", "Query Google", "OpenAI CODEX (BETA)")
        self.language_dropdown.pack()

        # Create a button to generate the code
        self.generate_button = tk.Button(self, text="Generate", command=self.generate_code)
        self.generate_button.pack()

        # Create a button to save the code
        self.save_button = tk.Button(self, text="Save", command=self.save_code)
        self.save_button.pack()

        # Create a text area to display the generated code
        self.code_display = tk.Text(self)
        self.code_display.pack()

    def generate_code(self):
        # Get the user's input description and selected programming language
        description = self.description_input.get()
        language = self.language_var.get()

        # Use the ChatGPT API to generate the code
        response = openai.Completion.create(
            engine="text-davanci-003",
            prompt=f"Write a {language} program that {description}",
            temperature=0.16,
            max_tokens=2048,
            top_p=0.32,
            frequency_penalty=0.64,
            presence_penalty=0.24
        )
        code = response["choices"][0]["text"]

        # Display the generated code
        self.code_display.delete(1.0, tk.END)
        self.code_display.insert(1.0, code)

    def save_code(self):
        # Open a file dialog to choose where to save the code
        file_path = filedialog.asksaveasfilename()

        # Write the code to the file
        with open(file_path, "w") as f:
            f.write(self.code_display.get(1.0, tk.END))

text_editor = TextEditor()
text_editor.mainloop()
