from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Calculadora(App):
    def build(self):
        self.resultado = Label(text='0', font_size=32, size_hint=(1, 0.2))
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical')
        
        # Layout para o display (tela de resultado)
        main_layout.add_widget(self.resultado)
        
        # Layout para os botões
        grid = GridLayout(cols=4, spacing=10, padding=10)
        
        # Definindo os botões da calculadora
        buttons = [
            ('7', self.update_display), ('8', self.update_display), ('9', self.update_display), ('/', self.update_display),
            ('4', self.update_display), ('5', self.update_display), ('6', self.update_display), ('*', self.update_display),
            ('1', self.update_display), ('2', self.update_display), ('3', self.update_display), ('-', self.update_display),
            ('0', self.update_display), ('.', self.update_display), ('+', self.update_display), ('=', self.calculate),
            ('C', self.clear_display)
        ]
        
        # Adicionando os botões à Grid
        for (text, callback) in buttons:
            btn = Button(text=text, font_size=32, size_hint=(1, 1))
            btn.bind(on_press=lambda btn, text=text: callback(text))
            grid.add_widget(btn)
        
        # Adicionando a grid com os botões ao layout principal
        main_layout.add_widget(grid)
        
        return main_layout
    
    def update_display(self, text):
        # Atualiza o display com os números ou operadores pressionados
        current_text = self.resultado.text
        if current_text == '0' or current_text == 'ERROR':
            self.resultado.text = text
        else:
            self.resultado.text += text
    
    def clear_display(self, text):
        # Limpa o display
        self.resultado.text = '0'
    
    def calculate(self, text):
        # Realiza o cálculo quando o botão "=" é pressionado
        try:
            result = eval(self.resultado.text)
            self.resultado.text = str(result)
        except Exception:
            self.resultado.text = 'ERROR'

if __name__ == "__main__":
    Calculadora().run()
