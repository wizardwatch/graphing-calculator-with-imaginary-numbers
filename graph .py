import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
verticies = (
    (1, -1, -0),
    (1,1, 0),
    (1, 1, -0),
    (-1,1, 0),
    (1, 1, -0),
    (1,1, 1)
)

edges = (
    (0,1),
    (2,3),
    (4,5)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        #glRotatef(1, 3, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)
main()
