from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy3dgui.layout3d import Layout3D
from kivy3dgui.node import Node

class Layout_2D(FloatLayout):
    def __init__(self, **kwargs):
        super(Layout_2D, self).__init__(**kwargs)

        source = kwargs['source']
        image = Image(source=source, size_hint=(1.0,1.0), allow_stretch=True, keep_ratio=False)
        self.add_widget(image)

class Node_3D(Node):
    def __init__(self, **kwargs):
        super(Node_3D, self).__init__(**kwargs)

        position = kwargs['position']
        source = kwargs['source']
        if position == 'left':
            self.rotate = (80.0, 0.0, 1.0, 0.0)
            self.translate = (-50, 0, -150)
            self.scale = (0.4, 0.5, 0.4)
            self.effect = True
            self.meshes = ("./2dbox.obj", )
        elif position == 'left_out':
            self.rotate = (80.0, 0.0, 1.0, 0.0)
            self.translate = (-50, 0, 100)
            self.scale = (0.4, 0.5, 0.4)
            self.effect = True
            self.meshes = ("./2dbox.obj", )    
        elif position == 'right':
            self.rotate = (-80.0, 0.0, 1.0, 0.0)
            self.translate = (50, 0, -150)
            self.scale = (0.4, 0.5, 0.4)
            self.effect = True
            self.meshes = ("./2dbox.obj", )
        elif position == 'front':
            self.rotate = (0.0, 0.0, 1.0, 0.0)
            self.translate = (0, 0, -150)
            self.scale = (0.4, 0.5, 0.4)
            self.effect = True
            self.meshes = ("./2dbox.obj", )
        elif position == 'right_out':
            self.rotate = (-80.0, 0.0, 1.0, 0.0)
            self.translate = (50, 0, 100)
            self.scale = (0.4, 0.5, 0.4)
            self.effect = True
            self.meshes = ("./2dbox.obj", )
        else:
            # Default lay-down position at the boottom
            self.rotate = (-90.0, 1.0, 0.0, 0)
            self.scale = (0.4, 0.5, 0.4)
            self.translate = (-5, -25, -70)
            self.effect = True
            self.meshes = ("./2dbox.obj", )

        layout = Layout_2D(size_hint=(1.0, 1.0), source=source)
        self.add_widget(layout)

        # Show how Animation works on rotate and translate
        #
        # rotate(degree, x, y, z):
        # degree: rotation degree
        # x: 1.0: rotate along x axis, fall torward closer/farther
        # y: 1.0: rotate along y axis, fall torward left/right
        # z: 1.0: rotate along z axis, fall torward up/down

        # translate(x, y, z): 
        # x: move right (positve) or left (negative)
        # y: move up (positve) or down (negative)
        # z: move closer (positive) or farther (negative)

class Layout_3D(Layout3D):
    def __init__(self, **kwargs):
        super(Layout_3D, self).__init__(**kwargs)
        self.left_index = 0
        self.max_index = 4
        self.node3d={}

        self.node3d['0'] = Node_3D(size_hint=(1.0, 1.0), position='left', source='./Apple.jpg')
        self.add_widget(self.node3d['0'])
        self.node3d['1'] = Node_3D(size_hint=(1.0, 1.0), position='front', source='./Banana.jpg')
        self.add_widget(self.node3d['1'])
        self.node3d['2'] = Node_3D(size_hint=(1.0, 1.0), position='right', source='./Cantaloupe.jpg')
        self.add_widget(self.node3d['2'])
        self.node3d['3'] = Node_3D(size_hint=(1.0, 1.0), position='right_out', source='./Grapefruit.jpg')
        self.add_widget(self.node3d['3'])

        button1 = Button(size_hint=(0.15, 0.1), pos_hint={"x":0.0, "y":0.9}, text="rotate left", on_press=self.roll_left)
        button2 = Button(size_hint=(0.15, 0.1), pos_hint={"x":0.85, "y":0.9}, text="rotate right", on_press=self.roll_right)
        self.add_widget(button1)
        self.add_widget(button2)

    # Front position: Animation(rotate=(0.0, 0.0, 1.0, 0.0), translate=(0, 0, -150), duration=1.0)
    # Left position: Animation(rotate=(80.0, 0.0, 1.0, 0.0), translate=(-50, 0, -150), duration=1.0)
    # Right position: Animation(rotate=(-80.0, 0.0, 1.0, 0.0), translate=(50, 0, -150),duration=1.0)

    def roll_left(self, instance):
        if (self.left_index == 0):
            print 'Do nothing: already in left most position!'
        elif (self.left_index == 1):
            # Move widget right while rolling left!!!
            self.roll_widget_right(self.node3d['0'], "left-out")
            self.roll_widget_right(self.node3d['1'], "left")
            self.roll_widget_right(self.node3d['2'], "front")
            self.roll_widget_right(self.node3d['3'], "right")
            self.left_index = 0
        else:
            print "Do nothing: invalid left index position: %d" % left_index

    def roll_right(self, instance):
        if (self.left_index == 1):
            print 'Do nothing: already in right most position!'
        elif (self.left_index == 0):
            # Move widget left while rolling right!!!
            self.roll_widget_left(self.node3d['0'], "left")
            self.roll_widget_left(self.node3d['1'], "front")
            self.roll_widget_left(self.node3d['2'], "right")
            self.roll_widget_left(self.node3d['3'], "right-out")
            self.left_index = 1
        else:
            print "Do nothing: invalid left index position: %d" % left_index       

    def roll_widget_left(self, widget, cur_position):
        if (cur_position == 'left'): # Roll to left-out
            Animation(rotate=(80.0, 0.0, 1.0, 0.0), translate=(-50, 0, 100), duration=1.0).start(widget)
        elif (cur_position == 'front'): # Roll to the left
            Animation(rotate=(80.0, 0.0, 1.0, 0.0), translate=(-50, 0, -150), duration=1.0).start(widget)
        elif (cur_position == 'right'): # Roll to the front
            Animation(rotate=(0.0, 0.0, 1.0, 0.0), translate=(0, 0, -150), duration=1.0).start(widget)
        elif (cur_position == 'right-out'): # Roll to the right
            Animation(rotate=(-80.0, 0.0, 1.0, 0.0), translate=(50, 0, -150),duration=1.0).start(widget)
        else:
            print "Warning: invalid current position %s to roll left!!" % cur_position

    def roll_widget_right(self, widget, cur_position):
        if (cur_position == 'front'): # Roll to the right
            Animation(rotate=(-80.0, 0.0, 1.0, 0.0), translate=(50, 0, -150),duration=1.0).start(widget)
        elif (cur_position == 'right'): # Roll to the right-out
            Animation(rotate=(-80.0, 0.0, 1.0, 0.0), translate=(50, 0, 100), duration=1.0).start(widget)   
        elif (cur_position == 'left'): # Roll to the front
            Animation(rotate=(0.0, 0.0, 1.0, 0.0), translate=(0, 0, -150), duration=1.0).start(widget)
        elif (cur_position == 'left-out'): # Roll to the left
            Animation(rotate=(80.0, 0.0, 1.0, 0.0), translate=(-50, 0, -150), duration=1.0).start(widget)
        else:
            print "Warning: invalid c urrent position %s to roll right!!" % cur_position


class Slideshow3dApp(App):
    def build(self):
        layout = Layout_3D()
        return layout

if __name__ == '__main__':
    Slideshow3dApp().run()
