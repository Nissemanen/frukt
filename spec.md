# **Frukt Specification v0.1**
## **1. Introduction**
Frukt is a simple scripting language made to test my (nissemanen) skills around programming, it is recommended not to use this language until it has a good reason to do so.

### Design goals:
- **Consistency**: keep the language as consistent as possible.
- **Readability**: code made by anyone should be easy to read and thus debug.
- **Easy to learn**: the language should as supportive to new programmers as professional ones.

## **2. Lexical Structure**
### **2.1** Character set
Frukt source code uses UTF-8 encoding natively, but supports the standard ASCII encoding to.

### **2.2** Comments and Whitespace
single line comments start with `#` and continue to the end of the line
comment blocks start with `#--` and continue to the next `#--`

Whitespaces characters (such as spaces, tabs, and newlines) are generally used to separate tokens for readability.
Except where required to separate tokens, whitespaces has no syntactic meaning and may appear freely between tokens.

**Line Terminators**
A line terminator is either:
- a newline character (`\n`),
- a carriage return (`\r`), or
- a carriage return followed by a newline (`\r\n`).
Line terminators may be used to indicate the end of a statement.

Statements are normally separated by either:
- a semicolon (`;`), or
- a line terminator.

### **2.3** Tokens
> [!NOTE]
> regular expression (regex) will be used in some places to make it clearer how something is defined
> regex will be defined with a code block starting and ending with a forwards slash, e.g. `/this is [Rr]eg([Ee]x|ular [Ee]xpresion)/`

**Identifier**: `/[A-Za-z_][A-Za-z0-9_]*/`
**Keywords**:
- **Conditional**: `if`, `else`, `try`, `except`, `match`
- **Loops**: `while`, `for`
- **Flow Control**: `break`, `continue`, `return`
- **Declaration**: `var`, `const`, `func`, `class`
- **Literals**: `true`, `false`, `none`
- **Code Blocks**: `do`, `end`
**Operators**:
- **Assignment**: `=`, `-=`, `+=`, `*=`, `/=`, `**=`, `%=`

that's it for now. I don't really know how to structure specifications in a good way so I just went as simple but detailed explanatory as possible