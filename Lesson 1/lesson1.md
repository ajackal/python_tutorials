# Lesson 1 - Define a Function

```python
def print_hello_world():
    print "Hello World!"
  
print_hello_world()
```

The first line defines (def) the function named "print_hello_world" and it takes no arguments (). The next line is indented 4 spaces per Python's PEP8 and defines what the function does. Most text editors and IDEs will automatically turn a "tab" into four spaces. This function is going to use the built in module `print` to print the string "Hello World!" to the console. The last line actually calls the function; without this line the function will be defined but never called.
