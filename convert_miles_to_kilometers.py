"""
CP1404 Prac06, "From Scratch" section
A program that converts miles to kilometers
Gareth Mullins, JCU student
Started 09/09/2016
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Gareth Mullins'


class convert_miles_to_kilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_kilometers.kv')
        return self.root

    def handle_change(self, change):
        self.root.ids.input_miles.text = str(self.check_input() + change)
        self.handle_conversion()

    def handle_conversion(self):
        self.root.ids.output_label.text = str(self.check_input() * 1.60934)

    def check_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

app = convert_miles_to_kilometers()
app.run()
