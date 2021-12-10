from ekonline.util.DebugUtil import log;

BUFFER  = {};

def contains(tag):
	return BUFFER.__contains__(tag);

def add(tag, action = None):
	flag = BUFFER.__contains__(tag);

	if action is not None:
		if action == "update" and flag:
			del BUFFER[tag];

			flag = False;


	if not flag:
		BUFFER[tag] = bytes(0);

def debug():
	log("Len buffer: " + str(len(BUFFER)));