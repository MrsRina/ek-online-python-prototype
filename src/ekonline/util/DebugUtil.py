UVU_NONE = "MAIN";

DIFFERENCE_ONE = "[";
DIFFERENCE_TWO = "]";

global CACHE_LOG;
global WRITE_LOG;

CACHE_LOG = "";
WRITE_LOG = False;

def log(uuv, uvu = None):
	_log = None;

	if uvu is None:
		_log = DIFFERENCE_ONE + UVU_NONE + DIFFERENCE_TWO + " " + uuv;
	else:
		_log = DIFFERENCE_ONE + uuv + DIFFERENCE_TWO + " " + uvu;

	print(_log);

	if WRITE_LOG:
		CACHE_LOG = CACHE_LOG + "\n";

def print_log():
	print(CACHE_LOG);

def print_len_log():
	print(len(CACHE_LOG))