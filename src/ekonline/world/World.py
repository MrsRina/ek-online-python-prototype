from ekonline.util.DebugUtil import log;
from ekonline.util.MathUtil import interpolation;

class BigChunk:
	def __init__(self, name):
		self.name = name;

		self.loaded_entity_list = {};
		self.loaded_data_vertex = {};

	def add(self, entity):
		if not self.loaded_entity_list.__contains__(entity.id):
			self.loaded_entity_list[entity.id] = entity;

			log("INFO", "Added entity id: " + str(entity.id));

	def load(self):
		pass;

	def on_event(self, event):
		pass;

	def on_update(self, dt):
		for id in self.loaded_entity_list:
			entity = self.loaded_entity_list[id];
			entity.on_update(dt);

	def on_render(self, world_render, camera, partial_ticks):
		for id in self.loaded_entity_list:
			entity = self.loaded_entity_list[id];

			# Upate interpolating position;
			entity.last_pos_x = interpolation(entity.last_pos_x, entity.rect.x, partial_ticks);
			entity.last_pos_y = interpolation(entity.last_pos_y, entity.rect.y, partial_ticks);

			world_render.update_render(entity, entity.type, camera);