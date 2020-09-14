from flask import request, jsonify


class SubscriberService:

	def __init__(self, db):
		self.__db = db

	def subscribe_topic(self, topic):
		url = request.get_json().get("url")

		if url:
			topics = self.__db.get_topics()
			if topic in topics.keys():
				topics[topic].append(url)
			else:
				subs = [url]
				topics[topic] = subs

			self.__db.save_topics(topics)

			return jsonify({"msg": "url has been added"}), 200
		else:
			return jsonify({"error": "request body is invalid, plz provide url"}), 400
