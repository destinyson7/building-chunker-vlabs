from exp10 import db


class answersData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answers = db.Column(db.String(120), unique=True)

    def __init__(self, answers):
        self.answers = answers

    def __repr__(self):
        return '<answersData %r>' % self.answers
