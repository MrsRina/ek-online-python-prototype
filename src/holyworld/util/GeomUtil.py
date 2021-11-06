from panda3d.core import *;

from holyworld.util.MathUtil import normalized;

class Tessellator:
	def __init__(self, vdata, vertex, normal, color, textcoord):
		self.vdata = vdata;
		self.vertex = vertex;
		self.normal = normal;
		self.color = color;
		self.textcoord = textcoord;

	def geom(self):
		tris = GeomTriangles(Geom.UHDynamic);
		tris.addVertices(0, 1, 3);
		tris.addVertices(1, 2, 3);

		geom = Geom(self.vdata);
		geom.addPrimitive(tris);

		return geom;

	def geomNode(self):
		geomNode = GeomNode('geom');
		geomNode.addGeom(self.geom());

		return geomNode;

def createGeomQuad(x, y, z, w, h, l):
	vdata = GeomVertexData('square', GeomVertexFormat.getV3n3cpt2(), Geom.UHDynamic);
	
	vertex = GeomVertexWriter(vdata, 'vertex');
	normal = GeomVertexWriter(vdata, 'normal');
	
	color = GeomVertexWriter(vdata, 'color');
	textcoord = GeomVertexWriter(vdata, 'textcoord');

	if x != w:
		vertex.addData3(x, y, z);
		vertex.addData3(w, y, z);
		vertex.addData3(w, h, l);
		vertex.addData3(x, h, l);

		normal.addData3(normalized(2 * x - 1, 2 * y - 1, 2 * z - 1));
		normal.addData3(normalized(2 * w - 1, 2 * y - 1, 2 * z - 1));
		normal.addData3(normalized(2 * w - 1, 2 * h - 1, 2 * l - 1));
		normal.addData3(normalized(2 * x - 1, 2 * h - 1, 2 * l - 1));
	else:
		vertex.addData3(x, y, z);
		vertex.addData3(w, h, z);
		vertex.addData3(w, h, l);
		vertex.addData3(x, y, l);

		normal.addData3(normalized(2 * x - 1, 2 * y - 1, 2 * z - 1));
		normal.addData3(normalized(2 * w - 1, 2 * h - 1, 2 * z - 1));
		normal.addData3(normalized(2 * w - 1, 2 * h - 1, 2 * l - 1));
		normal.addData3(normalized(2 * x - 1, 2 * y - 1, 2 * l - 1));

	return Tessellator(vdata, vertex, normal, color, textcoord);