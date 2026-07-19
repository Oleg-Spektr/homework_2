from abc import ABC, abstractmethod


class BaseGroup(ABC):
    """Абстрактный класс для группировки объектов (Категории, Заказы)."""

    @abstractmethod
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
