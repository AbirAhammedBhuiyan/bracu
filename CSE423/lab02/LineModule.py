#!/usr/bin/env python3



from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



class Line:
    def __init__(self, x0, y0, x1, y1, size = 1, color = (1, 1, 1)):
        self.size = size
        self.color = color

        self.zoneZero = {
                0: lambda x, y: (x, y),
                1: lambda x, y: (y, x),
                2: lambda x, y: (y, -x),
                3: lambda x, y: (-x, y),
                4: lambda x, y: (-x, -y),
                5: lambda x, y: (-y, -x),
                6: lambda x, y: (-y, x),
                7: lambda x, y: (x, -y),
                }

        self.zoneOriginal = {
                0: lambda x, y: (x, y),
                1: lambda x, y: (y, x),
                2: lambda x, y: (-y, x),
                3: lambda x, y: (-x, y),
                4: lambda x, y: (-x, -y),
                5: lambda x, y: (-y, -x),
                6: lambda x, y: (y, -x),
                7: lambda x, y: (x, -y),
                }

        self.zone = self.findZone(x0, y0, x1, y1)
        # print(f"{self.zone} -> zone")

        x0, y0 = self.zoneZero[self.zone](x0, y0)
        x1, y1 = self.zoneZero[self.zone](x1, y1)
        # print(f"({x0}, {y0}) ({x1}, {y1}) -> converted")
        
        self.midPointAlgo(x0, y0, x1, y1)


    def findZone(self, x0, y0, x1, y1):
        dy = y1 - y0
        dx = x1 - x0

        if (abs(dx) > abs(dy)):
            if (dx >= 0 and dy >= 0):
                return 0
            elif (dx <= 0 and dy >= 0):
                return 3
            elif (dx <= 0 and dy <= 0):
                return 4
            else:
                return 7
        else:
            if (dx >= 0 and dy >= 0):
                return 1
            elif (dx <= 0 and dy >= 0):
                return 2
            elif (dx <= 0 and dy <= 0):
                return 5
            else:
                return 6


    def drawPoint(self, x, y):
        glPointSize(self.size)
        glBegin(GL_POINTS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        glVertex2f(x, y)
        glEnd()


    def midPointAlgo(self, x0, y0, x1, y1):
        dy = y1 - y0
        dx = x1 - x0
        d_init = 2*dy - dx
        incE = 2*dy
        incNE = 2*(dy - dx)

        while (x0 <= x1):
            a, b = self.zoneOriginal[self.zone](x0, y0)
            self.drawPoint(a, b)
            # print(f"{a}, {b} done")

            x0 += 1

            if d_init <= 0:
                d_init += incE
            else:
                y0 += 1
                d_init += incNE


