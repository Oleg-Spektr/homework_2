from abc import ABC, abstractmethod


class PrintMixin:
    """Миксин для логирования информации о создании объекта в консоль."""

    def __init__(self, *args, **kwargs) -> None:
        # Сначала даем отработать инициализации базовых атрибутов
        super().__init__(*args, **kwargs)
        # Распечатываем строковое представление объекта
        print(repr(self))

    def __repr__(self) -> str:
        # Динамически собираем имя класса и значения его базовых атрибутов
        # Используем hasattr, чтобы безопасно читать атрибуты во время цепочки super()
        attrs = []
        for attr in ["name", "description", "price", "quantity"]:
            if hasattr(self, attr):
                attrs.append(repr(getattr(self, attr)))

        return f"{self.__class__.__name__}({', '.join(attrs)})"


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового отображения."""
        pass


class Product(PrintMixin, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        # Вызов super() пойдет в PrintMixin, а оттуда в BaseProduct
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Сложение двух продуктов (возвращает общую стоимость их запасов)."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного и того же класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
