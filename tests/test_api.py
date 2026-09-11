from api import get_github_user
import pytest


def test_get_github_user():
    user = get_github_user("octocat")

    assert user["login"] == "octocat"
    assert "public_repos" in user
    assert "followers" in user


def test_invalid_github_user():
    with pytest.raises(ValueError):
        get_github_user("this-user-definitely-does-not-exist-123456789")