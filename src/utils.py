import json
from pathlib import Path

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[Category]:
    """Читает JSON-файл и возвращает список объектов класса Category."""
    file_path = Path(path)

    # Проверяем, существует ли файл, чтобы избежать падения программы
    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        # 1. Сначала собираем объекты продуктов для текущей категории
        products_list = []
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data.get("name"),
                description=product_data.get("description"),
                price=float(product_data.get("price", 0)),
                quantity=int(product_data.get("quantity", 0)),
            )
            products_list.append(product)

        # 2. Создаем объект категории и передаем туда готовый список продуктов
        category = Category(
            name=category_data.get("name"),
            description=category_data.get("description"),
            products=products_list,
        )
        categories.append(category)

    return categories
