import pygame
from Models.static import *
from View.tilemap import *



class Character(pygame.sprite.Sprite):

	def __init__(self, session):
		self.groups = session.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.session = session

	def is_health_empty(self):
		if self.health < 0:
			self.destroy_character()

	def destroy_character(self):
		self.health = 0

	def generate_random_location(self, init_coordinate):
		return

	def attack(self):
		return


class Player(Character):

	def __init__(self, session, x, y):
		Character.__init__(self, session)
		self.atk_damage = 15
		self.score = 0
		# for testing only
		# self.image = player_image
		self.image = session.player_image
		self.rect = self.image.get_rect()
		#
		# self.hit_rect = pygame.Rect(0, 0, 35, 35)
		# self.hit_rect.center = self.rect.center
		self.x = x
		self.y = y
		self.health = 100

	def collide_with_walls(self, dx=0, dy=0):
		for wall in self.session.walls:
			if wall.x == self.x + dx and wall.y == self.y + dy:
				return True
		return False

	def move(self, dx=0, dy=0):
		if not self.collide_with_walls(dx, dy):
			self.x += dx
			self.y += dy


	def key_pressed(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.move(dx=-1)
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.move(dx=1)
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.move(dy=-1)
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.move(dy=1)

	def update(self):
		# self.key_pressed()
		self.rect.x = self.x
		self.rect.y = self.y



class Enemy(Character):

	def __init__(self, session):
		Character.__init__(self, session)
		# for testing only
		# self.image = enemy_image
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill((255, 0, 0))
		#
		self.atk_damage = 5

	def update(self):
		return


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, session, x, y, w, h):
        self.groups = session.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = session
        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
