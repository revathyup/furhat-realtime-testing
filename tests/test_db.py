from __future__ import annotations

from src.db import (
    ResultRecord,
    avg_response_ms,
    count_failed_scenarios,
    get_connection,
    insert_result,
)


def test_insert_and_count_failed_scenarios() -> None:
    connection = get_connection()
    insert_result(
        connection,
        ResultRecord(
            scenario="user interrupts robot greeting",
            status="FAILED",
            response_ms=920,
            defect_severity="HIGH",
        ),
    )
    insert_result(
        connection,
        ResultRecord(
            scenario="normal greeting flow",
            status="PASSED",
            response_ms=380,
            defect_severity="NONE",
        ),
    )

    assert count_failed_scenarios(connection) == 1


def test_avg_response_time() -> None:
    connection = get_connection()
    insert_result(
        connection,
        ResultRecord(
            scenario="faq flow",
            status="PASSED",
            response_ms=400,
            defect_severity="NONE",
        ),
    )
    insert_result(
        connection,
        ResultRecord(
            scenario="fallback flow",
            status="PASSED",
            response_ms=600,
            defect_severity="LOW",
        ),
    )

    assert avg_response_ms(connection) == 500.0
