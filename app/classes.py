class Databases:
	'''Stores numerous databases (message database, user database, etc.'''
	def __init__(self):
		self.databases = {}

	def add_database(self, database):
		'''Adds a new database'''
		self.databases[database.name] = database

	def __getitem__(self, item):
		return self.database.get(item)

class Database:
	'''Stores entries of tuples (all of them have to be in the same format :)'''
	def __init__(self, name):
		self.name = name
		self.database = []
		self.size = 0
		self.entry_num = -1

	def add_entry(self, entry: tuple):
		'''Adds a new entry'''
		#if the database is empty, set the database scheme
		if self.size > 0:
			self.entry_num = len(entry)
		else:
			if self.entry_num != len(entry):
				raise TypeError("The tuple that was entered did not match the schema of this database")
		self.database.append(entry)
		self.size += 1

	def get_entry_by_index(self, index):
		'''Get the entry by index'''
		return self.database[index]

	def get_entries_by_indices(self, index1, index2):
		'''Gets entries in [index1, index2)'''
		return self.database[index1:index2]

	def get_last_n_entries(self, n):
		'''Gets the last n entries.'''
		return self.database[max(0, self.size-100):]

	def get_size(self):
		return self.size
