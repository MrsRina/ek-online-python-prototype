import pygame, sys;

pygame.mixer.quit();
pygame.init();

win = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF);

pygame.display.set_caption("Test");

sbr = [];
i = 0;

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();

			break;
	win.fill((0, 0, 0));

	for v in range(0, 5000):
		sbr.append(win.fill([20, 20, 60, 60], [255, 255, 255, 255]));

	if i >= 100:
		for surfaces in sbr:
			surfaces

		i

	i += 1

	print(i, len(sbr));


	pygame.display.flip();