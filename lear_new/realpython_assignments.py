"""input = input("Enter some text:")
newtext1 = input .replace("a","4").replace("b","8").replace("c","9").replace("e","3")

print(newtext1)

for i in range(2,11):
    print(i)


def invest(principal, interest, time):
    amount = []
    amt = principal
    for i in range(1, time+1):
        amt = amt * (1 + interest)
        amount.append(amt)
        print(amount)


invest(100, .05, 8)
invest(2000, .025, 5)


def addUnderscores(word):
  new_word = "_"
  for i in range(0, len(word)):
   new_word = new_word + word[i] + "_"
  return new_word

phrase = "hello!"
print(addUnderscores(phrase))

print(42 * True + False)
print(False * 2 - 3,"\n ",True + 0.2 / True)
print("good" != "Good",123 == "123")
print(("good" != "bad") or False)
print(("good" != "Good") and not (1 == 1))

for i in range(4):
    print("*"* (4-i))
for i in range(4):
    print("*"* (i+1))
for i in (1,3,5,7,5,3,1):
    print("*"*i)

l = 3
w = 45
for i in range(l):
     print("*" * w)

name = "Rihana"
for i in range(1,101):
    print(f"{i} -- {name}")
for char in range(len(name)):
    print(name[char],end="")
    print(name[char])
    n=20
for i in range(1,n+1):
    print(f"{i}--{i*i}")

for i in range(8,90,3):
       print(f" {i} ",end = '')

l = 3
w = 10
for row in range(l):  # Loop l times for l rows
    if row == 0 or row == l-1:  # For the first and last row, print solid box
        print('*' * w)
    else:  # For the middle rows, print hollow center
        print('*' + ' ' * (w-2) + '*')
print()  # Print a newline to end the line

# Ask the user to enter a number
x = int(input("Enter a number: "))

# Use a loop to print the multiples of x separated by three dashes
for i in range(1, 6):
    multiple = x * i
    if i != 1:  # Skip the first iteration
        print(f"---{multiple}", end="")
    else:
        print(multiple, end="")
print()  # Print a newline to end the line
"""
#size = int(input("Enter the size of the letter A: "))
size = 5
# Print the top part of the letter A
for i in range(size):
    spaces = size - i - 1
    stars = 2 * i + 1
    if i == 1:
        print(" " * spaces + "*" + " " * (i * 2 - 1) + "*")
    else:
        print(" " * spaces + "*" + " " * (i * 2 - 1) + "*")

# Print the bottom part of the letter A
print(" " * (size - 1) + "*" + " " * (size - 1))

#size = int(input("Enter the size of the letter A: "))
size = 5
# Print the top part of the letter A
for i in range(size):
    spaces = size - i - 1
    stars = 2 * i + 1
    if i == 0:
        print(" " * spaces + "*" + " " * spaces)
    else:
        print(" " * spaces + "*" + " " * (i * 2 - 1) + "*")

# Print the bottom part of the letter A
for _ in range(size // 2):
    print(" " * (size - 1) + "*" + " " * (size - 1))

def print_giant_letter_a(size):
  """Prints a giant letter A to the console.

  Args:
    size: The size of the letter A.
  """

  for i in range(size):
    for j in range(size):
      if i == 0 or i == size - 1 or j == size // 2:
        print("*", end="")
      else:
        print(" ", end="")
    print()


def print_diamond_shape(height):
    """Prints  a diamond to the console.

     Args:
       height: The height of the diamond.
     """
    # Print the top half of the diamond
    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

    # Print the bottom half of the diamond
    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

def doubles(number):
    """
        Takes one number as its input and doubles
       that number three times using a loop, displaying each result on a separate
        line
        Args:
          Number: The number need to be doubled
    """
    for _ in range(3):
        number *= 2
        print(number)

if __name__ == "__main__":
  # Get the height of the diamond from the user.
  height = int(input("Enter the height of the diamond: "))

  # Print the the diamond .
  print_diamond_shape(height)

  # Get the size of the letter from the user.
  size = int(input("Enter the size of the letter A: "))

  # Print the giant letter A.
  print_giant_letter_a(size)

  # Test the function
  doubles(2)
