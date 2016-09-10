"""
CP1404 Prac06, "Dynamic Kivy Widgets"section
Dynamically create labels based on contents of a dictionary
Gareth Mullins, JCU student
Modified from Lindsay Wards dynamic_widgets, 09/09/2016
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

__author__ = 'Gareth Mullins'


class loop_string_list(App):
    # Main program
    status_text = StringProperty()

    def __init__(self, **kwargs):
        # Construct main app
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.strings = {"0": "a", "1": "b", "2": "c"}

    def build(self):
        # Build Kivy GUI
        self.title = "Loop String List"
        self.root = Builder.load_file('loop_string_list.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        # Create buttons from dictionary entries and add them to the GUI
        for name in self.strings:
            # create a label for each strings entry
            self.root.ids.entriesBox.add_widget(Label(text=name))

    def clear_all(self):
        # Clear all of the widgets that are children of the "entriesBox" layout widget
        self.root.ids.entriesBox.clear_widgets()


loop_string_list().run()
