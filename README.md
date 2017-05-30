# FooBarQix

You should implements a function String foobarqix(String) which implements the following rules.

## Rules

* If the number is divisible by 3, write "Foo" instead of the number
* If the number is divisible by 5, add "Bar"
* If the number is divisible by 7, add "Qix"
* For each digit 3, 5, 7, add "Foo", "Bar", "Qix" in the digits order.
 
## Examples

    1  => 1
    2  => 2
    3  => FooFoo (divisible by 3, contains 3)
    4  => 4
    5  => BarBar (divisible by 5, contains 5)
    6  => Foo (divisible by 3)
    7  => QixQix (divisible by 7, contains 7)
    8  => 8
    9  => Foo (divisible by 3)
    10 => Bar (divisible by 5)
    13 => Foo (contains 3)
    15 => FooBarBar (divisible by 3, divisible by 5, contains 5)
    21 => FooQix
    33 => FooFooFoo (divisible by 3, contains two 3)
    51 => FooBar
    53 => BarFoo

