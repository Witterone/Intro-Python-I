# Write a function is_even that will return true if the passed-in number is even.

def is_even (x):
    if x%2==0:
        return True
    else:
        return False
#%%
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
#%%
def printer(y):
    if is_even(y)==True:
        return print("Even!")
    else:
        return print("Odd")
printer(num)
