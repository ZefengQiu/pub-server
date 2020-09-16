from flask import request, jsonify
import requests
import urllib3


class PublisherService:

	def __init__(self, db):
		self.__db = db

	def publish_topic(self, topic):
		topics = self.__db.get_topics()
		events = self.__db.get_events()
		json_header = request.headers.get("Content-Type")

		if topic in topics.keys() and json_header == "application/json":
			data = request.get_json()
			content_to_sent = jsonify({"topic": topic,
										"data": data})
			sub_urls = topics[topic]

			for url in sub_urls:
				try:
					requests.post(url, content_to_sent)
					events[topic].append({"success": topic + "-url- " + url + ": message sent successfully."})

				except requests.exceptions.HTTPError as err:
					events[topic].append({"error": topic + "-url- " + url + ": error in sent request."})
					continue
				except urllib3.exceptions.NewConnectionError as er:
					events[topic].append({"error": topic + "-url- " + url + ": error in connection between publish server and subscriber."})
					continue

			return jsonify({"message": "send data to all subscribers"}), 200

		else:
			return jsonify({"error": "topic has not been subscribed yet."}), 400
