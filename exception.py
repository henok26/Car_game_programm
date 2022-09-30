from timeit import timeit

code1="""
try:

    div = int(input("enter ur age"))
    if div <= 0:
        raise ValueError
    x = 10 / div
except ValueError as erro :

    print("erro")
except ZeroDivisionError as ex:

    print()
    print(ex)

"""
print("first",timeit(code1,number=10000))