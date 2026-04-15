# pylint:disable = W0212
# pylint:disable = E1102
from typing import Optional
from sqlalchemy import insert, select, func, case
from app.models.settings.database_connection_handler import DbConnectionHandler
from app.models.entities.request_logs import Request_logs

class RequestLogsRepository:
    def __init__(self, db_handler_factory: DbConnectionHandler):
        self.db_handler_factory = db_handler_factory

    async def insert_request_logs(self, request_logs_infos: dict) -> None:
        async with self.db_handler_factory() as db:
            query = insert(Request_logs).values(**request_logs_infos)
            await db.session.execute(query)

    async def get_average_metrics_latency_request_logs(self, endpoint: str | None) -> list[dict]:
        async with self.db_handler_factory() as db:
            if endpoint is None:
                query = (
                    select(
                        Request_logs.c.endpoint,
                        func.avg(Request_logs.c.response_time_ms).label("avg_latency")
                    )
                    .group_by(Request_logs.c.endpoint)
                )
                result = await db.session.execute(query)
                rows = result.all()
                return [
                    {
                        "endpoint": row.endpoint,
                        "average_latency_ms": float(row.avg_latency)
                    }
                    for row in rows
                ]

            query = (
                select(func.avg(Request_logs.c.response_time_ms).label("avg_latency"))
                .where(Request_logs.c.endpoint == endpoint)
            )
            result = await db.session.execute(query)
            avg_latency = result.scalar()
            return [{
                "average_latency_ms": float(avg_latency) if avg_latency is not None else None
            }]

    async def get_error_rate_service_request_logs(self, service:Optional[str] = None) -> list[dict]:
        async with self.db_handler_factory() as db:
            error_case = case(
                (Request_logs.c.status_code >= 500, 1),
                else_=0
            )

            query = (
                select(
                    Request_logs.c.service,
                    func.avg(error_case).label("error_rate")
                )
                .group_by(Request_logs.c.service)
            )

            if service:
                query = query.where(Request_logs.c.service == service)

            result = await db.session.execute(query)
            rows = result.all()
            return [
                {
                    "service": row.service,
                    "error_rate": float(row.error_rate)
                }
                for row in rows
            ]

    async def get_p95_latency_service_request_logs(self, service: str) -> list[dict]:
        async with self.db_handler_factory() as db:
            query = (
                select(
                    Request_logs.c.service,
                    func.percentile_cont(0.95)
                    .within_group(Request_logs.c.response_time_ms.asc()).label("p95_latency_ms")
                )
                .where(Request_logs.c.service == service)
                .group_by(Request_logs.c.service)
            )
            result = await db.session.execute(query)
            rows = result.all()
            return [
                {
                    "service": row.service,
                    "p95_latency_ms": round(float(row.p95_latency_ms), 2)
                    if row.p95_latency_ms is not None
                    else None
                }
                for row in rows
            ]
