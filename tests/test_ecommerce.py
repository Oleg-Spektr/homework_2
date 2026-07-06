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
    # Перед каждым тестом сбрасываем счетчики класса, чтобы они не копились
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
    """Тест корректности инициализации объекта класса Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Электронные устройства для связи"
    assert len(sample_category.products) == 1


def test_category_and_product_count():
    """Тест корректного подсчета количества категорий и продуктов."""
    # Сбрасываем глобальные счетчики класса перед изолированной проверкой
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Описание 1", 100.0, 1)
    p2 = Product("Товар 2", "Описание 2", 200.0, 2)
    p3 = Product("Товар 3", "Описание 3", 300.0, 3)

    c1 = Category("Категория 1", "Описание кат 1", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2

    c2 = Category("Категория 2", "Описание кат 2", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3
