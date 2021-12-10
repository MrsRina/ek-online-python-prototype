from ekonline.util.MathUtil import interpolation, object_inside_aabb;
from ekonline.util.DebugUtil import log;

def frustum(w, h):
	pass;

class Matrix:
	def __init__(self):
		self.x = 0;
		self.y = 0;

		self.w = 0;
		self.h = 0;

		self.last_tick_x = self.x;
		self.last_tick_y = self.y;

	def contains_entity(self, entity):
		return object_inside_aabb(entity.last_pos_x - self.x, entity.last_pos_y - self.y, entity.rect.w, entity.rect.h, self.x, self.y, self.w, self.h);

	def pos(self, x, y):
		self.last_tick_x = x;
		self.last_tick_y = y;

	def on_render(self, partial_ticks):
		self.x = interpolation(self.x, self.last_tick_x, partial_ticks);
		self.y = interpolation(self.y, self.last_tick_y, partial_ticks);