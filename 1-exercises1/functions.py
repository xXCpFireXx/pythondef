def calculate_tip(amount, percentage):
    tip = amount * (percentage / 100)
    return tip

def meters_to_kilometers(meters):
    return meters / 1000

def create_email(first_name, last_name, domain):
    return f"{first_name.lower()}.{last_name.lower()}@{domain.lower()}"

def final_price(base_price, tax=0.21):
    return base_price * (1 + tax)

def validate_login(username, password):
    valid_username = "admin"
    valid_password = "1234"
    if username == valid_username and password == valid_password:
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Credenciales incorrectas")
        return False

def generate_username(name, birth_year):
    year_suffix = str(birth_year)[-2:]
    return f"{name.lower()}{year_suffix}"

def format_name(full_name):
    return full_name.title()

from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

def validate_phone(number):
    return len(str(number)) == 10 and str(number).isdigit()

def student_average(name, *grades):
    if grades:
        average = sum(grades) / len(grades)
        print(f"{name}: Promedio = {average:.2f}")
    else:
        print(f"{name}: No hay notas disponibles")
