from fastapi import Request, status
from fastapi.responses import JSONResponse


def resource_not_found_handler(_: Request, exception: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error_message": str(exception)
        }
    )
