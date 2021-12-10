import random;

DEF_NAME_LIST = [
"Imperador",
"Tarzan",
"Logan",
"Alice",
"Ana",
"Rina",
"Dudu",
"Totó",
"XXX",
"Cherosin",
"Hertin"
];

def pick_random_name_list():
	return DEF_NAME_LIST[random.randint(0, len(DEF_NAME_LIST) - 1)];

def update_data_vertex(entity, data):
	if data["rect"][0] != entity.last_pos_x:
		data["rect"][0] = entity.last_pos_x;

	if data["rect"][1] != entity.last_pos_y:
		data["rect"][1] = entity.last_pos_y;

	if data["rect"][2] != entity.rect.w:
		data["rect"][2] = entity.rect.w;

	if data["rect"][3] != entity.rect.h:
		data["rect"][3] = entity.rect.h;

	if data["mode"] != entity.mode:
		data["mode"] = entity.mode;

	return data;

class Account:
	def __init__(self, name, uuid):
		self.name = name;
		self.uuid = uuid;
