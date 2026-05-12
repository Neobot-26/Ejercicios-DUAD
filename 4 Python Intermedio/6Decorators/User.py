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
    def wrapper(age):
        if age < 18:
            raise ValueError(
                "Age under 18.User is not an adult "
            )
        func(age)
    return wrapper

@verify_adult_age
def verify_age(age):
    print("The user is an adult")

# =========================
# Example of use
# =========================

my_user = User(date(1990, 1, 1))
print(f"Age: {my_user.age}")
verify_age(my_user.age)