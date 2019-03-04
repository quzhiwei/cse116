import pygame

screen_width = 720
screen_height = 480

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('An RPG example')

background = pygame.image.load('../gameTest/Resources/bg.jpg')


while(True):

	screen.blit(background, (0, 0))

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
