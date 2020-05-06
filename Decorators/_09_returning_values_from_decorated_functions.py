from _06_do_twice_args_kwargs_and_return import do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
hi_adam
print(hi_adam)
