from ekonline.util.MathUtil import Rect;

class ClientPlayer(object):
	def __init__(self, account):
		self.account = account;
		self.death = False;
		self.request_spawn = False;
		self.health = 50;
		self.immortal = True;
		self.spec = False;
		self.invisible = False;
		self.walking = False;
		self.rect = Rect();
		self.rect.w = 25;
		self.rect.h = 20;
		self.last_pos_x = self.rect.x;
		self.last_pos_y = self.rect.y;
		self.id = 99;
		self.type = "cplayer";
		self.mode = "notexture";

	def pos(self, x, y):
		self.rect.x = x;
		self.rect.y = y;

	def on_update(self, dt):
		pass;

class ServerPlayer(object):
	def __init__(self, username):
		self.username = username;
		self.health = 50;
		self.invisible = False;
		self.spec = False;
		self.death = False;
		self.rect = Rect();
		self.rect.w = 50;
		self.rect.h = 50;
		self.last_pos_x = self.rect.x;
		self.last_pos_y = self.rect.y;
		self.id = 1;
		self.type = "splayer";
		self.mode = "notexture";
	
	def pos(self, x, y):
		self.rect.x = x;
		self.rect.y = y;

	def on_update(self, dt):
		pass;