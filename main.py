from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (380,620)

helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo Application'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]  # you can use toggle_nav_drawer insted of set state
                        elevation: 10
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

"""
class MainApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper)
        return screen

MainApp().run()
