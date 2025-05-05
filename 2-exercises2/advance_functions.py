import string
import random

# 1. Shopping cart simulator
def calculate_cart_total(items, tax=0.21):
    subtotal = 0
    for item in items:
        price = item["price"]
        quantity = item["quantity"]
        subtotal += price * quantity
    total = subtotal * (1 + tax)
    return round(total, 2)

# 2. Text processing (word count)
def word_count(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

# 3. Secure password generator
def generate_password(length=12):
    if length < 6:
        raise ValueError("La longitud mínima debe ser de 6 caracteres")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 4. Weather analyzer (temperatures)
def analyze_temperatures(temps):
    if not temps:
        return None, None, None
    avg = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    return avg, max_temp, min_temp

# 5. Functional contact book
def add_contact(book, name, phone):
    new_book = book.copy()
    new_book[name] = phone
    return new_book

def find_contact(book, name):
    return book.get(name, "No encontrado")

def delete_contact(book, name):
    new_book = book.copy()
    new_book.pop(name, None)
    return new_book
