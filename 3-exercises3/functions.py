

# 1. Library Book Tracker
library = {}
def add_book(title, autor, pages):      
    library[title] = [autor, pages]

def find_book(title):
    if title in library:
        return "Found book"
    else:
        return "Book not found."
    
def show_books():
    for key, value in library.items():
        print (f"Book: {key}, Autor: {value[0]}, Pages: {value[1]}")


# 2. Student Grade Manager
grades = {}
def add_student(name_student):
    grades[name_student] = []

def add_grade(name_student, grade):
    grades[name_student].append(grade)

def get_average(name_student):
    average_grades = 0.0

    for value in grades[name_student]:
        average_grades += value

    average_grades = (average_grades/len(grades[name_student]))
    return average_grades

# 3. Restaurant Menu Editor
menu = {}
def add_dish(name_dish, price_dish, availability): 
    menu[name_dish] = [price_dish, availability]

def change_availability(name_dish, new_availability):    
    menu[name_dish] = [menu[name_dish][0], new_availability]

def total_available_price():

    sum_dishes = 0
    for value in menu.values():
        if value[1] is True:
            sum_dishes += value[0]

    return sum_dishes

# 4. Warehouse Box Counter
warehouse = {}
def add_box(box_type, amount):
    warehouse[box_type] = amount
    print(warehouse)

def update_quantity(box_type, new_amount):
    warehouse[box_type] = warehouse[box_type]+new_amount
    print(warehouse)


def has_enough(box_type, amount):    
    if warehouse[box_type] >= amount:
        return True
    else:
        return False

# 5. Movie Rating System
movies = {}
def add_movie(name_movie):
    movies[name_movie] = []
    
def rate_movie(name_movie, rating):
    movies[name_movie].append(rating)

def average_rating(name_movie):
    average_ratings = 0.0

    for value in movies[name_movie]:
        average_ratings += value

    average_ratings = (average_ratings/len(movies[name_movie]))    
    return average_ratings

# 6. Online Course Tracker
courses = {}
def add_course(title_course, duration, number_enrollment):
    courses[title_course] = [duration, number_enrollment]


def update_enrollment(title_course, new_number_enrrollment):
    courses[title_course] = [courses[title_course][0], new_number_enrrollment]

def filter_by_hours(hours):
    courses_filtered = []

    for key, value in courses.items():
        if value[0] >= hours:
            courses_filtered.append(key)
    return courses_filtered

# 7. To-Do List Organizer
todos = {}
def add_task(task,priority):
    todos[task] = [priority,"to do"]

def complete_task(task):
    todos[task] = [todos[task][0],"completed"]

def filter_tasks(priority, status):
    tasks_filtered = []

    for key, value in todos.items():
        if value[0] == priority or value[1] == status:
            tasks_filtered.append(key)
    return tasks_filtered

# 8. Digital Wallet
wallet = {}
def add_expense(category, value):
    wallet[category] = value

def total_spent():
    total_expenses = 0.0

    for value in wallet.values():
        total_expenses += value
    return total_expenses

def expense_percentages():
    category_percentages = {}
    total = 0
    
    for value in wallet.values():
        total += value
    
    for key, value in wallet.items():
        category_percentages[key] = ((value/total)*100)

    return category_percentages

# 9. Pet Adoption Center
pets = {}
def add_pet(name, specie, age):
    pets[name] = [specie,age]

def find_by_species(specie):
    pets_filtered = []

    for key, value in pets.items():
        if value[0] == specie:
            pets_filtered[key] = value
    return pets_filtered

def older_than(age):
    pets_older = []

    for key, value in pets.items():
        if value[1] >= age:
            pets_older.append({"name": key})
    return pets_older

# 10. Gym Membership System
members = []
def register_member(name_member, membership, payments_status):
    members.append({"name_member": name_member, "membership": membership, "payments_status":payments_status})

def change_plan(name, new_membership):
    for member in members:
        if member["name_member"] == name:
            member["membership"] = new_membership

def unpaid_members():
    defaulters = []
    for member in members:
        if member["payments_status"] == "late":
            defaulters.append(member["name_member"])
    return defaulters

