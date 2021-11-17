import sdl2.ext;
import sdl2;

window = sdl2.ext.Window("SDL Test, Hello!", size = (230, 230));
window.show();

processor = sdl2.ext.TestEventProcessor();
processor.run(window);

import sys;

while 1:
	for event in sdl2.ext.get_events():
		if event.type == sdl2.SDL_QUIT:
			sys.exit();

			break;

	window.refresh();

sdl2.ext.quit();