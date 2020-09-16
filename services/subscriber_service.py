from flask import request, jsonify


class SubscriberService:

	def __init__(self, db):
		self.__db = db

	def subscribe_topic(self, topic):
		url = request.get_json().get("url")

		if url:
			topics = self.__db.get_topics()
			events = self.__db.get_events()
			if topic in topics.keys():
				topics[topic].append(url)
			else:
				subs = [url]
				topics[topic] = subs
				events[topic] = []

			self.__db.save_topics(topics)
			self.__db.save_events(events)

			return jsonify({"msg": url + " is subscribe to topic " + topic}), 200

		else:
			return jsonify({"error": "request body is invalid, plz provide url"}), 400
