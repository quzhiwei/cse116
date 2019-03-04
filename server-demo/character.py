class character(object):
	#health = 100
	#location =

	def __init__(self, initLoca):
		self.health = 100

	def isHealthEmpty(self):
		if self.health < 0:
			character.destroyCharacter()

	def destroyCharacter(self):
		self.health = 0

	def generateRandomLoca(self):
		return

	def attack(self, rival):
		return