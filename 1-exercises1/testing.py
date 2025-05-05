import pytest
from datetime import date

from functions import (
    calculate_tip,
    meters_to_kilometers,
    create_email,
    final_price,
    validate_login,
    validate_phone,
    format_name,
    generate_username,
    calculate_age,
    student_average
)

# 1. Test calculate_tip
def test_calculate_tip():
    assert calculate_tip(100, 15) == 15.0

# 2. Test meters_to_kilometers
def test_meters_to_kilometers():
    assert meters_to_kilometers(1500) == 1.5

# 3. Test create_email
def test_create_email():
    assert create_email("Lucia", "Gomez", "empresa.com") == "lucia.gomez@empresa.com"

# 4. Test final_price
def test_final_price():
    assert final_price(100, 0.10) == pytest.approx(110.0)
    assert final_price(100) == 121.0

# 5. Test validate_login
def test_validate_login_success(capsys):
    assert validate_login("admin", "1234") is True
    captured = capsys.readouterr()
    assert "Inicio de sesión exitoso" in captured.out

def test_validate_login_fail(capsys):
    assert validate_login("user", "wrong") is False
    captured = capsys.readouterr()
    assert "Credenciales incorrectas" in captured.out

# 6. Test generate_username
def test_generate_username():
    assert generate_username("Lucas", 1997) == "lucas97"

# 7. Test format_name
def test_format_name():
    assert format_name("juan perez") == "Juan Perez"

# 8. Test calculate_age
def test_calculate_age():
    current_year = date.today().year
    assert calculate_age(2000) == current_year - 2000

# 9. Test validate_phone
def test_validate_phone_valid():
    assert validate_phone(1234567890) is True

def test_validate_phone_invalid():
    assert validate_phone(12345) is False
    assert validate_phone("abcdefghij") is False

# 10. Test student_average (capture print output)
def test_student_average(capsys):
    student_average("Ana", 8, 9, 7)
    captured = capsys.readouterr()
    assert "Ana: Promedio = 8.00" in captured.out
