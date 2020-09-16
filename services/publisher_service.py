from flask import request, jsonify
import requests


class PublisherService:

	def __init__(self, db):
		self.__db = db

	def publish_topic(self, topic):
		topics = self.__db.get_topics()
		json_header = request.headers.get("Content-Type")

		if topic in topics.keys() and json_header == "application/json":
			data = request.get_json()
			content_to_sent = jsonify({"topic": topic,
										"data": data})
			sub_urls = topics[topic]

			for url in sub_urls:
				requests.post(url, content_to_sent)

			return jsonify({"message": "send data to all subscribers"}), 200

		else:
			return jsonify({"error": "topic has not been subscribed yet."}), 400
