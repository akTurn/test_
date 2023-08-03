for letter in 'Python': # First Example
 if letter == 'h':
     continue
 print('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
 var = var -1
 if var == 5:
     continue
 print('Current variable value :', var)
print("Good bye!")


# ***************************** \n

for letter in 'Python':
 if letter == 'h':
     pass
 print('This is pass block')
 print('Current Letter :', letter)


 basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
 for f in sorted(basket):
     print(f)




 print("\n")
for i in reversed(range(1, 10, 2)):
 print(i)
