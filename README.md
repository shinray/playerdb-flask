# playerdb-flask
playerdb demo using flask

A sample microservice that serves the contents of Players.csv through a REST API.

The service should expose two REST endpoints:

* `GET /api/players` - returns the list of all players.
* `GET /api/players/{playerID}` - returns a single player by ID.

Wishlist:
* package for distribution (Docker image?)