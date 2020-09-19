from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        f = FloatLayout()
        s = Scatter()

        t = TextInput(font_size=150, size_hint_y=None, height=200, text='default')
        l = Label(text="default", font_size=150)

        t.bind(text=l.setter('text'))

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)
        button1 = Button(text="Send",
                      background_color=(0.572, 0.45, 0.65,1),
                      font_size=80,
                      size_hint_y=None,
                      height=100)
        b.add_widget(button1)

        return b

if __name__=="__main__":
    TutorialApp().run()
