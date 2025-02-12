from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class Programa(App):
    def build(self):
        return Button(text='Clique', font_size='50px')
        ## return Button(text='Clique', font_size='50px')  RETORNA UM BOTAO
        ## return Label(text='Hello World',font_size='50px') RETORNA UMA LABEL

if __name__ == "__main__":
    Programa().run()
