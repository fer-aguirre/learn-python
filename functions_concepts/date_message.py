from datetime import datetime

""" Decorator to give a welcome message"""
def date_message(*args, **kwargs):
    def with_message(func):
        list_names = list(args)
        names = ', '.join(list_names)
        print(f"Hello {names}!")
        def wrapper():
            func()
        return wrapper
    return with_message


@date_message("Eli", "Ana", "John")
def get_date():
        date = datetime.now()
        day = date.strftime("%A")
        day_num = date.strftime("%d")
        month = date.strftime("%B")
        year = date.strftime("%Y")
        print(f"Today is: {day} {day_num} of {month} {year}")
get_date()


@date_message("Paul")
def get_hour():
    my_hour = datetime.now()
    hour = my_hour.strftime("%l")
    meridian = my_hour.strftime("%p")
    minutes = my_hour.strftime("%M")
    print(f"It's {hour} {meridian} with {minutes} minutes")
get_hour()