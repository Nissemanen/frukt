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

as you see, unlike many other languages with comment blocks, these open and closing "symbols" are symmetrical. an example of a unsymmetrical comment block are `/*` and `*/`. you can think of a man opening a scroll
![[medieval-man-holding-scroll-isolated-260nw-231944920.webp]]

## Types
### Integer
an integer is a whole, positive or negative number, such as 2, 0 or -14. in code its name is `int`

## Declarations 
### Variables
To declare a variable you use the keyword `var`, then assign a value to it with the equals sign
```
var greeting = "Hello!"
```

> [!NOTE]
> a variable doesn't need to get declared with a value, if it doesn't have one, it wont get declared until it gets a value later in the program. If the variable is used before it gets a value or if it never gets a value in local space, it gets declared with a value of `none`
> you can find more info under
### Constants
you can declare a constant with the `const` keyword. a constant is like a variable but it cant be changed
```
const constant_var = "This wont Change!"
```

> [!NOTE]
> unlike many languages with constants, you can declare a constant without a value.
> when a constant is declared without a value it becomes a `none` type.
> its recommended not to do this since constants don't have the same treatment as normal variables when undefined. i.e. it gets a space in memory as soon as its declared
### Functions
to define functions, use the `func` keyword
```
func greet(name) do
	print(f"Hello {name}!")
end
```
### Type Declaration
everything that can have/return a type can be specified (eg variables since they can be a type and functions since they can return types). you do this with a colon
```
var a: int = 0 # this means that "a" is of type int and wont change
var b := true # this means that "b" is of the initial values type, in this case it'a a bool

func echo(thing : str) : str do # this is a function that takes a string argument and returns a string
	retrun thing
end
```


# Explanations
here you'll find in depth explanations on how stuff works, and when/why to use stuff.
## Variable usage
### Undeclared variables and constants
its not always guaranteed that you have something to save yet, you might know that you need a variable for something, just that you don't know it yet. That's a place where you would want to use an undeclared variable, or rather define a variable without a value. So that you later on can give it one

under the hood, a undefined variable doesn't actually exist. What that means is that variables without any value on declaration doesn't exist, that means...
```
var a
a = "hello world!"
```
and...
```
var a = "hello world!"
```
use the exact same resources.

if a variable never get a value it will be replaced with `none`. That means...
```
var a

if a do
	print(a)
end
```
and...
```
if none do
	print(none)
end
```
also use the same resources

but, if a variable isn't declared with a value, and gets one later in the script, it's value will be set to `none`, instead of being replaced. That means...
```
var a

if a do
	print(a)
else do
	a = "hello world!"
end
```
and...
```
var a = none

if a do
	print(a)
else do
	a = "hello world!"
end
```


# Dictionary of all keywords
`if`
runs code in-between the nearest `do` and `end`/`else` keywords if the statement after the `if` keyword is true

`else`
always comes after an `if` statement, runs the code in-between the nearest `do` and `end`/`else` keywords if the `if` statement above it is false

`do`


`end`

