import pytest
from advance_functions import (
    calculate_cart_total,
    word_count,
    generate_password,
    analyze_temperatures,
    add_contact,
    find_contact,
    delete_contact
)

# 1. Test shopping cart
def test_calculate_cart_total():
    cart = [
        {"name": "Shirt", "price": 20.0, "quantity": 2},
        {"name": "Pants", "price": 40.0, "quantity": 1}
    ]
    assert calculate_cart_total(cart) == pytest.approx(96.8, 0.1)

# 2. Test word count
def test_word_count():
    text = "Hola hola mundo! Mundo..."
    result = word_count(text)
    assert result == {"hola": 2, "mundo": 2}

# 3. Test password generator
def test_generate_password():
    password = generate_password(12)
    assert isinstance(password, str)
    assert len(password) == 12

# 4. Test temperature analyzer
def test_analyze_temperatures():
    temps = [20, 25, 22, 18, 30]
    avg, max_t, min_t = analyze_temperatures(temps)
    assert avg == pytest.approx(23.0, 0.1)
    assert max_t == 30
    assert min_t == 18

# 5. Test contact book
def test_contact_book():
    book = {}
    book = add_contact(book, "Ana", "123")
    assert find_contact(book, "Ana") == "123"
    book = delete_contact(book, "Ana")
    assert find_contact(book, "Ana") == "No encontrado"
