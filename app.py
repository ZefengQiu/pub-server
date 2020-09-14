from flask import Flask
from routers.router import init_routes
from services.mock_db import MockDataBase

app = Flask(__name__)


if __name__ == "__main__":

	# Load data from mock db, in practice will choose to use dynamodb (big table database) or redis
	db = MockDataBase([], {})

	init_routes(app, db)

	app.run(debug=True, port=8000)
