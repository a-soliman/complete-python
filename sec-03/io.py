# Create a file and write into it.
file = open('test.txt', 'w+')
file.write('Hello, this is a test')
file.close()

# Open and read
file = open('test.txt', 'r')
content = file.read()
file.seek(0)
content_list = file.readlines()
file.close()

print(content)
print(content_list)


# Best Practice
with open('test.txt') as new_file:
    contents = new_file.read()

    print(contents)


with open('test.txt', 'w+') as new_file:
    new_file.write('This is a new appended line')
    print(new_file.read())