
def foobarqix(number):
    dico={3:'Foo', 5: "Bar", 7: "Qix"}

    result = replaceByDivisible(dico, number) + replaceByContains(dico, number)
    if isDivisibleOrContains(result):
        return "".join(result)
    return str(number)

def replaceByDivisible(dico, number):
    return [ value for divisor,value in dico.items() if number % divisor == 0 ]

def replaceByContains(dico, number):
    return [ dico[int(digit)] for digit in str(number) if int(digit) in dico ]

def isDivisibleOrContains(string):
    return len(string) > 0
