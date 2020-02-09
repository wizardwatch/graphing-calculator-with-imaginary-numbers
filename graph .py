import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from numpy import *
points = []
def Cube():
        #else:
        #    z_cord.append (y.imag)
    verticies = [
        (0, -1, -0),
        (0,1, 0),
        (1, 0, -0),
        (-1,0, 0),
        (0, 0, -1),
        (0,0, 1)
    ]
    edges = [
        (0,1),
        (2,3),
        (4,5)
    ]
    graph = [
        (0,1),
        (1,2),
        (2,3),


    ]


    x= 0
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    try:
        x_cord = (
            (0),
            (1),
            (2),
            (3),
            (4),
            (5)
        )

        def formula(a):
            transformations = "(-2)**x"
            varplace = transformations.find("x")
            return transformations.replace("x", str(a))
        for number in x_cord:
            expression = formula(number)
            print (expression)
            y = eval(expression)
            if (y.imag) == 0:
                print (y)
                point = (number, y, 0)
                print (point)
                points.append(point)
                print (points)
            else:
                z = y.imag
                print (z)
                point = (number, 0, z)
                print (point)
                points.append(point)
                print (points)
            try:
                for edge in graph:
                    for vertex in edge:
                        glVertex3fv(points[vertex])
            except:
                print("graphing failed")

    except:
        print("calculation failded")
    glEnd()
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1.0,0.0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1.0,0.0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0.0,1.0,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0,-1.0,0)
                if event.key == pygame.K_w:
                    print ("you pressed w")
                    glRotatef(1, 10, 0, 0)
                if event.key == pygame.K_s:
                    glRotatef(1, -10, 0, 0)
                if event.key == pygame.K_a:
                    glRotatef(1, 10, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        glRotatef(100, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(100)
main()
