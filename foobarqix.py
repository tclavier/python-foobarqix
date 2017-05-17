def foobarqix(number):
    dico={3:'Foo', 5: "Bar", 7: "Qix"}

    divisible = [ value for divisor,value in dico.iteritems() if number % divisor == 0 ]

    contains = [ dico[int(digit)] for digit in str(number) if int(digit) in dico ]

    result = divisible + contains
    if len(result) > 0:
        return "".join(result)
    return str(number)

