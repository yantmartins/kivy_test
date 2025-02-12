from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##BoxLayout é uma caixa que irá conter os WIDGETS

class Programa(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.texto = Label(text='Bem- vindo')
        self.botao = Button(text='+')

        ## Adicionando uma função ao clicar no botão
        self.botao.bind(on_press = self.hello)

        layout.add_widget(self.texto)
        layout.add_widget(self.botao)

        return layout
    
    def hello(self,event):
        print("HELLO!")
        self.texto.text = '+' ##Adicionando o novo texto no botão

if __name__ == "__main__":
    Programa().run()  ## INSTANCIA A CLASSE E CHAMA O METODO RUN DE APP
