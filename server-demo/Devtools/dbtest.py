import dbconn


def insertionTest():
	op_db = dbconn.mongo()
	players = {}
	players["online_player"] = ["player_A", "player_B", "player_C"]
	print(players)
	op_db.insert_data("players", players)
	op_db.close()


def deletionTest():
	op_db = dbconn.mongo()
	flow = {"username": "collin"}
	op_db.delete_data("players", flow)
	op_db.close()

deletionTest()
