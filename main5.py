from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##BoxLayout é uma caixa que irá conter os WIDGETS

class Programa(App):
    def build(self):
        container = BoxLayout(orientation='vertical')
        
        header = BoxLayout(orientation='horizontal')
        footer = BoxLayout(orientation='vertical')
    
        botao1 = Button(text='One')
        botao2 = Button(text='Two')
        botao3 = Button(text='Three')
        botao4 = Button(text='Four')

        header.add_widget(botao1)
        header.add_widget(botao2)

        footer.add_widget(botao3)
        footer.add_widget(botao4)

        container.add_widget(header)
        container.add_widget(footer)

        return container
    
        

if __name__ == "__main__":
    Programa().run()  ## INSTANCIA A CLASSE E CHAMA O METODO RUN DE APP
