from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CashRewardApp(App):
    def build(self):
        self.points = 0
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(text='Points: 0', font_size='32sp')
        btn = Button(text='Earn Coin', font_size='24sp')
        btn.bind(on_press=self.add_points)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def add_points(self, instance):
        self.points += 10
        self.label.text = f'Points: {self.points}'

if __name__ == '__main__':
    CashRewardApp().run()
  
