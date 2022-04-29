from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.window.add_widget(Image(source="Central Albania.png"))

       
        self.button = Button(
                      text= "Welcome",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00c2cb',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Hello " + self.user.text + "!"

# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
