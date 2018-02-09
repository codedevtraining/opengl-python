from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw() :
  glClearColor(0.0, 0.0, 0.0, 0.0)
  glClear(GL_COLOR_BUFFER_BIT)

  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()

  glOrtho(0,250, 0, 250, -1, 1)

  glColor3f(0.0, 1.0, 0.0)

  glBegin(GL_POINTS)
  glVertex2i(35, 150)
  glColor3f(1.0, 0.0, 0.0)
  glVertex2i(20, 100)
  glColor3f(0.0, 0.0, 1.0)
  glVertex2i(50, 100)
  glEnd()

  glFlush()

if __name__ == '__main__' :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(250, 250)
  glutInitWindowPosition(100, 100)
  glutCreateWindow("Primeiro Programa em PyOpenGL")
  glutDisplayFunc(draw)
  glutMainLoop()






