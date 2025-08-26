import tkinter as tk
from PIL import ImageTk, Image


class PokemonView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(text="0", font=("Helvetica", 20), master=master) #Number Label
        self.label.grid(row=0, column=0)

        self.label2 = tk.Label(text="",  font=("Helvetica", 15), master=master) #Name Label
        self.label2.grid(row=3, column=0)
        
        self.image_label = tk.Label(master=master)
        self.image_label.grid(row=2, column=0)

        self.frame = tk.Frame(master=master)
        self.frame.grid(row=4,column=0)

        self.next_button = tk.Button(text="Next", master=self.frame)
        self.next_button.grid(row=0, column=1)

        self.prev_button = tk.Button(text="Previous",master=self.frame)
        self.prev_button.grid(row=0, column=0)


    def set_label(self, text):
        """
        Sets the number value of the Tkinter label by calling self.label.config()
        """
        self.label.config(text=str(text))
    
    def set_label_name(self, text):
        """
        Sets the name value of the Tkinter label by calling self.label.config()
        """
        self.label2.config(text=str(text))


    def set_next_callback(self, callback):
        self.next_button.config(command=callback)

    def set_prev_callback(self, callback):
        self.prev_button.config(command=callback)
    
    def set_image(self, image_path):
        """
        1. Calls for and identifies the image path
        2. Converts the image path into a Tk image object that tk.Label can use
        3. Sets the image variable in self.image_label
        """
        # Load and resize the image (optional)
        pil_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(pil_image)

        self.image_label.config(image=tk_image)
        self.current_image = tk_image
