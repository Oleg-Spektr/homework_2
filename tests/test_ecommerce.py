import pytest

from src.category import Category
from src.iterator import CategoryIterator
from src.product import Product, Smartphone, LawnGrass


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
    """Тест сложения двух продуктов одного типа (__add__)."""
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


def test_smartphone_init():
    """Тест инициализации класса Smartphone."""
    phone = Smartphone(
        name="iPhone 15",
        description="Флагман от Apple",
        price=100000.0,
        quantity=5,
        efficiency=4.5,
        model="15 Pro",
        memory=256,
        color="Space Gray"
    )
    assert phone.name == "iPhone 15"
    assert phone.description == "Флагман от Apple"
    assert phone.price == 100000.0
    assert phone.quantity == 5
    assert phone.efficiency == 4.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Space Gray"


def test_lawngrass_init():
    """Тест инициализации класса LawnGrass."""
    grass = LawnGrass(
        name="Изумруд",
        description="Быстрорастущая трава",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )
    assert grass.name == "Изумруд"
    assert grass.description == "Быстрорастущая трава"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Зеленый"


def test_add_different_types_raises_error():
    """Тест, что сложение продуктов разного типа вызывает TypeError."""
    phone = Smartphone("iPhone 15", "Desc", 100000.0, 2, 4.5, "15", 256, "Gray")
    grass = LawnGrass("Изумруд", "Desc", 500.0, 20, "Россия", 14, "Зеленый")

    with pytest.raises(TypeError):
        _ = phone + grass


def test_add_base_product_and_subclass_raises_error(sample_product):
    """Тест, что сложение базового Product и подкласса Smartphone вызывает TypeError."""
    phone = Smartphone("iPhone 15", "Desc", 100000.0, 2, 4.5, "15", 256, "Gray")

    with pytest.raises(TypeError):
        _ = sample_product + phone


def test_category_add_subclass_products(sample_category):
    """Тест успешного добавления подклассов (Smartphone, LawnGrass) в категорию."""
    phone = Smartphone(
        name="iPhone 15", description="Desc", price=100000.0, quantity=2,
        efficiency=4.5, model="15 Pro", memory=256, color="Gray"
    )
    grass = LawnGrass(
        name="Изумруд", description="Desc", price=500.0, quantity=20,
        country="Россия", germination_period=14, color="Зеленый"
    )

    # Добавляем наследников класса Product
    sample_category.add_product(phone)
    sample_category.add_product(grass)

    # Проверяем, что они попали в список через ваш метод get_products_list()
    products_in_cat = sample_category.get_products_list()
    assert phone in products_in_cat
    assert grass in products_in_cat


def test_category_add_invalid_type_raises_error(sample_category):
    """Тест, что попытка добавить некорректный тип данных вызывает TypeError."""
    with pytest.raises(TypeError):
        # Передаем обычную строку вместо объекта Product или его наследника
        sample_category.add_product("Просто тестовая строка")
