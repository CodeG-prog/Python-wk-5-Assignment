# opening files in python
# opening a file
file = open('test.txt', 'r')
# read the file
data = file.read()
print(data)
# Opening a pdf file in python
file = open('filename, 'rb'')
data = file.readlines() #Reads all the lines
print(data)
# closing the file
file.close()
# opening a file using with statement
with open('test.txt', 'r') as file:
    data = file.read()
    print(data)
# opening a file in write mode
file = open('test.txt', 'w')
# write data to the file
file.write('Hello World')
# closing the file
file.close()
# opening a file in append mode
file = open('test.txt', 'a')
# append data to the file
file.write('Hello World')
# closing the file
file.close()
# opening a file in binary mode
file = open('filename', 'rb')
# read the file
data = file.readlines() # Reads all the lines
print(data) # print data- binary data 
# closing the file
file.close()

# Error handling in file operations involves catching exceptions that may occur during file operations.
# This can be done using try and except blocks.
try: 
    # opening a file
    file = open('test.txt', 'r')
    # read the file
    data = file.read()
    print(data)
except FileNotFoundError:
    print('File not found. Please check the file name and path.')
    
# Advanced error handling in file operations involves using the finally block to ensure that the file is closed even if an exception occurs.
try:
    # opening a file
    file = open('test.txt', 'r')
    # read the file
    data = file.read()
    print(data)
except FileNotFoundError:
    print('File not found. Please check the file name and path.')
finally:
    # closing the file
    file.close()
# This ensures that the file is closed even if an exception occurs.
# Example of error handling in file operations
try:
    file = open('test.txt', 'r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print('File not found. Please check the file name and path.')
finally:
    file.close()
# This ensures that the file is closed even if an exception occurs.

