# Introduction
Frukt is a dynamically typed programming language inspired mainly from Lua, Gdscript and Typescript.

Feel free to help if you have an idea of some addition or change 

> [!NOTE]
> currently this is just thoughts and ideas, this language doesn't actually have a working compiler.
> in the future I have plans to make three versions, them being: Transpiled, Interpreted and finally JIT (just in time compilation) in that order
# Features
## Comments
There are two different ways to make comments. either single-line comments with a single hashtag like in python, or a comment block using two separate `#--`
```
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
a string is an list of characters, you can use them for easy debugging or showing information to someone using the script.

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
print(f"{string}bar") # output: foobar

var usr_age = int(input("how old are you?"))
print(f"you are born year {2025 - age}!")
```
#### Regular Expression (RegEx)
Regular Expression (RegEx) is a way to search a string for different patterns. There specific RegEx patterns are made with two separate "\`", like this:
```gdscript
var regex_pattern: REPattern = `hello`
```
then you can match that pattern to another string like:
```gdscript
var matches: [dict] = regex_pattern.match("hello world!")
```
that will return, as hinted at, a list of `dict`, where each dict is its own match, containing information like position, match number or the match itself.
```python
print(matches) #output: []
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
number = 1 # works
number = 1.5 # also works

var integer: int
var floating_point: float
integer = number # same as `int(number)`
floating_point = number # also works, same as `float(number)`
```
### List
A `list` is an iterable type containing multiple values without specified keys, only identifier for each value is its index

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

```lua
func greet(name) do
	print(f"Hello {name}!")
end
```

you can pass arguments to a function, do this via adding the wished arguments inside the parenthesis, then when the function is ran you pas through the argument inside the parenthesis
```lua
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
An operator is one or more symbols (e.g. `#`, `*`, `%`, etc...) that run a method.
Under the hood, all operators run a method from the left operand, with the right as the argument to the method
### Comparison
a Comparison operator checks if the two values on each side and returns a bool
here are the comparison operators and what they do:
```python
x == y # Equality comparison. Checks if x is Equal to y, returns true if it is.
x === y # Percise Equality comparison. Checks if x is Exactly y, that means they need to have all exact same values, includes name.
x ~= y # Weak Equality comparison. Checks if x is almost Equal to y, ignores decimal number percition.
x != y # Not Equal comparison. Checks if x is Not Equal to y, returns reversed from normal Equality comparison
x !== y # Percise Not Equal comparison. Checks if x is Not Exactly y. returns reversed from normal Percise Equality comparison
x ~!= y # Weak Not Equal comparison. Checks if x is Almost Not Equal to y. returns reversed from normal Weak Equality comparison.
x < y # Smaller then comparison. Checks if x is smaller then y, returns true if so.
x > y # Greater then comparison. Checks if x is greater then y, returns true if so.
x <= y # Smaller or Equal to comparison. Checks if x is smaller or equal to y. returns true if so.
x >= y # Greater or Equal to comparison. Checks if x is greater or equal to y. returns true if so.
```
### Arithmetic
Arithmetic operators do just that, arithmetic.
```python
x + y # Addition
x - y # Subtraction
x * y # Multiplication
x / y # Division
x % y # Modulus
x ** y # Raised to the Power
```
### Assignment
Assignment operators are operators that set one value (the left most) to another value (the right most).
```python
x = y # Assign
x += y # Increase with
x -= y # Reduce by
x *= y # Multiply with
x /= y # Divide by
x **= y # with the Power of
x %= y # Modulus by
```
### Concatenation
The concatenation operator (`++`) joins two values of same type into one.
```python
print("foo"++"bar") #output: foobar
print(31++41) #output: 3141
print(3.4++1.1) #output: 31.41
print([3]++[2, 5]) #output: [3, 2, 5]
```

Under the hood, `++` calls the `__concat()` method left of the operand, with the right as the input,
meaning you can define custom concatenation for your own classes.
For all built in types, concatenation will always return the same type as the inputs.

> [!NOTE]
> Currently concatenation between two floats is a little weird and will either get removed or changed in the future,
> right now what it does is it takes the whole numbers and concatenates them and then takes the decimals and concatenates them.
> I.e. It works like the decimal point is just a separator between two different integers that get concatenated.
> 
> Any and all recommendations surrounding this are more than welcome!
## Control flow
### Conditional
Sometimes you want to only run some code depending on some condition. Conditions are a `bool` value used in different ways
#### if/else
`if` is a keyword consisting of two parts, the condition and the code. `if` is structured like `if {condition} {code}` (the squiggly braces are not used in real code), and it runs the `{code}` if the `{condition}` is `true`.
Code example:
```lua
if true print("Hello World!")
```

As you see, all you really need is the condition and statement/code. This example isn't so useful, since the `{condition}` is set to the constant `true`, that means the code after `{condition}` will always run, there is no need for that if statement.
here is a better use of the if statement
```python
if (input("what food do you like? ") == "hamburger") print("me too")
```

in this example you see that I have the condition inside two parentheses. Unlike many languages, it's not necessary for the statement to work, but highly recommended if you want more readable code. since else its hard to distinguish between the condition and code.

if you want to run multiple lines with the if keyword, you can surround the code in a `do` and `end`. think of them as opening and closing brackets, and for people who haven't used a language that uses them before, think of the `do` keyword as telling the `if` keyword to keep running code until the corresponding `end` keyword is reached.
```lua
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
#### try/except
The `try` and `except` are usefull when running code where errors might happen, and you don't want the code to stop because of it.
The `try` keyword is not structured exactly like the other conditionals. Instead of having a condition and code field, it only has a code field, so its structured like `try {code}`.
The `except` keyword is structured like normal conditional though, it is like 
Code example:
```python
try print("hello world!") #output: hello world!

try do raise TypeError("something went wrong!") end
except print("error alert!") #output: error alert!
print("no exit") #(this will print, even if there is a raise right above) output: no exit
```

if you want the error that occurred you can use [[#Variable Binding with `as`]], it can not be used on the `try` keyword, but for the `except` keyword it can
### Loops
Sometimes you might want to do something over a bunch of revisions, doing the same thing over and over. That's where loops are useful, they let you repeat one thing over and over until a [condition](#Conditional) is met.
#### While loop
A while loop runs the designated code whilst the condition is true, its structured like an if statement, like this `while {condition} {code}`, and for each repetition of the code it checks the condition, looking if it still is `true`.
```lua
while true print("hello world!")
```
this will print `hello world!` for infinity until the program is terminated.
#### For loop
A for loop is used to iterate through some elements in a `dict`/`list`. It's structured like `for {elements} {code}`. it works via getting the `__iter()` function of the `{elements}`, all built in types has this function and they always return a `list` or `dict` containing a value (and in the case of a dict there is a key linking to that value). it will not give any form of way of knowing what iteration its currently on, nor what value the current iteration has, that makes it good for loops with specific iterations, where the value isn't needed:
```lua
for range(10) do
	print("this will print 10 times!")
end
```

if you want to get the current value, you can use the `as` keyword, it puts the current value in the specified variable. here is more information about [[#Variable Binding with `as`]]
```lua
for range(10) as i do
	print(i)
end
```


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
```lua
var a

if a do
	print(a)
end
```
and...
```lua
if none do
	print(none)
end
```
also use the same resources

but, if a variable isn't declared with a value, and gets one later in the script, it's value will be set to `none`, instead of being replaced. That means...
```lua
var a

if a do
	print(a)
else do
	a = "hello world!"
end
```
and...
```lua
var a = none

if a do
	print(a)
else do
	a = "hello world!"
end
```
## Variable Binding with `as`
The `as` keyword captures values from expressions into variables
### In for loops
`as` is really useful in for loops, since it can get the current iterations value and put it in a useable variable, examples:
```python
for range(10) as i print(i)
for my_dict as (key, value) print(f"{key}: {value}")
```
In this code, the first `for` loop will loop 10 times and each time the `i` variable will be set to the new value in the given list,
and as for the dict, I don't know how to actually do it yet, but right now I'll just say that for more then one variable you have to put them in parenthesis.
### In try/except
it can be used to get the error that occurred in the `except` part, 
or in the case of it not getting an error, you can the the returned value of the function/code ran.
Examples:
```python
func test_code() do return "hello from function! no problem here" end

try test_code() as result
print(result) #output: hello from function! no problem here

try do
	var a = 2
	var b = 5
	var c = 7
	return a + b + c
end as result
print(result) # 5

try do #malicious code
	raise ValueError("this is an error")
end
except as error do
	print(f"got this error: {error}") #output: got this error: ValueError: this is an error
end
```

# Dictionary of all keywords
`do`/`end`
acts like a "code block" that groups together lines of code. Its used in situations where you can only use one line of code, like `if` or `while` statements

`if`
runs the code after the condition

`else`
always used after an `if` statement, runs the code if the `if` statements condition was false.

`do`+`end`
the `do` and `end` keywords are always used together, they act like how curly brackets work in many other languages work. they group up multiple lines of code so that its easier to read.

