from db import db

class BlocklistModel(db.Model):
    __tablename__ = 'blocklist'

    jti = db.Column(db.String(500), primary_key=True)