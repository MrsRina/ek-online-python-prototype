import OpenGL;
from OpenGL.GLUT import *;
from OpenGL.GL import *;

w = 800;
h = 600;

class Player:
	def __init__(self, name):
		self.x = 0;
		self.y = 0;
		self.w = 50;
		self.h = 50;
		self.name = name;

		self.vertex_list = None;
		self.refreshed = False;

	def refresh(self):
		if self.refreshed:
			return;

		self.vertex_list = glGenLists(1);

		glNewList(self.vertex_list, GL_COMPILE);

		glBegin(GL_QUADS);

		glVertex(self.x, self.y);
		glVertex(self.x, self.y + self.h);
		glVertex(self.x + self.w, self.y + self.h);
		glVertex(self.x + self.w, self.y);

		glEnd();

		glEndList();

		self.refreshed = True;

	def on_render(self):

		#glBegin(GL_QUADS);

		#glVertex(self.x, self.y);
		#glVertex(self.x, self.y + self.h);
		#glVertex(self.x + self.w, self.y + self.h);
		#glVertex(self.x + self.w, self.y);

		#glEnd();
		#glPushMatrix();
		glCallList(self.vertex_list);
		#glPopMatrix();

import time;

player = Player("ronaldo");

class Data:
	fps = 0;
	c = 0;
	l = time.perf_counter();
	k = 0;

def update():
	Data.c += 1
	Data.l = Data.k;
	Data.k = time.perf_counter();

	if round(Data.k) > round(Data.l):
		Data.fps = Data.c;
		Data.c = 0;

	print(str(Data.fps),str(player.x));

def ever():
	update();

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glClearColor(0.5, 0.5, 0.5, 0.9);

	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);

	glLoadIdentity();
	glOrtho(0, w, h, 0, 0, 1);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	player.refresh();
	for i in range(200):
		player.on_render();

	glutSwapBuffers();

def keyboard(a, b, c):
	if a == b's':
		player.x += 1;
		player.refreshed = False;

		player.refresh();

glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(w, h);
win = glutCreateWindow("Hello");

glutDisplayFunc(ever);
glutIdleFunc(ever);
glutKeyboardFunc(keyboard);
glutMainLoop();