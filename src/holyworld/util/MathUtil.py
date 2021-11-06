from panda3d.core import LVector3;

def normalized(*args):
	vec = LVector3(*args);
	vec.normalize();

	return vec;