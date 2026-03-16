from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from app.models.settings.metadata import metadata

Request_logs = Table(
    "request_logs",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("timestamp", DateTime, nullable=False),
    Column("http_method", String, nullable=False),
    Column("headers", JSONB, nullable=False),
    Column("service", String, nullable=False),
    Column("endpoint", String, nullable=False),
    Column("request_body", JSONB, nullable=True),
    Column("response_body", JSONB, nullable=True),
    Column("response_time_ms", Integer, nullable=False),
    Column("status_code", Integer, nullable=False),
    Column("user_id", Integer, nullable=True),
    Column("request_id", String, nullable=False),
    Column("client_ip", String, nullable=True),
    Column("error_message", JSONB, nullable=True)
)
