from fastapi import HTTPException
from .types.http_bad_request_error import HttpBadRequestError

def error_handler(exception: Exception)-> HTTPException:
    if isinstance(exception, HttpBadRequestError):
        # alertar um sistema de mensageria
        # log para quando ocorrer este erro
        # varios processamentos
        raise HTTPException(
            status_code=exception.status_code,
            detail=exception.message
        )

    raise HTTPException(
        status_code=500,
        detail="Erro inesperado ao processar!!"
    )
