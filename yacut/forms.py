from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp
from .constants import (
    DESCRIPTION_URL,
    MISSING_DATA,
    ERROR_URL,
    SHORT_DESCRIPTION,
    ERROR_LEN,
    PATTERN_SHORT_URL,
    SHORT_URL_ERROR,
    CREATE,
)


class YacutForm(FlaskForm):
    original_link = URLField(
        DESCRIPTION_URL,
        validators=[
            DataRequired(message=MISSING_DATA),
            URL(require_tld=True, message=ERROR_URL),
        ],
    )
    custom_id = URLField(
        SHORT_DESCRIPTION,
        validators=[
            Length(1, 16, message=ERROR_LEN),
            Optional(),
            Regexp(PATTERN_SHORT_URL, message=SHORT_URL_ERROR),
        ],
    )
    submit = SubmitField(CREATE)
