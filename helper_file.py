
helper_str = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    LoginScreen:
    BcaScreen:
    BcomScreen:
    BaScreen:
    BbaScreen:
    McomScreen:
    MaScreen:
    PgdcaScreen:
    oldquesScreen:

<MenuScreen>:
    name: 'menu'
    Screen:
        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Study Material App '
                            left_action_items: [["menu", lambda x: nav_drawer.set_state()]]  # you can use toggle_nav_drawer insted of set state
                            elevation: 10
                        Widget:
                    ScrollView:
                        size_hint: (1.1, 0.85)
                        pos_hint: {'center_x': .55, 'y': .05}
                        MDList:
                            OneLineIconListItem:
                                id: 'bca141'
                                text: 'BCA'
                                on_press: root.manager.current = 'bca'
                                IconLeftWidget:
                                    icon: 'laptop'
                            OneLineIconListItem:
                                text: 'BCom'
                                on_press: root.manager.current = 'bcom'
                                IconLeftWidget:
                                    icon: 'bank-plus'
                            OneLineIconListItem:
                                text: 'BA'
                                on_press: root.manager.current = 'ba'
                                IconLeftWidget:
                                    icon: 'pencil-circle'
                            OneLineIconListItem:
                                text: 'BBA'
                                on_press: root.manager.current = 'bba'
                                IconLeftWidget:
                                    icon: 'account-badge-horizontal-outline'
                            OneLineIconListItem:
                                text: 'MCom'
                                on_press: root.manager.current = 'mcom'
                                IconLeftWidget:
                                    icon: 'account-badge-horizontal'
                            OneLineIconListItem:
                                text: 'MA'
                                on_press: root.manager.current = 'ma'
                                IconLeftWidget:
                                    icon: 'bolnisi-cross'
                            OneLineIconListItem:
                                text: 'PGDCA'
                                on_press: root.manager.current = 'pgdca'
                                IconLeftWidget:
                                    icon: 'alpha-p-box'
                            OneLineIconListItem:
                                id: 'bca141'
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
                                text: 'Login'
                                on_press: root.manager.current = 'login'
                                IconLeftWidget:
                                    icon: 'login'


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

<LoginScreen>:
    name: 'login'
    MDLabel:
        text: 'let login here.'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<BcaScreen>:
    name: 'bca'
    MDLabel:
        text: 'BCA'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: root.manager.current = 'oldques'
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')
        # MDRectangleFlatButton:
        #     text: 'Back'
        #     pos_hint: {'center_x':0.5, 'center_y':0.2}
        #     on_press: root.manager.current = 'menu'

<BcomScreen>:
    name: 'bcom'
    MDLabel:
        text: 'BCom'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('0')
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')
   

<BaScreen>:
    name: 'ba'
    MDLabel:
        text: 'BA'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('0')
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')


<BbaScreen>:
    name: 'bba'
    MDLabel:
        text: 'BBA'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('0')
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')

<McomScreen>:
    name: 'mcom'
    MDLabel:
        text: 'MCom'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('0')
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')

<MaScreen>:
    name: 'ma'
    MDLabel:
        text: 'MA'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('0')
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')

<PgdcaScreen>:
    name: 'pgdca'
    MDLabel:
        text: 'PGDCA'
        font_style: 'H5'
        color: 0.1, 0.5, 0.6, 1 
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {'x':0.45, 'y':0.94}
    BoxLayout:
        padding: 40
        spacing: 40
        orientation: 'vertical'
        pos_hint: {'x':0, 'y':-0.01}
        Button:
            text: 'Previous year Question Papers'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('0')
        Button:
            text: 'Important Questions'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('1')
        Button:
            text: 'Notes'
            font_size: 20
            background_color: 0.1, 0.5, 0.6, 1 
            on_release: print('2')

<oldquesScreen>:
    name: 'oldques'
    Screen: 
        name: 'itemscad_oldques'
        BoxLayout:
            id: boxcad
            orientation: 'vertical'
            MDToolbar:
                id: toolcad
                title: "Select Semester"
                md_bg_color: app.theme_cls.primary_color
                anchor_title: 'justify'
                # left_action_items: [['menu-left', lambda x: app.back_button()]]      #for back button but showing errors
            BoxLayout:
                id: tabox
                orientation: 'vertical'
                MDTabs:
                    id: itemstab
                    tab_display_mode: 'text'            

                    MDTabsBase:
                        id: ingr_tab
                        name: 'Semester 1'
                        text: "Semester 1"                                                

                    MDTabsBase:
                        id: prod_tab
                        name: 'Semester 3'
                        text: "Semester 3"

                    MDTabsBase:
                        id: pack_tab
                        name: 'Semester 5'
                        text: "Semester 5"

            FloatLayout:       
                BoxLayout:
                    id: listbox
                    size_hint_y: None
                    height: boxcad.height - (toolcad.height + itemstab.tab_bar_height)
                    orientation: 'vertical'
                    ScrollView:
                        do_scroll_x: False
                        MDList:     
                            OneLineRightIconListItem:
                                text: 'Strawberry Cake'
                            OneLineRightIconListItem:
                                text: 'Chocolate Cake'
                            OneLineRightIconListItem:
                                text: 'Vanilla Cake'



"""
