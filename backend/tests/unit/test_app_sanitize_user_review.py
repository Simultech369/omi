from datetime import datetime, timezone
from models.app import App, AppReview


def test_sanitize_user_review_falsy_returns_none():
    assert App.sanitize_user_review(None) is None
    assert App.sanitize_user_review({}) is None


def test_sanitize_user_review_valid_payload():
    payload = {
        "uid": "user-123",
        "rated_at": datetime(2026, 1, 1, tzinfo=timezone.utc),
        "score": 4.5,
        "review": "Works great",
    }
    result = App.sanitize_user_review(payload)
    assert isinstance(result, AppReview)
    assert result.score == 4.5


def test_sanitize_user_review_malformed_dict_delegates_to_deserialize_safe():
    result = App.sanitize_user_review({"bad": "data"})
    assert result is None or isinstance(result, AppReview)
