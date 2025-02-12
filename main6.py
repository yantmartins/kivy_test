from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout 

class Programa(App):
    def build(self):
        ##Ajustando a tela com grid layout
        layout = GridLayout(cols=2) ## A  Grid será divididade em duas colunas

        label1 = Label(text='OK1')
        label2 = Label(text='OK2')
        botao1 = Button(text='Clicar')
        botao2 = Button(text='Cancelar')

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(botao1)
        layout.add_widget(botao2)

        return layout

if __name__ == "__main__":
    Programa().run()  ## INSTANCIA A CLASSE E CHAMA O METODO RUN DE APP
