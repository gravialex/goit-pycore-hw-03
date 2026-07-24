from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    """
    Identifies users who have birthdays within the next 7 days (including today).
    If a birthday falls on a weekend, the congratulation date is shifted
    to the upcoming Monday.
    
    Parameters:
    users (list): A list of dictionaries containing user names and their birthdays.
                  Format: [{'name': 'John Doe', 'birthday': '1985.01.23'}, ...]
                  
    Returns:
    list: A list of dictionaries containing the user name and their scheduled congratulation date.
          Format: [{'name': 'John Doe', 'congratulation_date': '2024.01.23'}, ...]
    """
    # Get the current system date (excluding the time part)
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        try:
            # Parse the user's birthday string to a date object
            original_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            
            # Replace the birth year with the current year to find this year's birthday
            birthday_this_year = original_birthday.replace(year=today.year)
            
            # If the birthday has already passed this year, look at next year's date instead
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            # Calculate the difference in days between the birthday and today
            days_until_birthday = (birthday_this_year - today).days
            
            # Check if the birthday falls within the upcoming 7 days (inclusive of today)
            if 0 <= days_until_birthday <= 7:
                # Determine the day of the week (0 = Monday, ..., 5 = Saturday, 6 = Sunday)
                weekday = birthday_this_year.weekday()
                congratulation_date = birthday_this_year
                
                # Shift to Monday if the birthday falls on a weekend
                if weekday == 5:    # Saturday
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif weekday == 6:  # Sunday
                    congratulation_date = birthday_this_year + timedelta(days=1)
                
                # Append the record to the list, formatting the date back to 'YYYY.MM.DD'
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })
                
        except (ValueError, KeyError) as e:
            # Gracefully skip entries with wrong formats or missing keys
            print(f"Skipping user {user.get('name', 'Unknown')}: invalid birthday or missing key. Error: {e}")
            
    return upcoming_birthdays

# Example usage:
users = [
    # Birthday today (Friday, Jul 24) -> congratulation date: Today (Jul 24)
    {"name": "Alice Green", "birthday": "1990.07.24"},
   
    # Birthday tomorrow (Saturday, Jul 25) -> congratulation date: Monday (Jul 27)
    {"name": "Bob Miller", "birthday": "1988.07.25"},
    
    # Birthday on Sunday, Jul 26 -> congratulation date: Monday (Jul 27)
    {"name": "Jane Smith", "birthday": "1990.07.26"},
    
    # Birthday on Wednesday, Jul 29 -> congratulation date: Wednesday (Jul 29)
    {"name": "John Doe", "birthday": "1985.07.29"},
    
    # Birthday on August 5th (More than 7 days away) -> should not be included
    {"name": "Charlie Brown", "birthday": "1995.08.05"},
]

upcoming = get_upcoming_birthdays(users)
print("Upcoming birthday greetings for this week:")
for entry in upcoming:
    print(entry)