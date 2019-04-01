import pygame

def key_pressed(player):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] or keys[pygame.K_a]:
		player.move(dx=-1)
	if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
		player.move(dx=1)
	if keys[pygame.K_UP] or keys[pygame.K_w]:
		player.move(dy=-1)
	if keys[pygame.K_DOWN] or keys[pygame.K_s]:
		player.move(dy=1)
	#Obstacleif keys[pygame.K_SPACE]:
		#player.interact