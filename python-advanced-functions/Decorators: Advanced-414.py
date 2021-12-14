## 1. Introduction ##

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        func(*args, **kwargs)

    wrapper.count = 0
    # Return the new decorated function
    return wrapper
@counter
def foo():
    print('calling foo()')    

foo()
foo()

print('foo() was called {} times.'.format(foo.count))

## 2. Real World Decorators ##

def print_return_type(func):
    print()
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))
        return result
    return wrapper
              
@print_return_type
def foo(value):
    return value
              
print(foo(42))
print(foo([1,2,3]))
print(foo({'a':42}))

## 3. Preserving Metadata When Decorating Functions ##

def timer(func):
    """A decorator that prints how long a function took to run."""  
    def wrapper(*args, **kwargs):
        t_start = time.time()
    
        result = func(*args, **kwargs)
    
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
    
        return result
    return wrapper
@timer
def sleep_n_seconds(n=10):
    """Pause processing for n seconds.
  
    Args:
        n (int): The number of seconds to pause for.
    """
    time.sleep(n)
    
print(sleep_n_seconds.__doc__)

print(sleep_n_seconds.__name__)

## 4. Preserving Metadata When Decorating Functions Continued ##

from functools import wraps
def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)
    
print_sum(10,20)
print(print_sum.__doc__)

## 6. Adding Arguments to Decorators Continued ##

def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@run_n_times(3)
def print_sum(a, b):
    print(a + b)
print_sum(3,5)

@run_n_times(5)
def print_hello():
    print('Hello!')
print_hello()

## 7. Real World Decorators with Arguments ##

import signal
def timeout(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set an alarm for 5 seconds
            signal.alarm(n)
            try:
                # Call the decorated func
                return func(*args, **kwargs)
            finally:
                # Cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator
@timeout(20)
def bar():
    time.sleep(10)
    print('bar!')
    
bar()

## 8. Real World Decorators with Arguments Continued ##

from functools import wraps
def tag(*tags):
    def decorator(func):
        
        # Define a new decorator to return
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
        # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    return decorator
    # Return the new decorator
  

@tag('test', 'this is a tag')
def foo():
    pass

print(foo.tags)