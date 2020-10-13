
helper_str = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    BcaScreen:
    BcomScreen:
    BaScreen:

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
                    ScrollView:
                        size_hint: (0.99, 0.55)
                        pos_hint: {'center_x': .55, 'y': .35}
                        MDList:
                            OneLineIconListItem:
                                text: 'BCA'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'laptop'
                            OneLineIconListItem:
                                text: 'BCom'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'bank-plus'
                            OneLineIconListItem:
                                text: 'BA'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'pencil-circle'
                            OneLineIconListItem:
                                text: 'BBA'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'account-badge-horizontal-outline'
                            OneLineIconListItem:
                                text: 'MCom'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'account-badge-horizontal'
                            OneLineIconListItem:
                                text: 'MA'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'bolnisi-cross'
                            OneLineIconListItem:
                                text: 'PGDCA'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'alpha-p-box'

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'

                    Image:
                        source: 'images/me.jpeg'

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

<BcaScreen>:
    name: 'bca'
    MDCard:
        # on_press: root.manager.current = 'bca2'   not using
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "250dp", "150dp"
        pos_hint: {"center_x": .5, "center_y": .8}
        MDLabel:
            text: "Previous year Question Papers"
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "250dp", "150dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        MDLabel:
            text: "Important Questions"
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "250dp", "150dp"
        pos_hint: {"center_x": .5, "center_y": .2}
        MDLabel:
            text: "Notes"
            # pos_hint_x: {"center_x": .5}   not working

"""