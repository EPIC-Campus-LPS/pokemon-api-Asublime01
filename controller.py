class PokemonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_next_callback(self.handle_increment)
        self.view.set_prev_callback(self.handle_decrement)

    def handle_increment(self):
        """
        Called on increment button pressed

        1. Clears the directory of all .png files
        2. Increase the number
        3. Set the value label to the current number
        4. Set the name label to the name retrieved from model.get_name()
        5. Set the image label to the image path retrieved from model.get_image_path()
        """
        self.model.takeout_the_trash()
        self.model.increment()
        self.view.set_label(self.model.get_value())
        self.view.set_label_name(self.model.get_name())
        self.view.set_image(self.model.get_image_path())

    def handle_decrement(self):
        """
        Called on Decrement button pressed

        1. Clears the directory of all .png files
        2. Decrease the number
        3. Set the value label to the current number
        4. Set the name label to the name retrieved from model.get_name()
        5. Set the image label to the image path retrieved from model.get_image_path()
        """
        self.model.takeout_the_trash()
        self.model.decrement()
        self.view.set_label(self.model.get_value())
        self.view.set_label_name(self.model.get_name())
        self.view.set_image(self.model.get_image_path())

