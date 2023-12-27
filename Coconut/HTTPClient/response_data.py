class ResponseData:
    def __init__(self, text: str, status: int) -> None:
        self.response_data: str = text
        self.status: int = status

    def __str__(self) -> str:
        return f"status_code : {self.status}\nresponse_data : {self.response_data}"
