from datetime import date

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def verify_adult_age(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError(
                "Age under 18.User is not an adult "
            )
        return func(user,*args,**kwargs)
    return wrapper

@verify_adult_age
def verify_age(user):
    print("The user is an adult")

# =========================
# Example of use
# =========================

my_user1 = User(date(1990, 1, 1))

my_user2 = User(date(2010, 1, 1))
verify_age(my_user1)
verify_age(my_user2)