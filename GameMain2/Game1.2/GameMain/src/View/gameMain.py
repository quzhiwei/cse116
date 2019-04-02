import pygame
from Control.controller import *
from Models.characters import *
from Models.static import *
from View.tilemap import *
import Battle.battleInterface


class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode([screen_width, screen_height])
		pygame.display.set_caption('An RPG Game')
		self.map = TiledMap('../../Resources/town.tmx')
		self.map_img = self.map.make_map()
		self.map_rect = self.map_img.get_rect()
		self.player_image = pygame.image.load("../../Resources/player.png").convert_alpha()

		self.isRunning = True

	def changemap(self,Player):
		if Player.x ==1120.00 and Player.y ==416.00:
			self.map = TiledMap('../../Resources/house1.tmx')

	def session_setup(self, set_x = -1, set_y = -1):
		self.all_sprites = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()
		self.enemy = pygame.sprite.Group()
		for tile_object in self.map.tmxdata.objects:
			if set_x != -1 & set_y != -1:
				self.player = Player(self, set_x, set_y)
			else:
				if tile_object.name == 'player':
					self.player = Player(self, tile_object.x, tile_object.y)

			if tile_object.name == 'wall':
				Obstacle(self, tile_object.x, tile_object.y,
						 tile_object.width, tile_object.height)
				wall = Obstacle
		self.camera = Camera(self.map.width, self.map.height)
		self.draw_debug = False


	def draw_grid(self):
		for x in range(0, screen_width, tile_size):
			pygame.draw.line(self.screen, (100, 100, 100), (x, 0), (x, screen_height))
		for y in range(0, screen_height, tile_size):
			pygame.draw.line(self.screen, (100, 100, 100), (0, y), (screen_width, y))

	def update_session(self):
		while self.isRunning:
			self.session_event()
			self.all_sprites.update()
			self.camera.update(self.player)

			self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
			# self.draw_grid()
			for sprite in self.all_sprites:
				self.screen.blit(sprite.image, self.camera.apply(sprite))
			pygame.display.flip()

	def session_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				# self.isRunning = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()

				#Keyboard input defined in character.Player.key_pressed()
				#This is only for testing
				if event.key == pygame.K_LEFT:
					self.player.move(dx=-32)
				if event.key == pygame.K_RIGHT:
					self.player.move(dx=32)
				if event.key == pygame.K_UP:
					self.player.move(dy=-32)
				if event.key == pygame.K_DOWN:
					self.player.move(dy=32)


				if event.key == pygame.K_e:
					battle_status = Battle.battleInterface.Battle()
					battle_status.BattleMain()


if __name__ == "__main__":
	session = Game()
	while True:
		session.session_setup()
		session.update_session()