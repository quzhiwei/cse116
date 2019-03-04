from pymongo import MongoClient

class mongo(object):

	def __init__(self):
		self.dbname = "gameTest"
		self._conn = None
		self._connect()
		self.db = self._conn[self.dbname]

	def _connect(self):
		try:
			conn_str = "mongodb://localhost:27017/"
			self._conn = MongoClient(conn_str)
		except:
			print("Mongodb connection error!")

	def get_collection(self, collection):
		try:
			handler =self.db[collection]
			return handler
		except:
			print('Error: cannot fetch collection!')

	def insert_data(self, collection, data):
		try:
			col = self.db[collection]
			col.insert(data)
			print("Insertion complete.")
		except:
			print("Insertion error!")

	def delete_data(self, collection, query):
		try:
			col = self.db[collection]
			col.delete_one(query)
		except:
			print('Deletion error!')

	def clear_data(self, collection):
		col = self.db[collection]
		try:
			col.remove()
			print("Collection cleared!")
		except:
			print("Operation failed.")

	def clear_collection(self, collection):
		col =self.db[collection]
		try:
			col.drop()
			print("Collection dropped!")
		except:
			print("Operation failed.")

	def close(self):
		self._conn.close()
		print('Mongodb database connection closed.')