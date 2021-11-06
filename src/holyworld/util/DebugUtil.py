UVU_NONE = "MAIN";

DIFFERENCE_ONE = "[";
DIFFERENCE_TWO = "]";

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