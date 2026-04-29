from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass
class ResultRecord:
    scenario: str
    status: str
    response_ms: int
    defect_severity: str


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario TEXT NOT NULL,
    status TEXT NOT NULL,
    response_ms INTEGER NOT NULL,
    defect_severity TEXT NOT NULL
);
"""


def get_connection(db_path: str = ":memory:") -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    connection.execute(SCHEMA_SQL)
    return connection


def insert_result(connection: sqlite3.Connection, record: ResultRecord) -> None:
    connection.execute(
        """
        INSERT INTO test_results (scenario, status, response_ms, defect_severity)
        VALUES (?, ?, ?, ?)
        """,
        (record.scenario, record.status, record.response_ms, record.defect_severity),
    )
    connection.commit()


def count_failed_scenarios(connection: sqlite3.Connection) -> int:
    query = "SELECT COUNT(*) FROM test_results WHERE status = 'FAILED'"
    (count,) = connection.execute(query).fetchone()
    return int(count)


def avg_response_ms(connection: sqlite3.Connection) -> float:
    query = "SELECT AVG(response_ms) FROM test_results"
    (avg,) = connection.execute(query).fetchone()
    return float(avg or 0.0)
