
helper_str = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
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
                                on_press: root.manager.current = 'profile'
                                IconLeftWidget:
                                    icon: 'face-profile-woman'

                            OneLineIconListItem:
                                text: 'Upload'
                                on_press: root.manager.current = 'upload'
                                IconLeftWidget:
                                    icon: 'file-upload'
                                    
                            OneLineIconListItem:
                                text: 'LogOut'
                                IconLeftWidget:
                                    icon: 'logout'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Sonu'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'lets upload somthing.'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'


"""