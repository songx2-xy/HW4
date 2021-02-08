def cube(a):
    try:
        return a*a*a
    except TypeError:
        return "Error"
