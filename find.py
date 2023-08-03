#
open('mames.txt', 'r').read().find('marshal')

fopen = open("mames.txt", mode = "r+")
fread = fopen.readlines()
x = input("Enter the name string: ")
for line in fread:
    if x in line: #print(line)

        f = open("test3.txt", "w")
        f.write("dldjjfbsdljf Python\n")
# in the above code‘\ n’ is next line which means in the text file it will write Hello Python and point the cursor to the next line
        f.write("89fsdff World")
        
    else:
        print ('word not found')

        f.close()
