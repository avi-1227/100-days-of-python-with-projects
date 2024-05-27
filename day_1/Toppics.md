# Day -1

What I have learned in Day-1 topics as mentioned below.

## Table of Contents
1. [print()](#print)
2. [\n](#\n)
3. [concatenation](#concatenation)
4. [input()](#input)
5. [variables](#variable)



## 1. print() Function
This function is generally use to print the statement in console
```bash
# Example for the use of print() function
print("Hello World")
print(2)
print("This is another sentence")

# Output will become as follows
Hello World
2
This is another sentence
```
## 2. Use of \n
It use to come for line break in sentence as mentioned above we saw if want to print multiple line we use every time print() function. But for that we also use "\n" 
```bash
# Example for the use of "\n"
print("Hello World\n2\nThis is another sentence")

# Output will be the same as above 
Hello World
2
This is another sentence
```

## 3. Concatenation
To concatenate or combine two strings we can use "+" operator
```bash
# Example
print("Hello"+"World")

# Output 
HelloWorld

# For Space we can use blank " " 
# Example
print("Hello"+" "+"World")

# Output 
Hello World
```

## 4. input() Function
To take input from user. This means that we are able to ask the user for the input
```bash
# Example
print("Hello, "+ input("Enter your name?:- "))

# When you run the file console will ask Your Name like as follows and when you enter your name your name will display 

Enter your name:- Your Name 

# Output 
Hello, Your Name
```

## 5. Variable
Variables are containers for storing data values.
```bash
# Example
name = input("Enter Your Name:- ")
print(name)

# We can use name variable anywhere in all code
# Output 
Your Name
```
Rules for python variable:-
- A variable name must start with a letter or underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscore (A-z, 0-9, and _)
- Variable names are case sensitive (age, Age and AGE are the different variable)
- A variable name cannot be any of the Python Keywords (like-print, input, sum etc..)

```bash
# Example
my_name = ""
myname = ""
_my_name = ""
my_name = ""
myName = "" 
```


