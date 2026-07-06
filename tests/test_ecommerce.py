import pytest

from src.category import Category
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


def test_category_init(sample_category):
    """Тест корректности инициализации объекта класса Category и работы геттера products."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Электронные устройства для связи"
    # Проверяем работу нового геттера, который возвращает строку
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert sample_category.products == expected_str


def test_category_and_product_count():
    """Тест корректного подсчета количества категорий и продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Описание 1", 100.0, 1)
    p2 = Product("Товар 2", "Описание 2", 200.0, 2)
    p3 = Product("Товар 3", "Описание 3", 300.0, 3)

    Category("Категория 1", "Описание кат 1", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("Категория 2", "Описание кат 2", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_new_product_classmethod():
    """Тест создания продукта через метод класса new_product."""
    product_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
    }
    product = Product.new_product(product_data)
    assert product.name == "Iphone 15"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_new_product_merge():
    """Тест слияния одинаковых продуктов через метод класса new_product."""
    p1 = Product("Iphone 15", "512GB", 200000.0, 5)
    current_list = [p1]

    product_data = {
        "name": "Iphone 15",
        "description": "512GB",
        "price": 220000.0,
        "quantity": 3,
    }

    updated_product = Product.new_product(product_data, current_list)
    assert updated_product.quantity == 8  # 5 + 3
    assert updated_product.price == 220000.0  # Выбрана максимальная цена


def test_price_setter_validation(sample_product):
    """Тест валидации цены в сеттере (ноль или отрицательное значение)."""
    sample_product.price = 0
    assert sample_product.price == 180000.0  # Цена не должна измениться

    sample_product.price = -100
    assert sample_product.price == 180000.0  # Цена не должна измениться


def test_price_setter_decrease_confirm(sample_product, monkeypatch):
    """Тест понижения цены с подтверждением пользователя 'y'."""
    # Симулируем ввод 'y' в терминале
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 150000.0
    assert sample_product.price == 150000.0


def test_price_setter_decrease_cancel(sample_product, monkeypatch):
    """Тест отмены понижения цены, если пользователь ввел 'n'."""
    # Симулируем ввод 'n' в терминале
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 150000.0
    assert sample_product.price == 180000.0  # Цена должна остаться прежней
