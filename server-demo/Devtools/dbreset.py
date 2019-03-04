import dbconn

op_db = dbconn.mongo()
op_db.clear_data("players")
op_db.clear_collection("players")
op_db.close()