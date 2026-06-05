from datetime import date, timedelta


def is_birthday_in_next_N_days(n: int, date_of_birth: date) -> bool:
    today = date.today()
    end_date = today + timedelta(days=n)

    # Handle leap year
    try:
        this_year_birthday = date_of_birth.replace(year=today.year)
    except ValueError:
        this_year_birthday = date(today.year, 2, 28)

    # Handle if birthday is in N days but next year
    try:
        next_year_birthday = date_of_birth.replace(year=today.year + 1)
    except ValueError:
        next_year_birthday = date(today.year + 1, 2, 28)

    is_this_year = today <= this_year_birthday <= end_date
    is_next_year = today <= next_year_birthday <= end_date

    return is_this_year or is_next_year
