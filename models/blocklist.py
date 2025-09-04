from db import db

# Model for database
class BlocklistModel(db.Model):
    __tablename__ = 'blocklist'

    jti = db.Column(db.String(500), primary_key=True)