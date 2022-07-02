# a flie object allows us to  use, access anc manipulate all the user accessible file.
# One can read write any such file. a file can be opened with a built-in function called open().
# This function takes in the file's address and the access_mode and returns a file object.

'''
syntax:
======
   file object = open(file name[, access_mode][,buffersize]

   r = opens a file for reading only
   rb = reading only in binary formant
   r+ = opens file for both reading and writing
   rb+ = opens a file for both reding and writing in binary format
   w = opens a file for writing only
   wb = open a file for writing only binary formant
   a = opens a file appending
   a+ = opens a file for appending in binary formant
   ab+ = opens a file for both appending and reading in bianary format

'''

# Writing  to file:
f=open("D:\Pyhon\hello.txt","w");
f.write("Python Programming");
f.close();


# Writing lines to file
lines=["Hello world .\n","Welcome to pyhon Programming.\n"]
g=open("D:\Pyhon\hello.txt","w")
g.writelies(lines);
g.close()

# Reading from a file
'''
readline() : Reads the characters starting from the current reading position upto a nnewline character

read(chars) : Reads the specified number of characters starting from the current position

readlines() : Reads all line until the end of file and returns a list object

'''
x= open("test.txt","~")
line=x.readline()
print(line)
x.close()