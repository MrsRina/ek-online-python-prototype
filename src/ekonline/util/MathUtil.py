import pygame;

def interpolation(a, b, t):
	if t <= 0.0 or t >= 1:
		return b;
	else:
		return a + (b - a) * t;

# Object One (oo); Object Two (ot);
def object_inside_aabb(oox, ooy, oow, ooh, otx, oty, otw, oth):
	return oox > otx and ooy > oty and oox + oow < otx + otw and ooy + ooh < oty + oth;

def object_inside_aabb_point(px, py, ox, oy, ow, oh):
	return px > ox and py > oy and px < ox + ow and py < oy + oh;

class Rect:
	def __init__(self):
		self.x = 0;
		self.y = 0;
		self.w = 0;
		self.h = 0;
		self.tag = "";