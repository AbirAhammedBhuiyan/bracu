#!/usr/bin/env python3


#####################################################
######## CSE423_Lab01_Task01   ####################
######## Abir Ahammed Bhuiyan  ##################
######## 20101197              ################
######## section: 01           ##############
##########################################


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random



class Rain:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



class RainScene:
    def __init__(self):
        self.width = self.height = 500
        self.rain_size = 2
        self.rain_drop_list = []
        self.rain_speed = 0.05
        self.rain_density = 0.009
        self.rain_angle = 0
        self.background = 0


    def drawHouse(self):
        glBegin(GL_QUADS)
        glColor3f(0.44, 0.22, 0.22)
        glVertex2f(300, 0)
        glVertex2f(150, 0)
        glVertex2f(150, 130)
        glVertex2f(300, 130)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.47, 0.75, 0.46)
        glVertex2f(330, 130)
        glVertex2f(120, 130)
        glVertex2f(225, 250)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.48, 0.13, 0.6)
        glVertex2f(250, 35)
        glVertex2f(200, 35)
        glVertex2f(200, 84)
        glVertex2f(250, 84)
        glEnd()


    def rainMaker(self):
        delay = random.random()
        if delay < self.rain_density:
            x1 = random.randint(-800, self.width+800)
            y1 = self.height
            x2 = x1
            y2 = self.height+random.randint(20, 70)
            self.rain_drop_list.append(Rain(x1, y1, x2, y2))


    def drawRain(self):
        for rain in self.rain_drop_list:
            glPushMatrix()
            glTranslatef((rain.x1 + rain.x2)/2, (rain.y1 + rain.y2)/2, 0)
            glRotatef(self.rain_angle, 0, 0, 1)
            glTranslatef(-(rain.x1 + rain.x2)/2, -(rain.y1 + rain.y2)/2, 0)
            glLineWidth(self.rain_size)
            glBegin(GL_LINES)
            glColor3f(0.39, 0.4, 1)
            glVertex2f(rain.x1, rain.y1)
            glVertex2f(rain.x2, rain.y2)
            glEnd()
            glPopMatrix()


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
        self.rainMaker()
        self.drawRain()
        self.drawHouse()
        glutSwapBuffers()
        

    def animate(self):
        for idx, rain in enumerate(self.rain_drop_list):
            if rain.y1 >= 0 and rain.y1 <= self.height:
                if self.rain_angle < -5 and self.rain_angle >= -45:
                    rain.x1 -= self.rain_speed
                    rain.x2 -= self.rain_speed
                    rain.y1 -= self.rain_speed
                    rain.y2 -= self.rain_speed
                if self.rain_angle > 5 and self.rain_angle <= 45:
                    rain.x1 += self.rain_speed
                    rain.x2 += self.rain_speed
                    rain.y1 -= self.rain_speed
                    rain.y2 -= self.rain_speed
                if self.rain_angle > -5 and self.rain_angle < 5:
                    rain.y1 -= self.rain_speed
                    rain.y2 -= self.rain_speed
            else:
                self.rain_drop_list.pop(idx)
        glutPostRedisplay()


    def keyboardListener(self, key, x, y):
        if key == b"=": # + key
            self.rain_density += 0.001
        if key == b"-":
            self.rain_density -= 0.001
        if key == b"f":
            self.rain_speed += 0.01
        if key == b"s":
            self.rain_speed -= 0.01
        glutPostRedisplay()


    def mouseListener(self, button, state, x, y):
        pass


    def specialKeyListener(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            if not self.rain_angle >= 45:
                self.rain_angle += 1
        if key == GLUT_KEY_LEFT:
            if not self.rain_angle <= -45:
                self.rain_angle -= 1
        if key == GLUT_KEY_UP:
            if not self.background > 1:
                self.background += 0.05
        if key == GLUT_KEY_DOWN:
            if not self.background < 0:
                self.background -= 0.05
        glutPostRedisplay()


    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("OpenGL Rain Drop")
        glutDisplayFunc(self.showScreen)
        glutIdleFunc(self.animate)
        glutKeyboardFunc(self.keyboardListener)
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()


if __name__ == "__main__":
    RainScene().run()

