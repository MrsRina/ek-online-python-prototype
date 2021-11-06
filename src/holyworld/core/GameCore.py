from holyworld.util import GeomUtil;
from holyworld.util.DebugUtil import log;
from direct.interval.IntervalGlobal import *;

class HolyWorld:
	def __init__(self, base):
		self.base = base;

	def prepare(self):
		self.base.camera.setZ(-10);

		self.quad = GeomUtil.createGeomQuad(-1, 1, -1, 1, -1, -1);

		self.quad.color.addData4f(1.0, 1.0, 1.0, 1.0);
		self.quad.color.addData4f(1.0, 1.0, 1.0, 1.0);
		self.quad.color.addData4f(1.0, 1.0, 1.0, 1.0);
		self.quad.color.addData4f(1.0, 1.0, 1.0, 1.0);

		node = render.attachNewNode(self.quad.geomNode());
		node.setTwoSided(True);

		log("GeomNode", "Created geom node.");