from src.base_group import BaseGroup
from src.product import Product


class Order(BaseGroup):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int) -> None:
        # Для базового класса генерируем имя и описание на основе товара
        super().__init__(
            name=f"Заказ товара: {product.name}", description=f"Покупка {quantity} шт. товара {product.name}"
        )
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итоговая стоимость: {self.total_price} руб."
