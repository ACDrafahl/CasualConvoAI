import tkinter as tk

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("CasualConvoAI Beta")

        # Set background color to black
        self.root.configure(bg='black')

        # Set up the Text widget
        self.text_box = tk.Text(root, height=10, width=40, bg='black', fg='green', insertbackground='green', relief=tk.FLAT, state=tk.DISABLED)
        self.text_box.pack(pady=10)

        # Create a frame with a green background
        self.text_frame = tk.Frame(root, bg='green', bd=2)  # bd is the border width
        self.text_frame.pack(side=tk.BOTTOM, pady=1, fill=tk.X)

        self.display_text("Booting up...")  # Initial message

        self.input_entry = tk.Entry(self.text_frame, bg='black', fg='green', insertbackground='green', relief=tk.FLAT)
        self.input_entry.pack(fill=tk.X, expand=True)

        # Bind the Enter key to the take_input method
        self.input_entry.bind("<Return>", self.take_input)

        # Set focus to the input entry
        self.input_entry.focus_set()

    def display_text(self, message):
        self.text_box.configure(state=tk.NORMAL)  # Set state to normal to enable editing temporarily
        self.text_box.insert(tk.END, message + "\n")
        self.text_box.configure(state=tk.DISABLED)  # Set state back to disabled

    def take_input(self, event):
        user_input = self.input_entry.get()
        self.display_text("User Input: " + user_input)
        # You can add more logic based on user input if needed
        self.input_entry.delete(0, tk.END)  # Clear the input entry

if __name__ == "__main__":
    root = tk.Tk()

    # Set the background color of the root window to black
    root.configure(bg='black')

    my_program = UI(root)
    root.mainloop()
