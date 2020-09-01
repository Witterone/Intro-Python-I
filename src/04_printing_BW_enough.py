"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %2d, y is %3.2f, z is %s"%{10,2.24552,z})


#%%
# Use the 'format' string method to print the same thing
print("x is {:-2}, y is {:3.3}, z is {:}".format(x,y,z))

#%%
# Finally, print the same thing using an f-string
print(f"x is {x}, y is {'%s'%float('%.3g' %y)}, z is {z}")