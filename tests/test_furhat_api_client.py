from __future__ import annotations

import os
from unittest.mock import Mock, patch

import pytest

from src.furhat_api_client import FurhatApiClient


@pytest.fixture()
def client() -> FurhatApiClient:
    return FurhatApiClient(
        ws_url="ws://192.168.1.108:9000/v1/events",
        api_key="LEO",
    )


@patch("src.furhat_api_client.create_connection")
def test_speak_text_success(mock_create_connection: Mock, client: FurhatApiClient) -> None:
    mock_ws = Mock()
    mock_ws.recv.return_value = '{"type":"response.speak.done","success":true}'
    mock_create_connection.return_value = mock_ws

    result = client.speak_text("hello")

    assert result.event_type == "response.speak.done"
    assert result.payload["success"] is True
    assert mock_ws.send.call_count == 2


@patch("src.furhat_api_client.create_connection")
def test_speak_text_non_json_response(
    mock_create_connection: Mock, client: FurhatApiClient
) -> None:
    mock_ws = Mock()
    mock_ws.recv.return_value = "ACK"
    mock_create_connection.return_value = mock_ws

    result = client.speak_text("hello")

    assert result.event_type == "unknown"
    assert "raw_text" in result.payload


def test_live_furhat_smoke() -> None:
    """Optional live websocket test: runs only when env vars are provided."""
    ws_url = os.getenv("FURHAT_WS_URL")
    api_key = os.getenv("FURHAT_API_KEY")

    if not ws_url or not api_key:
        pytest.skip("Set FURHAT_WS_URL and FURHAT_API_KEY to run live Furhat test.")

    live_client = FurhatApiClient(ws_url=ws_url, api_key=api_key)
    result = live_client.speak_text("hello from automated test")

    assert result.event_type != ""
