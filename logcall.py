from functools import wraps

def logformat(fmt: str):
    def logged(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            print(fmt.format(func=func))
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return logged

logged = logformat('Calling {func.__name__}')
