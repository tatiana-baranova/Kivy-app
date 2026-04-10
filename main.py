from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class DuckyApp(App):
    def build(self):
        box = BoxLayout()
        b1 = Button(text="Hello all")
        b2 = Button(text="Hello")
        box.add_widget(b1)
        box.add_widget(b2)
        return box

if __name__ == '__main__':
    DuckyApp().run()