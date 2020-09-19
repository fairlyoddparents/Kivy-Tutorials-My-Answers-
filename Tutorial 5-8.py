from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color

import random

class ScatterTextWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)

        """
        #write the word before if you want it to be under the labels
        with self.canvas.before:
            Color(0, 1, 0, 1)
            Rectangle(pos=(0,100), size=(300, 100))
            Ellipse(pos=(0,400), size=(300,100))
            Line(points=[0,0,500,600,400,300], close=True, width=3)
        """

    #We have 3 ways of doing this, this one
    def change_label_color(self, *args):
        color = [random.random() for i in range(3)]+ [1]
        label = self.ids['my_label']
        """You can also write it like this
                label = self.ids.my_label
        """

        label.color = color

    """
    Or we can write in the kv file this instead
        on_text: my_label.color = [random.random() for i in range(3)] + [1]

    to use the function random in the kv file you need to import
    the random module to import a module you use
    the following syntax at the top:

        #:import random random
    """

    """
    Or you can import ListProperty in the python file
        from kivy.properties import ListProperty

    then create a kivy property inside the ScatterTextWidget class
        text_color = ListProperty([1,0,0,1])

    then change it inside change_label_color function
        self.text_color = color

    now that it is a kivy porperty I can use the ON_ to tell the machine
    what to do whenever such property changes (under orientation):
        on_text_color: do_things()

    or you can write a function on the python file:
        def on_text_color(self, *args):
            do_whatever()
    """

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == '__main__':
    TutorialApp().run()
