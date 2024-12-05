from app import db

class SignUp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name  = db.Column(db.String(50), nullable=False)
    email      = db.Column(db.String(120), nullable=False, unique=False)
    phone      = db.Column(db.String(20))
    company    = db.Column(db.String(100))
    job_title  = db.Column(db.String(100))
    dietary_preferences = db.Column(db.String(200))
    topics_of_interest  = db.Column(db.Text)
    comments   = db.Column(db.Text)

    def __repr__(self):
        return f'<SignUp {self.email}>'
