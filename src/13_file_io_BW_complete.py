"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

foo = open('foo.txt','r')

print(foo.read(-1))

foo.close()
#%%
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open("bar.txt",'w')

bar.write( """
This is an exercise in writing onto a text file.
I think this is interesting to do without modules.
Python has more power than I previously knew.
""")

bar.close()

rbar = open('bar.txt','r')

print(rbar.read(-1))

rbar.close()
