class Product:
    """Класс для представления товара."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        # Скрываем цену в приватный атрибут
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(
        cls, product_data: dict, current_products: list = None
    ) -> "Product":
        """Метод класса для создания нового товара или обновления существующего."""
        name = product_data.get("name")
        description = product_data.get("description")
        price = float(product_data.get("price", 0))
        quantity = int(product_data.get("quantity", 0))

        if current_products:
            for existing_product in current_products:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    # Используем сеттер для безопасной установки максимальной цены
                    existing_product.price = max(existing_product.price, price)
                    return existing_product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения приватной цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для безопасной установки новой цены товара с подтверждением понижения."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Если цена понижается, запрашиваем подтверждение у пользователя
        if new_price < self.__price:
            user_answer = input(
                f"Вы уверены, что хотите снизить цену товара с {self.__price} до {new_price} руб.? (y/n): "
            ).lower()
            if user_answer != "y":
                print("Действие отменено. Цена осталась прежней.")
                return

        self.__price = new_price
