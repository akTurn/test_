with open('mames.txt') as file:
    contents = file.read()
    search_word = input("enter a name you want to search in file: ")
    if search_word in contents.split():
        f = open("userdata.txt", "w")

# Taking multiple inputs based on n:
       # for i in range(3):
        t = input("enter an age : ")
        t1 = input("enter an salary :")
        t2 = input("enter an phonenumebr :")

        f.write(str(t))
        f.write('\n')
        f.write(str(t1))
        f.write('\n')
        f.write(str(t2))

        f.close()
    else:
        print ('word not found')
