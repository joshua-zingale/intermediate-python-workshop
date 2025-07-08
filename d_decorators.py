import time

def main():
    print(fib_recursive(25) == fib_iterative(25))


# This is a function that "wraps" around another function by
# keeping the functionality the same while adding in a timer
# to track performance
def timed_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Function '{func.__name__}' with arguments {args} and {kwargs} took {duration} seconds to run")
        return return_value
    return wrapper

def fib_recursive(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib_recursive(n-1) + fib_recursive(n-2)

# We reassign the name "fib_recursive" to a wrapped version of the functoin     
fib_recursive = timed_function(fib_recursive)


# The decorator syntax, with @, does the same as the above explicit wrapping:
# The following is the same as having `fib_iterative = timed_function(fib_iterative)`
@timed_function
def fib_iterative(n):
    if n == 0:
        return 0
    last = 0
    curr = 1
    for _ in range(n-1):
        curr, last = curr+last, curr
    return curr


if __name__ == "__main__":
    main()
