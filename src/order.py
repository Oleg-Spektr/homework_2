from src.base_group import BaseGroup
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseGroup):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int) -> None:
        try:
            if quantity == 0:
                raise ZeroQuantityError("Нельзя создать заказ с нулевым количеством товара")
        except ZeroQuantityError as e:
            print(f"Возникла ошибка при создании заказа: {e}")
            raise e
        else:
            # Для базового класса генерируем имя и описание на основе товара
            super().__init__(
                name=f"Заказ товара: {product.name}", description=f"Покупка {quantity} шт. товара {product.name}"
            )
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
            print("Товар добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итоговая стоимость: {self.total_price} руб."
