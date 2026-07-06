from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса для подсчета количества (изначально равны 0)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        # При создании новой категории увеличиваем счетчик категорий на 1
        Category.category_count += 1

        # Увеличиваем счетчик товаров на количество переданных уникальных продуктов
        Category.product_count += len(products)
