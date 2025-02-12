from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 

class Programa(App):
    def build(self):
        self.tela = Label(text='0', font_size=50)

        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(self.tela)    

        grid = GridLayout(cols=4, spacing=10, padding=10)

        
        botao1 = Button(text='1')
        botao2 = Button(text='2')
        botao3 = Button(text='3')
        botao4 = Button(text='4')
        botao5 = Button(text='5')
        botao6 = Button(text='6')
        botao7 = Button(text='7')
        botao8 = Button(text='8')
        botao9 = Button(text='9')
        botao10 = Button(text='+')
        botao11 = Button(text='-')
        botao12 = Button(text='*')
        botao13 = Button(text='/')
        botao14 = Button(text='=')
        botao15 = Button(text='0')

        
        grid.add_widget(botao1)
        grid.add_widget(botao2)
        grid.add_widget(botao3)
        grid.add_widget(botao4)
        grid.add_widget(botao5)
        grid.add_widget(botao6)
        grid.add_widget(botao7)
        grid.add_widget(botao8)
        grid.add_widget(botao9)
        grid.add_widget(botao10)
        grid.add_widget(botao11)
        grid.add_widget(botao12)
        grid.add_widget(botao13)
        grid.add_widget(botao14)
        grid.add_widget(botao15)
        

        main_layout.add_widget(grid)

        return main_layout
if __name__ == "__main__":
    Programa().run()  ## INSTANCIA A CLASSE E CHAMA O METODO RUN DE APP
