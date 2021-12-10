from ekonline.util.DebugUtil import log;
from ekonline.util.ObjectUtil import pick_random_name_list, Account;
from ekonline.entity.Player import ClientPlayer, ServerPlayer;
from ekonline.world.World import BigChunk;
from ekonline.render.WorldRender import World;

import pygame;

class EKOnline:
	def __init__(self, window):
		self.display = window;
		self.gui_manager = None;
		self.camera = None;
		self.world = None;
		self.world_render = None;
		self.handler = None;
		self.player = None;
		self.screen_width = 480;
		self.screen_height = 240;
		self.digital_ui_controller = None;

	def prepare(self):
		self.create_player();
		self.create_world();

	def create_player(self, username = None):
		_username = username;

		if username is None:
			_username = pick_random_name_list();
		
		self.player = ClientPlayer(Account(_username, 99898989));
		self.player.id = 999;
		self.player.pos(40, 0);

		log("Created player, uuid & id: " + self.player.account.name + " " + str(self.player.account.uuid) + " " + str(self.player.id));

	def create_world(self):
		self.world = BigChunk("dev-test-1");
		self.world.add(self.player);

		for i in range(0, 40):
			player = ServerPlayer(pick_random_name_list());
			player.id += i;
			player.pos(player.rect.x + i * player.rect.w + 20, player.rect.y);

			self.world.add(player);

		self.world_render = World(self.display);

	def on_shutdown(self):
		pass;

	def on_event(self, event):
		pass;

	def on_touch_detected(self, tx, ty):
		if self.player is not None:
			self.player.pos(self.player.rect.x + 10, self.player.rect.y);

	def on_touch_released(self, tx, ty):
		pass;

	def on_render(self, partial_ticks):
		if self.world is not None and self.world_render is not None:
			if self.player is not None:
				self.camera.pos(self.player.last_pos_x - self.screen_width / 2, self.player.last_pos_y - self.screen_height / 2);

			self.world.on_render(self.world_render, self.camera, partial_ticks);
			self.world_render.on_render(self.camera.x, self.camera.y, partial_ticks);

	def on_update(self, dt):
		self.camera.w = self.screen_width;
		self.camera.h = self.screen_height;

		if self.world is not None:
			self.world.on_update(dt);