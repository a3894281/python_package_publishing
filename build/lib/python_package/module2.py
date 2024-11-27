def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero.")
    return a / b
    