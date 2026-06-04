def repeat_twice(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper

@repeat_twice
def greeting(name):
    print(f"Hola, {name}")
    return

#Main
user = "Didier"
greeting(user)