# Introduction
Frukt is a dynamically typed programming language inspired mainly from Lua, Gdscript and Typescript.

Feel free to help if you have an idea of some addition or change 

> [!NOTE]
> currently this is just thoughts and ideas, this language doesn't actually have a working compiler.
> in the future I have plans to make three versions, them being: Transpiled, Interpreted and finally JIT (just in time compilation) in that order
# Features
## Comments
There are two different ways to make comments. either single-line comments with a single hashtag like in python, or a comment block using two separate `#--`
```gdscript
# this is a single line comment
#--
these are all lines inside
a comment block. they dont
have to streach through multiable lines,
but can also be used in tight spaces,
like describing a function argument if
its name cant explain it
#--

#-- here is a comment block that could be placed inbetween stuff #--
```

> [!NOTE]
> as you see, unlike many other languages with comment blocks, these open and closing "symbols" are symmetrical. an example of a unsymmetrical comment block are `/*` and `*/`. you can think of a man opening a scroll
>
> ![image](medieval-man-holding-scroll-isolated-260nw-231944920.webp)
## Types
### String
a string is an array of characters, you can use them for easy debugging or showing information to someone using the script.

strings are made with two quotation marks (both double and single works)
```gdscript
"this is a string!"
'this too!'
```
#### Interpolation
String interpolation means inserting variable values or expressions directly into a string, this is good for cases where you want dynamic and readable logs, or formatted outputs without messy string concatenation

Interpolation is done via adding an `f` before a string, then using opening/closing braces (`{}`) for inserting values, just like in python.
```gdscript
print(f"1 + 2 = {1 + 2}") # output: 1 + 2 = 3

var string = "foo"
prtint(f"{string}bar") # output: foobar

var usr_age = int(input("how old are you?"))
print(f"you are born year {2025 - age}!")
```
### Integer
An integer is a binary 32 bit value. What that means is that it can store a whole number with the range of `2^32`, which is 4 294 967 296. though to get negative numbers one bit is used, that means you have a range from `2^31` to `-2^31`, that is 2 147 483 648 to -2 147 483 648.
Integers are used when you want to store any size whole number.
### Float
Float is short for "Floating point value". Unlike a integer (`int`), a float can have decimals, this is due to it storing numbers with a binary exponent. What that means is that you can store numbers with decimals via using a negative exponent (example: `2.53e-2 = 0.0253`).
Floats are used when a number needs decimal precision
### Long
A long is like an integer but it can store massive numbers. `int`'s use 32 bits to store their data, and `long`'s use 64 bits, that's double the amount.
```gdscrip
var my_large_number: long = 1e10 # "e" means exponent, so that is equal to `10^10` which is to large for a integer
```
### Number
a `num` is all number storing types at the same time, it dynamically switches from one to the other when needed, that means a variable set to a number can have integer, long or float value.
the `num` type is fully compatible with integers and floats, that means you can set a number to a int value, and an int to a number value
```gdscript
var number: num
number = 1.5 # works
number = 1 # also works

var integer: int
var floating_point: float
integer = number # same as `int(number)`
floating_point = number # also works, same as `float(number)`
```

## Declarations 
### Variables
To declare a variable you use the keyword `var`, then assign a value to it with the equals sign
```gdscript
var greeting = "Hello!"
```

> [!NOTE]
> a variable doesn't need to get declared with a value, if it doesn't have one, it wont get declared until it gets a value later in the program. If the variable is used before it gets a value or if it never gets a value in local space, it gets declared with a value of `none`
> you can find more info under
### Constants
you can declare a constant with the `const` keyword. a constant is like a variable but it cant be changed
```gdscript
const constant_var = "This wont Change!"
```

> [!NOTE]
> unlike many languages with constants, you can declare a constant without a value.
> when a constant is declared without a value it becomes a `none` type.
> its recommended not to do this since constants don't have the same treatment as normal variables when undefined. i.e. it gets a space in memory as soon as its declared
### Functions
to define functions, use the `func` keyword

```gdscript
func greet(name) do
	print(f"Hello {name}!")
end
```

you can pass arguments to a function, do this via adding the wished arguments inside the parenthesis, then when the function is ran you pas through the argument inside the parenthesis
```gdscript
func greet(name) do
	print("Hello" + name + "!")
end
```

you can have multiple arguments via separating them with a comma, you will also see the keyword `return` used here, what it does is when the function gets a call-back (it gets used) the function will "return" the value, so if it returns a number you can use the function and add it to an other number
```gdscript
func add(x, y) do
	return x + y
end

print(2 + add(3, 7)) # output: 12
```

when calling a function (using it) you can specify what argument is what value
```gdscript
func greet(age, name) do
	print(f"Hello {name}! you are {age} years old!")
end

greet(name="foo", age=25) # output: Hello foo ! you are 25 years old!"
```

### Type Declaration
everything that can have/return a type can be specified (eg variables since they can be a type and functions since they can return types). you do this with a colon
```gdscript
var a: int = 0 # this means that "a" is of type int and wont change
var b := true # this means that "b" is of the initial values type, in this case it'a a bool

func echo(thing: str): str do # this is a function that takes a string and returns a string
	retrun thing
end
```

## Operators
an operator is a symbol, or a group of symbols that do something,
### Comparison
**Equal to**: `x == y`
**Precise Equal to**: `x === y`
**Weak Equal to**: `x ~= y`
**Not equal to**: `x != y`
**Precise Not equal to**: `x !== y`
**Weak Not equal to**: `x ~!=`
**Smaller then**: `x < y`
**Greater then**: `x > y`
**Smaller or Equal to**: `x <= y`
**Greater or Equal to**: `x >= y`
### Arithmetic
**Add**: `x + y`
**Subtract**: `x - y`
**Multiply**: `x * y`
**Divide**: `x / y`
**Remainder**: `x % y`
**Raised to the Power**: `x ** y` or `x^y`
### Assignment
**Assign**: `x = y`
**Add to current value and Assign**: `x += y`
**Subtract from current value and Assign**: `x -= y`
**Multiply current value with and Assign**: `x *= y`
**Divide current value with and Assign**: `x /= y`

## Conditions
Conditions are used by some keywords, these need to be a `bool`. that means either `true` or `false`. When that condition is true the keyword runs, that means that that line runs.
Here are some different keywords that use conditions:
### If/else
`if` takes in a `bool` condition and runs the code in the line if that condition is `true`, `if` is structured like `if condition code`.
```gdscript
if true print("Hello world!") # this will always print since the condition is a constant true
```

here is a better use of the if statement
```gdscript
if (input("what food do you like? ") == "hamburger") print("me too")
```
in this example you see that I have the condition inside two parentheses. Unlike many languages, it's not necessary for the statement to work, but highly recommended if you want more readable code. since else its hard to distinguish between the condition and code.

if you want to run multiple lines with the if keyword, you can surround the code in a `do` and `end`. think of them as opening and closing brackets, and for people who haven't used a language that uses them before, think of the `do` keyword as telling the `if` keyword to keep running code until the corresponding `end` keyword is reached.
```gdscript
var x = int(input("number 1: "))
var y = int(input("number 2: "))
var opperation = input("opperation(+ or -): ")

if (opperation == "+") do
	print(f"adding {x} with {y}")
	print(f"sum is: {x + y}")
end
if (opperation == "-") do
	print(f"subtracting {x} with {y}")
	print(f"dif is: {x - y}")
end
```

## Wild-card things
here is the rest that I couldn't find a good place to categorize them.
### Concatenation
you can concatenate almost any two things of same type. Most commonly used for strings, but you can use it for anything like integers, arrays, or lists to name a few.
What it means to "Concatenate" two values is that you put the second value at the end of the first.
You concatenate with two dots in-between the two values to concatenate, when concatenating multiple values there is a left bias (that means first the two left-most values will concatenate, then that new value is "substituted" to be concatenated)
```gdscript
print("foo".."bar") # output: foobar
print(3..2) # output: 32
print([3]..[2, 5]) # output: [3, 2, 5]
```

the `..` just run the `__concat()` function of the first value, that means you can add your own concatenate method to your classes.
Every time you concatenate built-in types it always returns with the same type.


---
# Explanations
here you'll find in depth explanations on how stuff works, and when/why to use stuff.
## Variable usage
### Undeclared variables and constants
its not always guaranteed that you have something to save yet, you might know that you need a variable for something, just that you don't know it yet. That's a place where you would want to use an undeclared variable, or rather define a variable without a value. So that you later on can give it one

under the hood, a undefined variable doesn't actually exist. What that means is that variables without any value on declaration doesn't exist, that means...
```gdscript
var a
a = "hello world!"
```
and...
```gdscript
var a = "hello world!"
```
use the exact same resources.

if a variable never get a value it will be replaced with `none`. That means...
```gdscript
var a

if a do
	print(a)
end
```
and...
```gdscript
if none do
	print(none)
end
```
also use the same resources

but, if a variable isn't declared with a value, and gets one later in the script, it's value will be set to `none`, instead of being replaced. That means...
```gdscript
var a

if a do
	print(a)
else do
	a = "hello world!"
end
```
and...
```gdscript
var a = none

if a do
	print(a)
else do
	a = "hello world!"
end
```

# Faq (Frequently Asked Questions)
**What is "FooBar"?**
"foobar" is nothing but test names, they are frequently used in programming languages to show how things work and how to do stuff.

# Dictionary of all keywords
`do`/`end`
acts like a "code block" that groups together lines of code. Its used in situations where you can only use one line of code, like `if` or `while` statements

`if`
runs the code after the condition

`else`
always used after an `if` statement, runs the code if the `if` statements condition was false.

`do`+`end`
the `do` and `end` keywords are always used together, they act like how curly brackets work in many other languages work. they group up multiple lines of code so that its easier to read.

