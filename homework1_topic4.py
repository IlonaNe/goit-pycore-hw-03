from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        current_date = datetime.today().date()
        entered_date = datetime.strptime(date, '%Y-%m-%d').date()
        difference = (entered_date - current_date).days
        return difference
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
