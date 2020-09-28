from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

usr_helper = """ 
MDTextField:
    hint_text: "Enter Username: "
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x: None
    width: 300
    helper_text: "click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color

"""

class MainApp(MDApp):

    def build(self):
        scrn = Screen()
        self.theme_cls.primary_palette = "Red"

        # using coding insted of builder
        # usr = MDTextField(text="Enter username:", pos_hint={'center_x':0.5, 'center_y':0.5},
        #                     size_hint_x=None, width=300)

        # using builder to create
        self.usr = Builder.load_string(usr_helper)

        btn = MDRectangleFlatButton(text="Show", pos_hint={'center_x':0.5, 'center_y':0.4},
                                    on_release=self.show_data)

        scrn.add_widget(self.usr)
        scrn.add_widget(btn)
        return scrn
    
    def show_data(self, obj):
        if self.usr.text is "":
            check_string = "please enter a username."
        else:
            check_string = self.usr.text

         #creating dilogbox
        close_button = MDFlatButton(text='Close', on_release=self.close_dilog)
        more_button = MDFlatButton(text='More')
        self.dilog = MDDialog(title="Check", text=check_string, size_hint=(0.7,1),
                        buttons=[close_button, more_button])
        self.dilog.open()
    
    def close_dilog(self, obj):
        self.dilog.dismiss()

        

MainApp().run()
