import pytest

from src.category import Category
from src.iterator import CategoryIterator
from src.product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def sample_category(sample_product):
    """Фикстура для создания тестовой категории."""
    Category.category_count = 0
    Category.product_count = 0

    return Category(
        name="Смартфоны",
        description="Электронные устройства для связи",
        products=[sample_product],
    )


def test_product_init(sample_product):
    """Тест корректности инициализации объекта класса Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_str(sample_product):
    """Тест строкового отображения продукта (__str__)."""
    assert (
        str(sample_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_category_str(sample_category):
    """Тест строкового отображения категории (__str__)."""
    assert str(sample_category) == "Смартфоны, количество продуктов: 5 шт."


def test_product_add(sample_product):
    """Тест сложения двух продуктов (__add__)."""
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    # (180000 * 5) + (210000 * 8) = 900000 + 1680000 = 2580000
    assert sample_product + product2 == 2580000.0


def test_category_init(sample_category):
    """Тест корректности инициализации объекта класса Category и работы геттера products."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Электронные устройства для связи"
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert sample_category.products == expected_str


def test_category_iterator():
    """Тест работы класса-итератора CategoryIterator в цикле."""
    p1 = Product("Товар 1", "Описание 1", 100.0, 1)
    p2 = Product("Товар 2", "Описание 2", 200.0, 2)
    cat = Category("Категория", "Описание", [p1, p2])

    iterator = CategoryIterator(cat)
    iterated_products = []

    for product in iterator:
        iterated_products.append(product)

    assert len(iterated_products) == 2
    assert iterated_products[0].name == "Товар 1"
    assert iterated_products[1].name == "Товар 2"
