def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print(f"Function finished: {func.__name__}")

    return wrapper


@my_decorator
def do_this():
    print('Doing this')


@my_decorator
def do_that():
    print('Doing that')


# function called here will be passed to decorator and executed in line 4.
do_this()
do_that()
