def home(func):
    def wrapper(user):
        context = {
            "form": func(user)
        }
        print(context)
    return wrapper


@home
def log_in(user):
    return user
log_in("Лох")