from fastapi import HTTPException

# Custom HTTP exceptions
class NotFoundError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=404, detail=message)

# Internal Server Error
class InternalServerError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=message)
