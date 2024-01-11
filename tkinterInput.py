import tkinter as tk

main_window = tk.Tk()

main_window.configure(bg="gray7")
main_window.title('CasualConvoAI')

main_window.columnconfigure(0, weight=1)

my_label = tk.Label(main_window, text="What is your input?")
my_label.grid(column=0, row=1)

my_field = tk.Text(main_window, height=4, width=50, relief=tk.GROOVE, borderwidth=2)
my_field.grid(column=0, row=16, columnspan=2, rowspan=3, sticky=tk.W+tk.E)

def get_input():
    print("Input: ", my_field.get("1.0", "end"))
    my_field.delete("1.0", "end")

input_button = tk.Button(main_window, text="Input", command=get_input)
input_button.grid(column=0, row=0)

tk.mainloop()