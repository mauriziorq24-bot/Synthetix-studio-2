class TokenOccurrence:
    def __init__(self, file_path: str, line_number: int) -> None:
        self.file_path: str = file_path
        self.line_number: int = line_number