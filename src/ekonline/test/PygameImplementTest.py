import pygame, sys;

pygame.mixer.quit();

win = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF);

pygame.display.set_caption("Test");

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();

			break;

	pygame.display.flip();