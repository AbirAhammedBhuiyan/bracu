#!/usr/bin/env python3



#####################################################
######## CSE423_Lab02          ####################
######## Abir Ahammed Bhuiyan  ##################
######## 20101197              ################
######## section: 01           ##############
##########################################



from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from LineModule import Line
from Components import *

import random
import time



class Game:
    def __init__(self):
        self.width = 500
        self.height = 800
        self.pot_speed = 100
        self.diamond_speed = 8
        self.pot = Pot()
        self.diamond = None
        self.score = 0
        self.freeze = False
        self.gameOver = False
        self.prev_time = time.time()
        self.dt = 0
        self.fps = 30


    def calcDeltaTime(self):
        self.dt = time.time() - self.prev_time
        self.prev_time = time.time()
        self.dt *= self.fps


    def generateDiamond(self):
        if not self.diamond:
            self.diamond = Diamond(x=random.randint(25, 475), y=710)


    def checkBoundary(self):
        if self.diamond and self.diamond.y <= 0:
            self.diamond = None
            self.gameOver = True
            print(f"Game Over! Score: {self.score}")

    def collisionCheck(self):
        if self.diamond and self.pot:
            d_vl_x, d_vl_y = self.diamond.getLeftVertex()
            d_vr_x, d_vr_y = self.diamond.getRightVertex()

            p_vl_x, p_vl_y = self.pot.getLeftVertex()
            p_vr_x, p_vr_y = self.pot.getRightVertex()

            if p_vl_y >= d_vr_y or p_vr_y >= d_vl_y: 
                if (d_vl_x <= p_vr_x and d_vl_x >= p_vl_x) or (d_vr_x >= p_vl_x and d_vr_x <= p_vr_x):
                    # self.diamond_speed += 0.5
                    self.diamond = None
                    self.score += 1
                    self.diamond_speed += 0.25
                    print(f"Score: {self.score}")


    def drawComp(self):
        # Line(0, 720, 500, 720)
        # Line(160, 720, 160, 800)
        # Line(320, 720, 320, 800)

        if self.diamond:
            self.diamond.draw()

        Arrow().draw()
        Pause().draw() if not self.freeze else Play().draw()
        Cross().draw()

        self.pot.draw((0.941, 0.086, 0.086)) if self.gameOver else self.pot.draw()


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
        glClearColor(0, 0, 0, 1.0)

        self.calcDeltaTime()

        if not self.gameOver:
            self.generateDiamond()
        self.drawComp()
        self.collisionCheck()
        self.checkBoundary()
        glutSwapBuffers()
        

    def animate(self):
        if self.diamond and not self.freeze:
            self.diamond.y -= self.diamond_speed * self.dt
        glutPostRedisplay()


    def checkButton(self, x, y):
        if (y >= 720 and y <= 800):
            if (x <= 160 and x >= 0):
                self.score = 0
                self.gameOver = False
                self.diamond = None
                print("Starting Over!")
            elif (x <= 320 and x >= 165):
                self.freeze = True if not self.freeze else False
            elif (x <= 500 and x >= 325):
                glutLeaveMainLoop()
            else:
                print("Can't Recognize")


    def keyboardListener(self, key, x, y):
        pass


    def mouseListener(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.checkButton(x, self.height - y)
        glutPostRedisplay()


    def specialKeyListener(self, key, x, y):
        if not self.gameOver and not self.freeze:
            if key == GLUT_KEY_LEFT:
                if not self.pot.getLeftVertex()[0] <= 0:
                    self.pot.x -= self.pot_speed * self.dt
            if key == GLUT_KEY_RIGHT:
                if not self.pot.getRightVertex()[0] >= self.width:
                    self.pot.x += self.pot_speed * self.dt
        glutPostRedisplay()


    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("OpenGL Catch The Diamond")
        glutDisplayFunc(self.showScreen)
        glutIdleFunc(self.animate)
        glutKeyboardFunc(self.keyboardListener)
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()



if __name__ == "__main__":
    Game().run()

