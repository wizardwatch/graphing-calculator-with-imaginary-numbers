import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from numpy import *
points = []
graph = []
xcordconnect=-200
connect1 = 0
connect2 =1
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
x= 0
x_cord = ()
max_x = 10
xcord1 = -10
print(x_cord)
while xcord1 < max_x:
    x_cord = list(x_cord)
    x_cord.append(xcord1)
    x_cord = tuple(x_cord)
    xcord1 += .1
    graph.append((connect1,connect2))
    connect1 +=1
    connect2 +=1

def formula(a):
    transformations = "(-x)**.5"
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
    elif (y.real) ==0:
        z = y.imag
        print (z)
        point = (number, 0, z)
        print (point)
        points.append(point)
        print (points)
    else:
        z = y.imag
        print (z)
        point = (number, y.real, z)
        print (point)
        points.append(point)
        print (points)
def Graph():
    try:
        for edge in graph:
            for point in edge:
                glVertex3fv(points[point])
    except:
        pass

def Cube():
    try:
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
    except:
        pass
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
                    glRotatef(1, 0, 90, 0)
                if event.key == pygame.K_d:
                    glRotatef(1, 0, -90, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glBegin(GL_LINES)
        Cube()
        Graph()
        glEnd()
        pygame.display.flip()
        pygame.time.wait(1)
main()
