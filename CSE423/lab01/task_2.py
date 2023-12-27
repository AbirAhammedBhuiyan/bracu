#!/usr/bin/env python3


#####################################################
######## CSE423_Lab01_Task02   ####################
######## Abir Ahammed Bhuiyan  ##################
######## 20101197              ################
######## section: 01           ##############
##########################################


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random



class Point:
    def __init__(self, x, y):
        self.size = 10 
        self.r = random.random()
        self.g = random.random()
        self.b = random.random()
        self.x = x
        self.y = y
        self.direction_x = int(random.sample([1, -1], 1)[0])
        self.direction_y = int(random.sample([1, -1], 1)[0])

    def __str__(self):
        return f"RGB -> ({self.r}, {self.g}, {self.b})"



class PointScene:
    def __init__(self):
        self.width = self.height = 500
        self.background = 0
        self.speed = 0.001
        self.point_number = 5
        self.point_list = []
        self.blink = False
        self.freeze = False


    def makePoints(self, x, y):
        for _ in range(self.point_number):
            self.point_list.append(Point(x, self.height-y))


    def drawPoints(self):
        for point in self.point_list:
            glPointSize(point.size)
            glBegin(GL_POINTS)
            if self.blink and not self.freeze:
                if not random.randint(0, 50)%2:
                    glColor3f(point.r, point.g, point.b)
                else:
                    glColor3f(self.background, self.background, self.background)
            else:
                glColor3f(point.r, point.g, point.b)
            glVertex2f(point.x, point.y)
            glEnd()


    def iterate(self):
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.width, 0.0, self.height, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


    def showScreen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.iterate()
        glClearColor(self.background, self.background, self.background, 1.0)
        self.drawPoints()
        glutSwapBuffers()
        

    def animate(self):
        if not self.freeze:
            for point in self.point_list:
                point.x += point.direction_x * self.speed
                point.y += point.direction_y * self.speed
        glutPostRedisplay()


    def keyboardListener(self, key, x, y):
        if key == b' ':
            self.freeze = False if self.freeze else True
        glutPostRedisplay()


    def mouseListener(self, button, state, x, y):
        if not self.freeze:
            if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
                self.makePoints(x, y)
            if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
                self.blink = False if self.blink else True
        glutPostRedisplay()


    def specialKeyListener(self, key, x, y):
        if not self.freeze:
            if key == GLUT_KEY_UP:
                self.speed += 0.001
            if key == GLUT_KEY_DOWN:
                self.speed -= 0.001
        glutPostRedisplay()


    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("OpenGL Point Spawn")
        glutDisplayFunc(self.showScreen)
        glutIdleFunc(self.animate)
        glutKeyboardFunc(self.keyboardListener)
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()


if __name__ == "__main__":
    PointScene().run()

