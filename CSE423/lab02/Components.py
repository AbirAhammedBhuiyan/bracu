#!/usr/bin/env python3



from LineModule import Line

import random



class Diamond:
    def __init__(self, x, y, d=25, width=3):
        self.x = x
        self.y = y
        self.d = d
        self.color = (random.random(), random.random(), random.random())
        self.width = 3


    def draw(self):
        Line(self.x, self.y + self.d, self.x + self.d, self.y, self.width, self.color)
        Line(self.x, self.y + self.d, self.x - self.d, self.y, self.width, self.color)
        Line(self.x - self.d, self.y, self.x, self.y - self.d, self.width, self.color)
        Line(self.x + self.d, self.y, self.x, self.y - self.d, self.width, self.color)


    def getRightVertex(self):
        vr_x = self.x + self.d
        vr_y = self.y - self.d

        return vr_x, vr_y


    def getLeftVertex(self):
        vl_x = self.x - self.d
        vl_y = self.y - self.d

        return vl_x, vl_y



class Pot:
    def __init__(self, x=250, y=20, width=2):
        self.x = x
        self.y = y
        self.height = 30
        self.width = width


    def draw(self, color=(1, 1, 1)):
        Line(self.x+50, self.y, self.x-50, self.y, self.width, color)
        Line(self.x+50, self.y, self.x+70, self.y+30, self.width, color)
        Line(self.x-50, self.y, self.x-70, self.y+30, self.width, color)
        Line(self.x+70, self.y+30, self.x-70, self.y+30, self.width, color)


    def getRightVertex(self):
        vr_x = self.x + 70
        vr_y = self.y + self.height

        return vr_x, vr_y


    def getLeftVertex(self):
        vl_x = self.x - 70
        vl_y = self.y + self.height

        return vl_x, vl_y
    


class Arrow:
    def __init__(self, x=70, y=760, d=25, width=3, color=(0, 0.705, 0.705)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.color = color
        self.vertex_x =  self.x - self.d
        self.vertex_y = self.y


    def draw(self):
        Line(self.x, self.y, self.x + self.d, self.y, self.width, self.color)
        Line(self.x, self.y, self.vertex_x, self.vertex_y, self.width, self.color)
        Line(self.vertex_x, self.vertex_y, self.x, self.y + self.d, self.width, self.color)
        Line(self.vertex_x, self.vertex_y, self.x, self.y - self.d, self.width, self.color)
        


class Pause:
    def __init__(self, x=240, y=760, d=25, width=3, color=(0.125, 0.660, 0.286)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.space = 15
        self.color = color


    def draw(self):
        Line(self.x + self.space, self.y + self.d, self.x + self.space, self.y - self.d, self.width, self.color)
        Line(self.x - self.space, self.y + self.d, self.x - self.space, self.y - self.d, self.width, self.color)



class Play:
    def __init__(self, x=240, y=760, d=25, width=3, color=(0.125, 0.660, 0.286)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.color = color
        self.vertex_x =  self.x + self.d
        self.vertex_y = self.y


    def draw(self):
        Line(self.x, self.y + self.d, self.x, self.y - self.d, self.width, self.color)
        Line(self.vertex_x, self.y, self.x, self.y + self.d, self.width, self.color)
        Line(self.vertex_x, self.y, self.x, self.y - self.d, self.width, self.color)



class Cross:
    def __init__(self, x=400, y=760, d=25, width=3, color=(0.840, 0.0924, 0.0924)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.color = color


    def draw(self):
        Line(self.x, self.y, self.x + self.d, self.y + self.d, self.width, self.color)
        Line(self.x, self.y, self.x + self.d, self.y - self.d, self.width, self.color)
        Line(self.x, self.y, self.x - self.d, self.y + self.d, self.width, self.color)
        Line(self.x, self.y, self.x - self.d, self.y - self.d, self.width, self.color)

