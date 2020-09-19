from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.lang import Builder
from kivy.base import runTouchApp

Builder.load_string('''
<RootWidget>:
    canvas.before:
        Color:
            rgba: .3, .7, .5, .6
        Rectangle:
            size: self.size
            pos: self.pos
    text: 'THE BACKGROUND'
    font_size: 80
    Image:
        #pos: root.pos
        #size: root.width * 0.7, root.height * 0.4
        source: './logo.png'
        allow_stretch: True
        keep_ratio: False
        #center: self.parent.center
    Image:
        #pos: root.x + 0.5 * root.width, root.y
        #size: root.width * 0.5, root.height
        source: 'money.png'
        allow_stretch: True
        keep_ratio: False

''')

class RootWidget(Label):

    def do_layout(self, *args):
        #self.children is a list of all children
        number_of_children = len(self.children)
        width = self.width
        width_per_child = width / number_of_children

        positions = range(0, int(width), int(width_per_child))
        for position, child in zip(positions, self.children):
            child.height = self.height
            child.x = self.x + position
            child.y = self.y
            child.width = width_per_child

    def on_size(self, *args):
        self.do_layout()

    def on_pos(self, *args):
        self.do_layout()

    def add_widget(self, widget):
        super(RootWidget, self).add_widget(widget)
        self.do_layout()

    def remove_widget(self, widget):
        super(RootWidget, self).remove_widget(widget)
        self.do_layout()

runTouchApp(RootWidget())
