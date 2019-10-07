from app.dao import daoPool

db = daoPool.sqlDAO

class Numberplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CamID = db.Column(db.Integer, nullable=False)
    Timestamp = db.Column(db.String(120), nullable=True)
    Licplates = db.Column(db.String(120), nullable=True)

    def __init__(self, CamID, Timestamp, Licplates):
            self.CamID = CamID
            self.Timestamp = Timestamp
            self.Licplates = Licplates

    def __repr__(self):
        return '<Numberplate %r>' % self.CamID



