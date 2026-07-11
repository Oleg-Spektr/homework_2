from src.category import Category


class CategoryIterator:
    """Класс для итерации по продуктам конкретной категории."""

    def __init__(self, category: Category) -> None:
        # Забираем список продуктов из категории через созданный метод
        self.products = category.get_products_list()
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        # Метод __iter__ должен возвращать сам объект-итератор
        self.index = 0
        return self

    def __next__(self):
        # Метод __next__ возвращает следующий элемент или бросает StopIteration
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
