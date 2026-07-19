from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description

        # 1. Создаем строго приватный список с двойным подчеркиванием
        self.__products = []

        # 2. Наполняем его через метод add_product
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def add_product(self, product) -> None:
        """Добавляет продукт в приватный список товаров категории с валидацией типа."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Строковое отображение категории (общее количество штук на складе)."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в формате строк."""
        return "\n".join(str(product) for product in self.__products)

    def get_products_list(self) -> list[Product]:
        """Возвращает сырой список объектов продуктов (для итератора)."""
        return self.__products
