# with open("myfile.txt") as file:
#     lines = file.readlines()
#     lines = [line.rstrip() for line in lines]


# open the data file
file = open("myfile.txt")
# read the file as a list
data = file.readlines()


# close the file
file.close()
print(data)
print("Line{}: {}".format(line.strip()))
