from sqlalchemy import Table, Column, Integer, String, DateTime, BigInteger, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from app.models.settings.metadata import metadata

Request_logs = Table(
    "request_logs",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("timestamp", DateTime(timezone=True), nullable=False),
    Column("http_method", String, nullable=False),
    Column("headers", JSONB, nullable=False),
    Column("service", String(100), nullable=False),
    Column("endpoint", String(100), nullable=False),
    Column("request_body", JSONB, nullable=True),
    Column("response_body", JSONB, nullable=True),
    Column("response_time_ms", Integer, nullable=False),
    Column("status_code", Integer, nullable=False),
    Column("user_id", UUID(as_uuid=True), nullable=True),
    Column("request_id", UUID(as_uuid=True), nullable=False),
    Column("client_ip", String(45), nullable=True),
    Column("error_message", JSONB, nullable=True),
    Column("classification", JSONB, nullable=True)
)
