from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from helper_file import helper_str


Window.size = (380,620)


class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class BcaScreen(Screen):
    pass

class BcomScreen(Screen):
    pass

class BaScreen(Screen):
    pass

class BbaScreen(Screen):
    pass

class McomScreen(Screen):
    pass

class MaScreen(Screen):
    pass

class PgdcaScreen(Screen):
    pass



sm = ScreenManager()

sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(BcaScreen(name='bca'))
sm.add_widget(BcomScreen(name='bcom'))
sm.add_widget(BaScreen(name='ba'))
sm.add_widget(BbaScreen(name='bba'))
sm.add_widget(McomScreen(name='mcom'))
sm.add_widget(MaScreen(name='ma'))
sm.add_widget(PgdcaScreen(name='pgdca'))

class MainApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper_str)
        return screen

MainApp().run()



