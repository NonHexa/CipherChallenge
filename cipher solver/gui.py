import tkinter as tk

class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="your message", font=("Arial",18) )
        self.label.pack(padx=10,pady=10)
        self.textbox = tk.Text(self.root, font=("arial",16))
        self.textbox.pack(padx=10,pady=10)
        self.check_state=tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="show box", font=("Arial",16), variable=self.check_state)
        self.check.pack(padx=10,pady=10)
        self.button = tk.Button(self.root, text="show message", font=("Arial", 18),command=self.show_message)
        self.button.pack()
        self.root.mainloop()
    def show_message(self):
        print(self.check_state.get())

GUI()
