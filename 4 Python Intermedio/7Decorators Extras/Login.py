user_logged_in=True

def requires_login(func):
    def wrapper(*args,**kwargs):
        if not user_logged_in:
            raise ValueError(
                "User not authenticated "
            )
        func(*args,**kwargs)
    return wrapper

@requires_login
def view_profile():
    print(f"Displaying User´s profile")
    return

#Main
view_profile()
