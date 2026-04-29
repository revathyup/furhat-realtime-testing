from __future__ import annotations

from unittest.mock import Mock, patch

import pytest

from src.api_client import JsonPlaceholderClient


@pytest.fixture()
def client() -> JsonPlaceholderClient:
    return JsonPlaceholderClient()


@patch("src.api_client.requests.get")
def test_get_post_success(mock_get: Mock, client: JsonPlaceholderClient) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "title": "hello"}

    result = client.get_post(1)

    assert result.status_code == 200
    assert result.payload["id"] == 1
    assert "title" in result.payload


@patch("src.api_client.requests.post")
def test_create_post_success(mock_post: Mock, client: JsonPlaceholderClient) -> None:
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {
        "id": 101,
        "title": "furhat test",
        "body": "robot interaction scenario",
        "userId": 7,
    }

    result = client.create_post("furhat test", "robot interaction scenario", 7)

    assert result.status_code == 201
    assert result.payload["id"] == 101
    assert result.payload["userId"] == 7


@patch("src.api_client.requests.get")
@pytest.mark.parametrize("status_code", [400, 404, 500])
def test_get_post_negative_status_codes(
    mock_get: Mock, client: JsonPlaceholderClient, status_code: int
) -> None:
    mock_get.return_value.status_code = status_code
    mock_get.return_value.json.return_value = {"error": "bad request"}

    result = client.get_post(999)

    assert result.status_code == status_code
