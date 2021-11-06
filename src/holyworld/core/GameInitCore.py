print("HolyWorld main core initializing.");
print("Fixing packages path.");

import os;

arraypath = os.getcwd().split(os.sep);
path = "";

j = 0;
k = len(arraypath) - 2;

for _str in arraypath:
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

from holyworld.util.DebugUtil import log;
from holyworld import CLIENT_NAME, CLIENT_VERSION;
from holyworld.core.GameCore import HolyWorld;

import holyworld;

log(CLIENT_NAME + " started, version " + str(CLIENT_VERSION));

log("-- ");
log("Hello, how are you?");

from direct.showbase.ShowBase import ShowBase;

log(" ");
log("Creating base.");
log(" ");

holyworld.CLIENT_BASE = ShowBase();

log(" ");
log("Panda3D showbase initialized.");

game = HolyWorld(holyworld.CLIENT_BASE);
game.prepare();

holyworld.CLIENT_BASE.run();