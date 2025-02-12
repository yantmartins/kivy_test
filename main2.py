from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##BoxLayout é uma caixa que irá conter os WIDGETS

class Programa(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        texto = Label(text='Bem- vindo')
        botao = Button(text='Clique')
        

        layout.add_widget(texto)
        layout.add_widget(botao)

        return layout

if __name__ == "__main__":
    Programa().run()  ## INSTANCIA A CLASSE E CHAMA O METODO RUN DE APP
