from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between a given date and the current date.
    
    Parameters:
    date (str): A string representing the date in 'YYYY-MM-DD' format (e.g., '2020-10-09').
    
    Returns:
    int: The number of days from the given date to today (negative if the given date is in the future).
    None: If the input string has an invalid date format.
    """
    try:
        # Convert the input string into a datetime object and extract only the date portion (ignoring time)
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Get the current local date (ignoring time)
        today_date = datetime.today().date()
        
        # Calculate the difference: current date minus the given date
        difference = today_date - given_date
        
        # Return the difference in days as an integer
        return difference.days
        
    except ValueError:
        # Handle the exception if the input date is in an incorrect format

        print(f"Помилка: Неправильний формат дати '{date}'. "
              f"Будь ласка, використовуйте формат 'РРРР-ММ-ДД' (наприклад, '2020-10-09').")
        return None
    
# 1. Приклад із датою в минулому
days_left = get_days_from_today("2020-10-09")
print(f"Кількість днів: {days_left}\n")

# 2. Приклад із датою в майбутньому (якщо сьогодні 2026-07-23, а дата 2026-12-31)
days_left = get_days_from_today("2026-12-31")
print(f"Кількість днів: {days_left}\n")

# 3. Приклад обробки некоректного формату дати
days_left = get_days_from_today("09-10-2020")
print(f"Результат для некоректної дати: {days_left}\n")