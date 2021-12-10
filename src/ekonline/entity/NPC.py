class Animal(object):
	def __init__(self, name):
		self.name = name;
		self.health = 50;
		self.invisible = False;
		self.spec = False;
		self.death = False;
		self.rect = Rect();
		self.last_pos_x = 0;
		self.last_pos_y = 0;
		self.last_tick_pos_x = 0;
		self.last_tick_pos_y = 0;
		self.id = 1;
		self.type = "animal";

	def on_update(self, dt):
		pass;