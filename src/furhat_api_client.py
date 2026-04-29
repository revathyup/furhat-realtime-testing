from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any

from websocket import create_connection


@dataclass
class FurhatApiResponse:
    event_type: str
    payload: dict[str, Any]


class FurhatApiClient:
    """Client for Furhat realtime websocket API."""

    def __init__(self, ws_url: str, api_key: str) -> None:
        self.ws_url = ws_url
        self.api_key = api_key

    def speak_text(self, text: str) -> FurhatApiResponse:
        connection = create_connection(self.ws_url, timeout=10)
        try:
            auth_message = {"type": "request.auth", "key": self.api_key}
            connection.send(json.dumps(auth_message))

            speak_message = {"type": "request.speak.text", "text": text}
            connection.send(json.dumps(speak_message))

            raw_response = connection.recv()
            data = self._safe_json_load(raw_response)
            event_type = str(data.get("type", "unknown"))
            return FurhatApiResponse(event_type=event_type, payload=data)
        finally:
            connection.close()

    @staticmethod
    def _safe_json_load(raw_response: str) -> dict[str, Any]:
        try:
            data = json.loads(raw_response)
            if isinstance(data, dict):
                return data
            return {"data": data}
        except json.JSONDecodeError:
            return {"raw_text": raw_response}
