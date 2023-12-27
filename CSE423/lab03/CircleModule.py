#!/usr/bin/env python3



from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



class Circle:
    def __init__(self, x=0, y=0, radius=10, weight=2, color=(1, 1, 1)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.weight = weight

        self.eightWaySymmetry = {
                0: lambda x, y: (y, x),
                1: lambda x, y: (x, y),
                2: lambda x, y: (-x, y),
                3: lambda x, y: (-y, x),
                4: lambda x, y: (-y, -x),
                5: lambda x, y: (-x, -y),
                6: lambda x, y: (x, -y),
                7: lambda x, y: (y, -x),
                }


    def draw(self):
        self.midpointCircleAlgo()


    def circlePoint(self, x, y):
        for i in range(0, 8):
            a, b = self.eightWaySymmetry[i](x, y)
            self.drawPoint(a+self.x, b+self.y)


    def drawPoint(self, x, y):
        glPointSize(self.weight)
        glBegin(GL_POINTS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        glVertex2f(x, y)
        glEnd()

    def midpointCircleAlgo(self):
        x = 0
        y = self.radius
        d = 1 - self.radius
        self.circlePoint(x, y)

        while (x < y):
            if (d < 0): # E
                d += 2*x + 3
                x += 1
            else:
                d += 2*x - 2*y + 5
                x += 1
                y -= 1
            self.circlePoint(x, y)

