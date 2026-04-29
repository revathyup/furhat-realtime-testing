from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter


@dataclass
class ConversationResponse:
    intent: str
    message: str
    status: str
    latency_ms: int


class FurhatConversationEngine:
    """Local Furhat-style simulator for conversation system testing."""

    def respond(self, user_text: str, interrupted: bool = False) -> ConversationResponse:
        start = perf_counter()
        normalized = user_text.strip().lower()

        if interrupted:
            response = ConversationResponse(
                intent="recovery",
                message="No problem, let's continue when you are ready.",
                status="RECOVERED",
                latency_ms=0,
            )
        elif any(word in normalized for word in ("hello", "hi", "hey")):
            response = ConversationResponse(
                intent="greeting",
                message="Hello! I am Furhat. How can I help you today?",
                status="OK",
                latency_ms=0,
            )
        elif "price" in normalized or "cost" in normalized:
            response = ConversationResponse(
                intent="faq_pricing",
                message="The current plan starts from 49 SEK per month.",
                status="OK",
                latency_ms=0,
            )
        else:
            response = ConversationResponse(
                intent="fallback",
                message="I am not sure I understood. Could you rephrase?",
                status="FALLBACK",
                latency_ms=0,
            )

        response.latency_ms = max(1, int((perf_counter() - start) * 1000))
        return response
