from main.plugins.extensions import db


class TODO(db.Model):
    __tablename__ = 'todos_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(50), nullable=False)

    def __init__(self, id, details):
        self.id = id
        self.details = details

    def __repr__(self):
        return '<TODO (%s, %s)>' % (self.id, self.details)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
