class session(object):

	def __init__(self):
		self.online_players = []

	def add_player(self, player):
		self.online_players.append(player)

	def remove_player(self, player):
		try:
			self.online_players.remove(player)
		except:
			return "Player not found!"

	def show_all_players(self):
		return self.online_players