from ekonline.util.DebugUtil import log;

import pygame;

class EKOnline:
	def __init__(self, window):
		self.display = window;
		self.gui_manager = None;

	def prepare(self):
		pass;

	def on_shutdown(self):
		pass;

	def on_event(self, event):
		pass;

	def on_touch_detected(self, tx, ty):
		pass;

	def on_touch_released(self, tx, ty):
		pass;

	def on_render(self, partial_ticks):
		pass;

	def on_update(self, dt):
		pass;