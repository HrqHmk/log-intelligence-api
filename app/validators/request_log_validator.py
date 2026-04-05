from datetime import datetime
from uuid import UUID
from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field

class RequestLogInput(BaseModel):
    timestamp: datetime = Field(..., example="2024-06-01T12:00:00Z") 
    http_method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"] = Field(
        ..., example="GET"
    )

    headers: Dict[str, Any] = Field(
        ...,
        example={
            "Content-Type": "application/json",
            "Authorization": "Bearer token"
        }
    )

    service: str = Field(..., example="user-service")
    endpoint: str = Field(..., example="/api/v1/users")

    request_body: Optional[Dict[str, Any]] = Field(
        None,
        example={
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    )

    response_body: Optional[Dict[str, Any]] = Field(
        None,
        example={
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    )

    response_time_ms: int = Field(..., example=150)
    status_code: int = Field(..., example=200)

    user_id: Optional[UUID] = Field(
        None,
        example="123e4567-e89b-12d3-a456-426614174000"
    )

    request_id: UUID = Field(
        ...,
        example="123e4567-e89b-12d3-a456-426614174001"
    )

    client_ip: Optional[str] = Field(
        None,
        example="192.168.1.1"
    )

    error_message: Optional[Dict[str, Any]] = Field(
        None,
        example={
            "error": "User not found",
            "code": "USER_NOT_FOUND"
        }
    )
