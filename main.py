from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineListItem
from kivy.uix.camera import Camera
screen_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'SMAP'
                        left_action_items: [["menu",lambda x: nav_drawer.set_state()]]
                        elevation: '9'
                    Widget:

                    MDBottomAppBar:
                        
                        MDToolbar:
                            icon: 'camera'
                            left_action_items: [['', lambda x: nav_drawer.set_state()]]
                            mode: 'end'
                            type: 'bottom'
                            on_action_button: app.open_camera()
                    Button:
                        background_color: 0, 0, 0, 0
                        text: 'help'
                        size_hint_x: None
                        size_hint_y: None
                        width: 100
                        height: 50
                    BoxLayout:
                        id: cam
        MDNavigationDrawer:
            id: nav_drawer
      
        
"""

# Window.size = (360, 680)


class DemoApp(MDApp):
    def on_start(self):
        for i in range(20):
            item = ThreeLineListItem(text='Item ' + str(i + 1))
            self.root.ids.container.add_widget(item)

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def open_camera(self):
        cam = Camera(resolution=(350, 400), play=True)
        self.root.ids.cam.add_widget(cam)


DemoApp().run()
