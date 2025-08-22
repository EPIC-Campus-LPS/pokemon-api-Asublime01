class PokemonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_next_callback(self.handle_increment)
        self.view.set_prev_callback(self.handle_decrement)

    def handle_increment(self):
        self.model.increment()
        self.view.set_label(self.model.get_value())
        self.view.set_label_name(self.model.get_name())

    def handle_decrement(self):
        self.model.decrement()
        self.view.set_label(self.model.get_value())
