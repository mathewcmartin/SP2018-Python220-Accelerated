### UWPCE 220 Accelerated Python

HW due 7 days after class

Amos is the TA and Brian is the other instructor

Slack will be used

### Functional Promgramming notes

- Anonymous functions
- Lambda
- Iterator
- Generator
- yield

Catch up on reading

### State vs Stateless

Stateless paradigms variables don't change

Write functions as stateless to introduce no side effects

- They do not change the state of the Promgramming
- They are different from statelessness

Referential Transparency: is both stateless and has not produced side effects

### Truth Tables

Pure Function

def m(n: int) -> int:
    return 2**n-1
​
## This result depends only on the parameter, n.
## There are no changes to global variables and the function doesn't update any mutable data structures.
A procedural approach!
Functions generally consist of multiple statements
Assignments
If-statements
While loops
Etc.

OPERATORS = '+', '-', '*', '/'

``
def p_main():

    """The main flow."""

    print('Welcome to the barely functional calculator!')
    number1 = p_get_number()
    operator = p_get_operator()
    number2 = p_get_number()
    result = p_calculate(number1, operator, number2)
    print('The result is: %s' % result)


def p_get_number():

    """Reads an integer from the standard input and returns it.
    If a non-integer value is entered, a warning is printed,
    and a new value is read."""

    while True:
        s = input('Enter an integer: ')
        try:
            return int(s)
        except ValueError:
            print('That is not an integer!')
OPERATORS = '+', '-', '*', '/'
​
​
def p_main():

    """The main flow."""
​
    print('Welcome to the barely functional calculator!')
    number1 = p_get_number()
    operator = p_get_operator()
    number2 = p_get_number()
    result = p_calculate(number1, operator, number2)
    print('The result is: %s' % result)
​
​
def p_get_number():

    """Reads an integer from the standard input and returns it.
    If a non-integer value is entered, a warning is printed,
    and a new value is read."""

    while True:
        s = input('Enter an integer: ')
        try:
            return int(s)
        except ValueError:
            print('That is not an integer!')

​
def p_get_operator():

    """Reads an operator from the standard input and returns it.
    Valid operators are: +, -, *, and /. If an invalid operator
    is entered, a warning is printed, and a new value is read."""    

    while True:
        s = input('Enter an operator (+, -, *, or /): ')
        if s in OPERATORS:
            return s
        print('That is not an operator!')


def p_calculate(number1, operator, number2):

    """Performs a calculation with two numbers and an operator,
    and returns the result."""

    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '/':
        return number1 / number2
    raise Exception('Invalid operator!')
​

p_main()
​
Welcome to the barely functional calculator!
Enter an integer: 10
Enter an operator (+, -, *, or /): *
Enter an integer: 30
The result is: 300
A functional approach!
Functions consist of only one expression
How can we validate input? (One of the many things we will learn later!)

OPERATORS = '+', '-', '*', '/'


def f_get_number():
    return int input('Enter an interger:')


def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))


def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None


def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )

print('The result is: %s' % f_main())

OPERATORS = '+', '-', '*', '/'
​
​
def f_get_number():
    return int input('Enter an interger:')
​
​
def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))
​
​
def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None
​
​
def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )
​
print('The result is: %s' % f_main())
​
​
  File "<ipython-input-1-e64a913a0397>", line 5
    return int input('Enter an interger:')
                   ^
SyntaxError: invalid syntax



OPERATORS = '+', '-', '*', '/'


def f_get_number():
    return int(input('Enter an interger:'))


def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))


def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None


def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )

print('The result is: %s' % f_main())
OPERATORS = '+', '-', '*', '/'
​
​
def f_get_number():
    return int(input('Enter an interger:'))
​
​
def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))
​
​
def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None
​
​
def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )
​
print('The result is: %s' % f_main())
​
  File "<ipython-input-2-2a70960dce57>", line 5
    return int input('Enter an interger:')
                   ^
SyntaxError: invalid syntax



def f_get_number():
    return int(input('Enter an interger:'))


def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))


def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
    else None


def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )

print('The result is: %s' % f_main())
OPERATORS = '+', '-', '*', '/'
​
​
def f_get_number():
    return int(input('Enter an interger:'))
​
​
def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))
​
​
def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
    else None
​
​
def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )
​
print('The result is: %s' % f_main())
​
  File "<ipython-input-3-90c4fee4480e>", line 14
    else None
    ^
IndentationError: unexpected indent



else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None
def f_get_number():
    return int(input('Enter an interger:'))
​
​
def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))
​
​
def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None
​
​
def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )
​
print('The result is: %s' % f_main()
  File "<ipython-input-4-c0378b4dbd37>", line 11
    else None
    ^
IndentationError: unexpected indent



def f_get_number():
    return int(input('Enter an interger:'))
​
​
def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))
​
​
def f_calculate(number1, operator, number2):
    return number1+number2 if operator =='+'\
    else number1+number2 if operator =='*'\
    else number1+number2 if operator =='-'\
    else number1/number2
    else None
​
​
def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )
​
print('The result is: %s' % f_main()
  File "<ipython-input-5-f9ee1fe2fffd>", line 11
    else None
       ^
SyntaxError: invalid syntax

```
list(range(10))

for x in range(10):
    print (x)
```    
### MAP
```
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)
```
### Filter
```
number_list = range(-10, 10)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

number_list = range(-10, 10)
less_than_zero = list(filter(lambda x: x > 0, number_list))
print(less_than_zero)
```
### Reduce
```
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3])
print(product)
```
### List Comprehension
```
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

squared = [x**2 for x in range(10)]
print(squared)
```
### Dict Comprehension
```
mcase = {'a': 5, 'b': 3, 'A': 7, 'Z': 6}
{v: k for k, v in mcase.items()}
```
### Set Comprehension
```
squared = {x**2 for x in [0,1,1,2]}
print(squared)
```
In the previous set example, can you explain the output?

### Iterators and iterables
[Iterables](http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/)

Requires iter() and next()



Iter() Operation
Examples of Iter - lists, dictionaries etc ....

```
iter([2,3,4])

iter({1:2, 3:4, 5:8})
```
## is this iterable? Try ....

```
iter(104)
```
##Lets start with user defined String class
```
class String(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val

st = String('sample string')

​
```
Is the above string iterable? lets test it.
```
iter(st)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-749da7adf89a> in <module>()
----> 1 iter(st)

NameError: name 'st' is not defined
```
Why didn't this work?
What's missing?
the magic - an_iterator.iter()

Then, how should we make user defined type iterable?
This can be done by extending our String class with iter constructor

```
class String(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val
    def __iter__(self):
        print ("This is __iter__ method of String class")
        return iter(self.val)  #self.val is python string so iter() will return it's iterator

st = String('Sample String')

iter(st)
```
This is __iter__ method of String class
<str_iterator at 0x14cc916fd68>
We added a iter method in our String class to make String type as iterable. That means iter(iterable) calls iterable.iter() internally.
You could also do this using getitem

```
class String(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val
    def __getitem__(self, index):
        return self.val[index]

st = String('Sample String')

iter(st)
<iterator at 0x14cc91e7940>
```
We added getitem method and user defined String type becomes iterable. So iter(iterable) look for iterable.getitem() also.

​
Iterator
Iterator object produces values of iterable during iteration. next() or next() is applied on iterator for producing next value
It raises StopIteration exception at the end of iteration
iter() function return iterator object for an iterable
If iter() function is applied on iterator object, it returns same object

## List as an iterator
​```
a_list = [1,2,3]
list_iter = a_list.__iter__()
​```
## before python 2.6 I think - list_iter.next()
```
list_iter.__next__()
​

list_iter.__next__()
```
## see what happens after 2 more times?
​
IterTools
itertools is a collection of utilities that make it easy to build an iterator that iterates over sequences in various common ways

http://docs.python.org/library/itertools.html

NOTE:

iterators are not only for for

They can be used with anything that expects an iterator:

sum, tuple, sorted, and list

For example.

```
import itertools
​
letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]
Chain

print (list(itertools.chain(letters, booleans, decimals)))
['a', 'b', 'c', 'd', 'e', 'f', 1, 0, 1, 0, 0, 1, 0.1, 0.7, 0.4, 0.4, 0.5]
compress()
compress(): given two lists a and b, return the elements of a for which the corresponding elements of b are True.


print (list(itertools.compress(letters, booleans)))
​
['a', 'c', 'f']
Zip ()

xi= [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65]
yi= [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29]
zip( xi, yi )


list(zip( xi, yi ))

zip( xi, yi )

list(_)
```
​
We can see that the zip() function with no arguments is a generator function, but there won't be any items. This fits the requirement that the output is iterable.
```
zip( (1,2,3) )
<zip at 0x14cc92118c8>

list(_)
​
```
## In this case, the zip() function emitted one tuple from each input value. This too makes considerable sense.
```
[(1,), (2,), (3,)]
```
[Itertools](http://docs.python.org/library/itertools.html)

To be clear, in order to make your class an iterator you need to do two things:

1. Add an __iter__ function that returns the object itself (self)

2. Add a next function that returns the next item in the sequence each time it is called. When there are no more items in the sequence, the next function raises a StopIteration exception signal the end of the iteration.

#### Listing 1
```
class ByteValue(object):

    def __init__(self, data):
        self.data = data

    def to_bytes(self):
        bytes = []
        for char in self.data:
            bytes.append(ord(char))
            return bytes
```
#### Listing 2
```
class ByteValue(object):

    def __init__(self, data):
        self.data = data
        self.current_item = 0

    def __iter__(self):
        return self

    def next(self):
        if (self.current_item == len(self.data)):
            raise StopIteration
        else:
            byte_value = ord(self.data[self.current_item])
            self.current_item += 1
            return byte_value
```
#### generator

A generator is a function that creates, or generates, an iterator. In order for a function to become a generator it must return a value using the yield keyword.

#### Keywords

New Words, Concepts, and Tools
- Anonymous function
- Lambda
- Iterator
- Iterable
- Generator
- yield

#### Reading Class 1 220

Required Reading:
[Small functions and the lambda expression](https://docs.python.org/dev/howto/functional.html?highlight=lambda#small-functions-and-the-lambda-expression)

[Iterators](https://docs.python.org/3/glossary.html#term-iterator)
(https://docs.python.org/3/library/stdtypes.html#iterator-types)
(https://docs.python.org/dev/howto/functional.html#iterators)

[Itertools](https://docs.python.org/3/library/itertools.html (Links to an external site.)
(https://pymotw.com/3/itertools/index.html)

What exactly are Python's iterator, iterable, and iteration protocols?
(https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols)

[Generators](https://wiki.python.org/moin/Generators

Optional Reading
Lott, S. (2015) Chapter 5. Higher-order Functions. Using Python lambda forms. In Functional Python Programming.
Lott, S. (2015) Chapter 3. Functions, Iterators, and Generators. In Functional Python Programming.
[The Iterator Protocol: How For Loops Work in Python](http://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/ (Links to an external site.)

[Chapter 14 in Fluent Python by Luciano Ramalho](http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/ (Links to an external site.)

[PEP 255 — Simple Generators](https://www.python.org/dev/peps/pep-0255/)
​
