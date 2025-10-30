from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        upcoming_birthdays = birthday.replace(year=today.year)
        if upcoming_birthdays < today:
            upcoming_birthdays =   upcoming_birthdays.replace(year=today.year + 1)
            days_to_birthday = (upcoming_birthdays - today).days
            if 0 <= days_to_birthday <=5:
                congratulation_date = upcoming_birthdays
            elif days_to_birthday == 6:
                congratulation_date = upcoming_birthdays + timedelta(days=1)
            elif days_to_birthday == 7:
                congratulation_date = upcoming_birthdays + timedelta(days=2)
            
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays
