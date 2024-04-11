from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(20), unique=True)
    birthYear = db.Column(db.Integer)
    birthMonth = db.Column(db.Integer)
    birthDay = db.Column(db.Integer)
    birthCity = db.Column(db.String(100))
    birthCountry = db.Column(db.String(100))
    birthState = db.Column(db.String(100))
    deathYear = db.Column(db.Integer)
    deathMonth = db.Column(db.Integer)
    deathDay = db.Column(db.Integer)
    deathCountry = db.Column(db.String(100))
    deathState = db.Column(db.String(100))
    deathCity = db.Column(db.String(100))
    nameFirst = db.Column(db.String(100))
    nameLast = db.Column(db.String(100))
    nameGiven = db.Column(db.String(200))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    bats = db.Column(db.String(1))
    throws = db.Column(db.String(1))
    debut = db.Column(db.String(20))
    bbrefID = db.Column(db.String(20))
    finalGame = db.Column(db.String(20))
    retroID = db.Column(db.String(20))

    def as_dict(self):
        try:
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        except Exception as e:
            print(f"Error serializing player: {e}")
            return {}

    @staticmethod
    def get_players():
        return Player.query.all()
    
    @staticmethod
    def get_by_playerId(playerId):
        return Player.query.filter_by(playerID=playerId).first()
