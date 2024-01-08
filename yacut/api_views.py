from http import HTTPStatus as status
from re import match

from flask import jsonify, request
from . import app, db
from .models import URLMap
from .utils import get_unique_short_id
from .error_handlers import InvalidAPIUsage
from .constants import (
    ID_NOT_FOUND,
    MISSING_REQUEST,
    URL_REQUIRED_FIELD,
    PATTERN_URL,
    ERROR_URL,
    PATTERN_SHORT_URL,
    SHORT_URL_ERROR,
    OCCUPIED_ID,
)


@app.route("/api/id/<string:short>/", methods=["GET"])
def yacut_redirect_api(short):
    redirect = URLMap.query.filter_by(short=short).first()
    if not redirect:
        raise InvalidAPIUsage(ID_NOT_FOUND, status.NOT_FOUND)
    return jsonify({"url": redirect.original})


@app.route("/api/id/", methods=["POST"])
def create_short_api():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage(MISSING_REQUEST)

    url = data.get("url")
    custom_id = data.get("custom_id")

    if not url:
        raise InvalidAPIUsage(URL_REQUIRED_FIELD)
    if not match(PATTERN_URL, url):
        raise InvalidAPIUsage(ERROR_URL)

    if custom_id:
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(OCCUPIED_ID.format(custom_id))
        if not match(PATTERN_SHORT_URL, custom_id):
            raise InvalidAPIUsage(SHORT_URL_ERROR)
    else:
        custom_id = get_unique_short_id()

    url_map = URLMap(original=url, short=custom_id)
    db.session.add(url_map)
    db.session.commit()

    return jsonify(url_map.to_dict()), status.CREATED
