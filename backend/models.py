from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    def to_dict(self): return {"id": self.id, "name": self.name}

class Challenge(db.Model):
    __tablename__ = "challenges"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(20))
    status = db.Column(db.String(20), default="incomplete")
    def to_dict(self): return {"id": self.id, "title": self.title, "date": self.date, "status": self.status}

class Log(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    challenge_id = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String(30), nullable=False)
    def to_dict(self): return {"id": self.id, "challenge_id": self.challenge_id, "progress": self.progress, "created_at": self.created_at}
