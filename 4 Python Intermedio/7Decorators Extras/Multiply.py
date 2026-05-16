from datetime import datetime

def log_call(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        actual_date=datetime.now()
        print(f"func:  {func.__name__} args:{args} {actual_date} - Result: {result}")
        return result
    return wrapper

def validate_numbers(func):
    def wrapper(*args,**kwargs):
        for index_args in args:
            if not isinstance(index_args,(int,float)):
                raise ValueError(
                    "All values must be numeric"
                )
        return func(*args,**kwargs)
    return wrapper

@validate_numbers
@log_call
def multiply(value1,value2):
    return value1*value2

#Main
result = multiply(3, 4)
print(f"Result is {result}")
