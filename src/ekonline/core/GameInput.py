import pygame;

class Theme:
	BACKGROUND = [0, 190, 190, 100];
	PRESSED = [255, 255, 255, 50];

	def draw(aabb, pressed):
		surface.fill(PRESSED if pressed else BACKGROUND, aabb);

class DigitalUIControllerManager:
	def __init__(self, surface):
		self.surface = surface;
		self.show = True;

		self.start_register();
		self.registry_ui("arrow", False);
		self.arrow_scale = 20;
		self.arrow_callback_pressed_up = False;
		self.arrow_callback_pressed_down = False;
		self.arrow_callback_pressed_left = False;
		self.arrow_callback_pressed_right = False;
		self.arrow_rect = [0, 0];
		self.arrow_rect_up = [0, 0];
		self.arrow_rect_down = [0, 0];
		self.arrow_rect_left = [0, 0];
		self.arrow_rect_right = [0, 0];

	def start_register(self):
		self.ui_register = {};

	def ui(self, name, state):
		self.ui_register[name] = state;

	def active(self, name, state):
		if self.ui_register.__contains__(name):
			self.ui_register[name] = state;

	def init(self):
		pass;

	def on_event(self):
		pass;

	def on_update(self, dt):
		if self.ui_register["arrow"]:
			x = arrow_rect[0];
			y = arrow_rect[1];

			self.arrow_rect_up = [x + self.arrow_scale, y];
			self.arrow_rect_down = [x + self.arrow_scale, y + (self.arrow_rect_down * 2)];
			self.arrow_rect_left = [x, y + self.arrow_scale];
			self.arrow_rect_right = [x + (self.arrow_scale * 2), y + self.arrow_scale];

	def on_render(self, partial_ticks):
		if not self.show:
			return;

		if self.ui_register["arrow"]:
			Theme.draw(self.arrow_callback_pressed_up, self.arrow_rect_up);