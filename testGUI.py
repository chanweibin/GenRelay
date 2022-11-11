from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyScreen(GridLayout):
    
    def __init__(self, **kwargs) -> GridLayout:
        super(MyScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        
        
class MyApp(App):
    
    def build(self): 
        return Button(text="HW", halign="right", valign="bottom", texture_size=[5,5])
    
MyApp().run()