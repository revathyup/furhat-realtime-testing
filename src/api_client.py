from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class ApiResult:
    status_code: int
    payload: dict[str, Any]


class JsonPlaceholderClient:
    """Tiny API client used for portfolio-ready testing practice."""

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com") -> None:
        self.base_url = base_url.rstrip("/")

    def get_post(self, post_id: int) -> ApiResult:
        response = requests.get(f"{self.base_url}/posts/{post_id}", timeout=10)
        return ApiResult(status_code=response.status_code, payload=response.json())

    def create_post(self, title: str, body: str, user_id: int) -> ApiResult:
        response = requests.post(
            f"{self.base_url}/posts",
            json={"title": title, "body": body, "userId": user_id},
            timeout=10,
        )
        return ApiResult(status_code=response.status_code, payload=response.json())
