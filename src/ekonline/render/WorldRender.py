from ekonline.util.ObjectUtil import update_data_vertex;
from ekonline.util.DebugUtil import log;
from ekonline.core import SurfaceBufferRender;

import pygame;

class World:
	def __init__(self, surface):
		self.data_texture = {};
		self.data_vertex = {};

		self.surface = surface;

	def update_render(self, entity, _type, camera):
		#if not camera.contains_entity(entity):
		#	if self.data_vertex.__contains__(entity.id):
		#		del self.data_vertex[entity.id];

		#	return;

		if self.data_vertex.__contains__(entity.id):
			self.data_vertex[entity.id] = update_data_vertex(entity, self.data_vertex[entity.id]);
		else:
			self.data_vertex[entity.id] = {"type": _type, "mode": "notexture", "color": [255, 255, 255, 255], "rect": [entity.last_pos_x, entity.last_pos_y, entity.rect.w, entity.rect.h]};

	def on_render(self, cx, cy, partial_ticks):
		for v in self.data_vertex:
			k = self.data_vertex[v];

			if "cplayer" in k["type"] or "splayer" in k["type"]:
				if k["mode"] == "notexture":
					r = k["rect"];

					if not SurfaceBufferRender.contains("entity:id:" + str(v)):
						self.surface.fill(k["color"], [r[0] - cx, r[1] - cy, r[2], r[3]]);

						#log("SBR", "Buffer update for entity-tagged as " + "entity:id:" + str(v));
						#SurfaceBufferRender.add("entity:id:" + str(v));