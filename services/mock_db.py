
class MockDataBase:

	def __init__(self, events, topics):
		self.__events = events
		self.__topics = topics

	def get_events(self):
		return self.__events

	def get_topics(self):
		return self.__topics

	def save_topics(self, topics):
		self.__topics = topics


