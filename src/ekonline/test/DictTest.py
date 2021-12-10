pos = 9

w = {"mog": {pos : 2, "l-3" : 1}};

g = "ee";
g.replace("e", "");

for z in w:
	v = w[z];

	for k in v:
		print(k);

	print(v.get("l-3"));
	print(v); 