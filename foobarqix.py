def foobarqix(number):
    asso={3:'Foo', 5: "Bar", 7: "Qix"}

    is_divisible=False

    accumulator = [value for divisor,value in asso.iteritems() if number % divisor == 0 ]

    if len(accumulator) > 0:
        return "".join(accumulator)
    return str(number)

