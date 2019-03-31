import pygame
from Models.static import *


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
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill((255, 255, 0))
		self.rect = self.image.get_rect()
		#
		# self.hit_rect = pygame.Rect(0, 0, 35, 35)
		# self.hit_rect.center = self.rect.center
		self.x = x
		self.y = y
		self.health = 100

	def move(self, dx=0, dy=0):
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
		self.key_pressed()
		self.rect.x = self.x * tile_size
		self.rect.y = self.y * tile_size



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


class Wall(pygame.sprite.Sprite):

	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.walls
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		# self.image = game.wall_img
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * tile_size
		self.rect.y = y * tile_size