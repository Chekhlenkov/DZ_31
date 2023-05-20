import datetime

from rest_framework.exceptions import ValidationError


def checkBDay(birth_date):
    today = datetime.date.today()
    age = (datetime.date.today().year - birth_date.year) - 1 + ((today.month, today.day) < (birth_date.month, birth_date.day))
    if age < 9:
        raise ValidationError(f"Малолетка {age}")


def chek_email(email):
    if "rambler.ru" in email:
        raise ValidationError("Не допустимый домен rambler.ru")