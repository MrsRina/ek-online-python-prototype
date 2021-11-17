print("EK main core initializing.");
print("Fixing packages path.");

import os;

array_path = os.getcwd().split(os.sep);
path = "";

j = 0;
k = len(array_path) - 2;

for _str in array_path:
	if j >= k:
		break;

	path = path + _str  + "/";

	j += 1;

print("New path applied: " + path);

import sys;

sys.path.insert(1, path);

print("[]");
print("[]");
print("[]");

from ekonline.util.DebugUtil import log, print_log, print_len_log;
from ekonline import CLIENT_NAME, CLIENT_VERSION;
from ekonline.core.GameCore import EKOnline;

import ekonline, sys;

log(CLIENT_NAME + " started, version " + str(CLIENT_VERSION));

log("-- ");
log("Hello, how are you?");
log("Preparing SDL.");

pygame = None;

try:
	import pygame as sdl;
	pygame = sdl;

	log("SDL found, using Pygame as base.");
except:
	log("SDL not found.");

from ekonline.core.GameGUI import GuiManager;

pygame.mixer.quit();

window = pygame.display.set_mode((480, 240), pygame.DOUBLEBUF);

pygame.display.set_caption(CLIENT_NAME + " " + str(CLIENT_VERSION));

# Init ALl classes of the game.
game = EKOnline(window);
game_gui_manager = GuiManager(window);

log("Game GUI initialized.");

# Update ALL main variables of the game.
game.gui_manager = game_gui_manager;

# Create main variables.
partial_ticks = 1;

while 1:
	for event in pygame.event.get():
		game.on_event(event);
		game_gui_manager.on_event(event);

		if event.type == pygame.MOUSEBUTTONUP:
			game.on_touch_detected(event.pos[0], event.pos[1]);
			game_gui_manager.on_touch_detected(event.pos[0], event.pos[1]);
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			game.on_touch_released(event.pos[0], event.pos[1]);
			game_gui_manager.on_touch_released(event.pos[0], event.pos[1]);

		if event.type == pygame.QUIT:
			game.on_shutdown();

			log("Game shutdown complete.");
			sys.exit();

			break;

	window.fill((0, 0, 0));

	game.on_update(partial_ticks);
	game.on_render(partial_ticks);

	pygame.display.flip();