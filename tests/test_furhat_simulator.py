from __future__ import annotations

import pytest

from src.furhat_simulator import FurhatConversationEngine


@pytest.fixture()
def engine() -> FurhatConversationEngine:
    return FurhatConversationEngine()


def test_greeting_intent(engine: FurhatConversationEngine) -> None:
    result = engine.respond("Hello Furhat")
    assert result.intent == "greeting"
    assert result.status == "OK"


def test_interruption_recovery(engine: FurhatConversationEngine) -> None:
    result = engine.respond("continue", interrupted=True)
    assert result.intent == "recovery"
    assert result.status == "RECOVERED"


def test_fallback_for_unknown_input(engine: FurhatConversationEngine) -> None:
    result = engine.respond("blabla random phrase")
    assert result.intent == "fallback"
    assert result.status == "FALLBACK"


def test_response_latency_under_threshold(engine: FurhatConversationEngine) -> None:
    result = engine.respond("what is the price?")
    assert result.intent == "faq_pricing"
    assert result.latency_ms < 200
