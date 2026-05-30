"""
System actions like time and date.
"""
from typing import Tuple
from datetime import datetime


def get_time() -> Tuple[bool, str]:
    now = datetime.now()
    return True, now.strftime("The current time is %H:%M")


def get_date() -> Tuple[bool, str]:
    today = datetime.now()
    return True, today.strftime("Today is %B %d, %Y")
