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
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'me.jpeg'

                MDLabel:
                    text: '    Sonu'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: '    mahajan00sonu@gmail.com'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile-woman'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'LogOut'
                            IconLeftWidget:
                                icon: 'logout'

"""
class MainApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper)
        return screen

MainApp().run()
