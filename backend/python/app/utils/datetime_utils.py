from datetime import datetime, timezone

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def get_current_date() -> str:
    dt = datetime.now()
    month_name = MONTHS[dt.month - 1]
    day = f"{dt.day:02d}"
    return f"{month_name} {day}, {dt.year}"


def get_current_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


def get_current_datetime() -> str:
    return datetime.now().strftime("%B %d, %Y %H:%M:%S")


def get_current_datetime_with_timezone() -> str:
    return datetime.now(timezone.utc).strftime("%B %d, %Y %H:%M:%S")
