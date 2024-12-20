from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                "yacut_redirect", short=self.short, _external=True
            ),
        )

    def from_dict(self, data):
        setattr(self, "original", data["url"])
        setattr(self, "short", data["custom_id"])
