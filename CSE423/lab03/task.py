#!/usr/bin/env python3


#####################################################
######## CSE423_Lab03          #####################
######## Abir Ahammed Bhuiyan  ##################
######## 20101197              ################
######## section: 01           ##############
##########################################


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from CircleModule import Circle


class CircleScene:
    def __init__(self):
        self.width = self.height = 600
        self.speed = 0.1
        self.freeze = False
        self.background = 0
        self.circles = []

    def drawCircles(self):
        for circle in self.circles:
            circle.draw()

    def checkCollision(self):
        if not self.freeze:
            for idx, circle in enumerate(self.circles):
                if circle.x-circle.radius < 0 or circle.x+circle.radius > self.width or circle.y-circle.radius < 0 or circle.y+circle.radius > self.height:
                    self.circles.pop(idx)


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
        self.checkCollision()
        self.drawCircles()
        glutSwapBuffers()
        

    def animate(self):
        if not self.freeze:
            for circle in self.circles:
                circle.radius += self.speed
        glutPostRedisplay()


    def keyboardListener(self, key, x, y):
        if key == b' ':
            self.freeze = False if self.freeze else True
        glutPostRedisplay()


    def mouseListener(self, button, state, x, y):
        if not self.freeze:
            if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
                self.circles.append(Circle(x=x, y=self.height-y, radius=1, weight=2, color=(1, 0, 0)))
        glutPostRedisplay()


    def specialKeyListener(self, key, x, y):
        if not self.freeze:
            if key == GLUT_KEY_RIGHT:
                if self.speed >= 0.0001:
                    self.speed -= 0.01
            if key == GLUT_KEY_LEFT:
                if self.speed <= 1:
                    self.speed += 0.01


    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("OpenGL Circle Spawn")
        glutDisplayFunc(self.showScreen)
        glutIdleFunc(self.animate)
        glutKeyboardFunc(self.keyboardListener)
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()


if __name__ == "__main__":
    CircleScene().run()

