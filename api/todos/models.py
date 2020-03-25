from api import db

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    from_date = db.Column(db.DateTime)
    to_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

