class ZeroQuantityError(ValueError):
    """Исключение для обработки событий, когда товар имеет нулевое количество."""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        self.message = message
        super().__init__(self.message)
