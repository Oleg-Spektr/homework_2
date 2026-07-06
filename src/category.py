from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description

        # Делаем список товаров приватным атрибутом
        self.__products = []

        # Заполняем список через метод add_product, чтобы инкапсуляция работала и при инициализации
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список товаров категории."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в формате строк."""
        product_strings = []
        for product in self.__products:
            product_strings.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(product_strings)
