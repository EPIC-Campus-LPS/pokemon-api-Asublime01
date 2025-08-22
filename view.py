import tkinter as tk

class PokemonView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(text="0", font=("Helvetica", 20), master=master)
        self.label.grid(row=0, column=0)

        self.label2 = tk.Label(text="",  font=("Helvetica", 15), master=master)
        self.label2.grid(row=1, column=0)
        
        self.frame = tk.Frame(master=master)
        self.frame.grid(row=3,column=0)

        self.next_button = tk.Button(text="Next", master=self.frame)
        self.next_button.grid(row=0, column=1)

        self.prev_button = tk.Button(text="Previous",master=self.frame)
        self.prev_button.grid(row=0, column=0)


    def set_label(self, text):
        self.label.config(text=str(text))
    
    def set_label_name(self, text):
        self.label2.config(text=str(text))


    def set_next_callback(self, callback):
        self.next_button.config(command=callback)

    def set_prev_callback(self, callback):
        self.prev_button.config(command=callback)
