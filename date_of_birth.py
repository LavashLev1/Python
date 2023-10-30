import datetime

def get_birthdays_per_week(users):
    # Створюємо словник для зв'язування днів тижня з ім'ями користувачів
    week_users = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }
    
    # Отримуємо поточний день тижня (понеділок - 0, вівторок - 1, ..., неділя - 6)
    current_weekday = datetime.date.today().weekday()
    
    # Ітеруємося по користувачах та додаємо їх до відповідних днів тижня
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        day_of_week = (birthday.weekday() - current_weekday) % 7  # Знаходимо, на який день тижня припадає день народження
        day_name = list(week_users.keys())[day_of_week]  # Назва дня тижня
        
        # Додаємо користувача до відповідного дня тижня
        week_users[day_name].append(name)
    
    # Виводимо результат
    for day, names in week_users.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Тестовий список користувачів
users = [
    {"name": "Bill", "birthday": datetime.date(1990, 10, 26)},
    {"name": "Jill", "birthday": datetime.date(1985, 10, 24)},
    {"name": "Kim", "birthday": datetime.date(1995, 10, 23)},
    {"name": "Jan", "birthday": datetime.date(2000, 10, 25)},
]

# Виклик функції для тестового списку користувачів
get_birthdays_per_week(users)
