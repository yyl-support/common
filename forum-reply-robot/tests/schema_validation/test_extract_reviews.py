from src.ForumBot.SchemaValidation import extract_reviews


def test_is_redfish_related_detects_keyword():
    assert extract_reviews.is_redfish_related("Need help", "Using Redfish API") is True
    assert extract_reviews.is_redfish_related("Need help", "No platform keyword") is False
