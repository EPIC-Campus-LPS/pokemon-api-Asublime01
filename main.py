import tkinter as tk
from model import PokemonModel
from view import PokemonView
from controller import PokemonController
from Cocoa import NSObject


class AppDelegate(NSObject):
    def applicationSupportsSecureRestorableState_(self, app):
        return True


def main():
    root = tk.Tk()
    root.title("Pokedex")

    model = PokemonModel()
    view = PokemonView(root)
    controller = PokemonController(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()
