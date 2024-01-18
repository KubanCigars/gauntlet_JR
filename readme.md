<h1> Hello and welcome! </h1>

---

This is a python gauntlet, whoever completes the series of python challenges first will be entered into a second set of ranking where I will test the code's performance and overall structure.

Each task will have a hint or piece of code that will help you in solving it but I recommend learning how to google code solutions, [w3schools](google.com) is a great learning tool for novices :D

There is no "right" way to code, especially in python. So long as your code is readable and not incredibly slow its good code!

_My DMs are always open for advice and support_

<details>
<summary>
Click me :3
</summary>
> `:D` appears as a smiley!
</details>

---

<h2> Getting started </h2>
I personally recommend getting:

[IDLE: Windows](https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe)
[IDLE: All downloads](https://www.python.org/downloads/release/python-3121/)
[VSCode: All downloads](https://code.visualstudio.com/download)
This is a barebones python IDE developed by the python foundation with all python docs included inapp!

However, if you want a linter (autocomplete), VSCode and PyCharm community edition are great IDEs to use.

---
<h3> Tasks </h3>

_`print("hello world")`_

<h6> Task 1: My 'hello world'</h6>

- Ask the user to input two numbers
- Return the sum of the numbers IF the former > the latter

<details>
<summary>
Hints for task:
</summary>

> Use int(input()) and print()
</details>

<br />

<h6> Task 2: Fruit loops</h6>

- Write a function that takes any number of number inputs, meaning integer and float types
- Return the max value of these numbers

<details>
<summary>
Hints for task:
</summary>

> Use a while loop, a for loop and a list!

```py
list = []
inp = float(input())
while inp != -1:
for value in range(start, end, jump):
```
</details>

<br />

<h6> Task 3: Introduction to functions</h6>

- Create a function that takes two integer inputs
- Return the power of each, so x ** y and y ** x

<details>
<summary>
Hints for task:
</summary>

```py
def func(input_parameters):
    # Code
    return
```
</details>

<br />

Great! Now we have a basic understanding of the majority of the content that is used in the structured programming labs, now its time to link everything together.

Wait...
I forgot something

erm

FILE HANDLING!
Python has two methods to open files, the good way and the bad way!
<br />

<h6> Task 4: File handling</h6>

- Create a file
- Write to a file
- Read a file
- Append to a file

<details>
<summary>
Hints for task:
</summary>

```py
a = file.open("text.txt", "r")
b = a.read()
a.close()
# Bad and stinky
with open("text.txt", "r") as file:
    # for line in file
    # b = a.read()
# good and will close the file for you outside of the loop!
```
</details>

<br />

<h6> Task 5: Classes</h6>

- I will keep this brief
- Make a class named "Person"
    - This person will have a name and age variable
    - Case sensitive
- Add a function for setting the age of the person
- Add a function for getting the name of the person
<details>
<summary>
Hints for task:
</summary>

Good luck `:P`
</details>

<br />

Final one I promise
This will require the power of google (w3schools <3)

I will also have solutions posted for all of these \^_\^

<br />

<h6> Task 999: Calculator</h6>

_SHOCK AND HORROR - a viable github project!_

- Write a calculator
- This will loop until an exit code is given
- This will take a string input 
- This will call a function with your input
- This function will split the input and cast the numbers [cast](https://www.w3schools.com/python/python_casting.asp) to a float
- This can be done with if statements or error handling
- This will output the result
- This calculator will support:
    - 2 digit arithmetic and logic
    - All arithmetic operations:
        - \+ \- * ** / // %
    - All logic operations:
        - < > == != >= <= [is]()



<details>
<summary>
Hints for task:
</summary>
Have fun, plan it out, w3 has what you need (my DMs are always open, too)
</details>

# Happy coding, losers!