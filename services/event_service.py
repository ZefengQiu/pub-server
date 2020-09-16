from flask import jsonify


class EventService:

	def __init__(self, events):
		self.__events = events

	def get_all_events(self):
		return jsonify(self.__events), 200
