
# Using readline()
file1 = open('myfile.txt', 'r')
count = 0
while True:
	count += 1
	# Get next line from file
	line = file1.readline()
	if not line:
		break
	print("{}: {}".format(count, line.strip()))
file1.close()
