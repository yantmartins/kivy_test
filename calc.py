##Configurações Iniciais -> IMPORT DAS CLASSES

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.core.window import Window
Window.size = (300,700)

class MyCalc(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')

        box_botoes = GridLayout(cols=4, spacing=10, padding=10)

        self.display = Label(text='Bem vindo', font_size='50px')

        self.button_zerar = Button(text='C')
        #Adicionando um evento ao botão ZERAR, que irá chamar o método Hello
        self.button_zerar.bind(on_press = self.zerar)

        self.buttonC = Button(text='C')
        self.buttonPow = Button(text='^')
        self.buttonSquare = Button(text='√')
        self.buttonPerc = Button(text='%')
        self.button1 = Button(text='7')
        self.button2 = Button(text='8')
        self.button3 = Button(text='9')
        self.button4 = Button(text='*')
        self.button5 = Button(text='4')
        self.button6 = Button(text='5')
        self.button7 = Button(text='6')
        self.button8 = Button(text='/')
        self.button9 = Button(text='1')
        self.button10 = Button(text='2')
        self.button11 = Button(text='3')
        self.button12 = Button(text='-')
        self.button0 = Button(text='.')
        self.button13 = Button(text='0')
        self.button_igual = Button(text='=')
        self.button_soma = Button(text='+')

        box_botoes.add_widget(self.buttonC)
        box_botoes.add_widget(self.buttonPow)
        box_botoes.add_widget(self.buttonSquare)
        box_botoes.add_widget(self.buttonPerc)
        box_botoes.add_widget(self.button1)
        box_botoes.add_widget(self.button2)
        box_botoes.add_widget(self.button3)
        box_botoes.add_widget(self.button4)
        box_botoes.add_widget(self.button5)
        box_botoes.add_widget(self.button6)
        box_botoes.add_widget(self.button7)
        box_botoes.add_widget(self.button8)
        box_botoes.add_widget(self.button9)
        box_botoes.add_widget(self.button10)
        box_botoes.add_widget(self.button11)
        box_botoes.add_widget(self.button12)
        box_botoes.add_widget(self.button13)
        box_botoes.add_widget(self.button0)
        box_botoes.add_widget(self.button_soma)
        box_botoes.add_widget(self.button_igual)

        self.buttonC.bind(on_press = self.zerar)
        self.buttonPow.bind(on_press = self.armazenar)
        self.buttonSquare.bind(on_press = self.armazenar)
        self.buttonPerc.bind(on_press = self.armazenar)
        self.button1.bind(on_press = self.armazenar)
        self.button2.bind(on_press = self.armazenar)
        self.button3.bind(on_press = self.armazenar)
        self.button4.bind(on_press = self.armazenar)
        self.button5.bind(on_press = self.armazenar)
        self.button6.bind(on_press = self.armazenar)
        self.button7.bind(on_press = self.armazenar)
        self.button8.bind(on_press = self.armazenar)
        self.button9.bind(on_press = self.armazenar)
        self.button10.bind(on_press = self.armazenar)
        self.button11.bind(on_press = self.armazenar)
        self.button12.bind(on_press = self.armazenar)
        self.button0.bind(on_press = self.armazenar)
        self.button13.bind(on_press = self.armazenar)
        self.button_soma.bind(on_press = self.armazenar)
        self.button_igual.bind(on_press = self.calcular)


        # layout.add_widget(self.button_zerar)
        layout.add_widget(self.display)
        layout.add_widget(box_botoes)

        return layout

    #def hello(self,event):
     #   print("Hello")
      #  print(event.text)    

    def zerar(self,event):
        #print(self.display.text)
        self.display.text = '' ##ZERANDO O DISPLAY DA CALCULADORA

    def armazenar(self,event):
        # print(event.text)
        self.display.text += event.text ##pega o texto do evento(evento é o botao pressionado no bind e on_press) e joga no display

    def calcular(self,event):
        if '+' in self.display.text:
            numbers = self.display.text.split('+')
            soma = float(numbers[0]) + float(numbers[1])
        elif '-' in self.display.text:
            numbers = self.display.text.split('-')
            soma = float(numbers[0]) - float(numbers[1])
        elif '*' in self.display.text:
            numbers = self.display.text.split('*')
            soma = float(numbers[0]) * float(numbers[1])
        elif '/' in self.display.text:
            numbers = self.display.text.split('/')
            if float(numbers[1]) == 0:
                self.display.text = "Erro"
                return
            soma = float(numbers[0]) / float(numbers[1])
        elif '^' in self.display.text:
            numbers = self.display.text.split('^')
            soma = float(numbers[0]) ** float(numbers[1])
        elif '√' in self.display.text:
            number = self.display.text.replace('√','')
            try:
                num = float(number)
                if num < 0:
                    self.display.text = "Erro" 
                    return
                soma = num ** 0.5
            except ValueError:
                    self.display.text = "Erro"
        elif '%' in self.display.text:
            number = self.display.text.split('%')
            soma = (float(numbers[0]) * float(numbers[1])) / 100
        else:
            return
        self.display.text = str(soma)    


if __name__ == "__main__"    :
    MyCalc().run()