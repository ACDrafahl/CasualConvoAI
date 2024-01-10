import tkinter as tk

def main():
    root = tk.Tk()
    label = tk.Label(root, text="Hello, world!")
    label.pack()
    loop_active = True

    while loop_active:
        root.update()
        user_input = input("Type something!\n")
        if user_input == "exit":
            root.quit()
            loop_active = False
        else: 
            new_label = tk.Label(root, text=user_input)
            new_label.pack()

if __name__ == "__main__":
    main()



