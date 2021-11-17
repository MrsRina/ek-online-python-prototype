class GuiManager:
	def __init__(self, ekonline):
		self.ekonline = ekonline;
		self.current = None;
		self.gui_list = {};

	def prepare(self):
		pass;

	def open(self, gui_class):
		if self.gui_list.__contains__(type(gui_class)) and self.gui_list is not self.gui_list[type(gui_class)]:
			if self.current is not None:
				self.current.on_close();

			self.current = self.gui_list[type(gui_list)];
			self.current.on_open();

	def on_event(self, event):
		pass;

	def on_touch_detected(self, tx, ty):
		if self.current is not None:
			self.current.on_touch_detected(tx, ty);

	def on_touch_released(self, tx, ty):
		if self.current is not None:
			self.current.on_touch_released(tx, ty);

	def on_update(self, dt):
		if self.current is not None:
			self.current.on_update(dt);

	def on_render(self, partial_ticks):
		if self.current is not None:
			self.current.on_render(partial_ticks);