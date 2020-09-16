from services.event_service import EventService
from services.publisher_service import PublisherService
from services.subscriber_service import SubscriberService


def init_routes(app, db):

	if app and db:
		sub = SubscriberService(db)
		pub = PublisherService(db)
		event_service = EventService(db.get_events())

		app.add_url_rule('/subscribe/<string:topic>', 'subscribe_topic', sub.subscribe_topic, methods=["POST"])
		app.add_url_rule('/publish/<string:topic>', 'publish_topic', pub.publish_topic, methods=["POST"])
		app.add_url_rule('/event', 'get_all_event', event_service.get_all_events, methods=["GET"])
