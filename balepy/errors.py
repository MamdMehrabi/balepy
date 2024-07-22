
class APIError(Exception):
    """
    Signal error with an API access.
    """
    error_code: int
    description: str

    def __post_init__(self):
        super().__init__(f"Error {self.error_code}: {self.description}")
