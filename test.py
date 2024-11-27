# this is a test program going over all the main concepts in the python self study

'''
This is a test program 
This was made for the MIT emerging talent crash course
'''
# This is a function. It adds the variables x and y and returns an integer. the type after the -> is the return type of the function
def add(x, y): 
  return x + y
def sub(x, y) -> int:
  assert(isinstance(x, int) and isinstance(y, int))
  return x - y

# stores user input from the command line into the userInput variable
userInput = input("Put in a phrase that you want to be printed out: ")
# prints out the user input
# print(userInput)
# prints out true or false depending on what type user input is (str, int, float, bool)
# isinst = isinstance(userInput, str)
# print(isinst)

# An example of operators being used with conditional statements (== is equal to, != is not equal to)
'''
if userInput != "Hi":
  print(True)
elif userInput != "Bye":
  print("Bye Bye")
else:
  print(False)
# An example of string operations. .replace(x, y) (replaces all occurrences of x with y), len(), .strip(), .upper() (makes all letters in a string uppercase), .lower() (makes all letters in a string upper case)

stringexample = "abcdefg"
strexlen = len(stringexample)
print(stringexample)
changedexample = stringexample.replace("cde", "")
chexlen = len(changedexample)
print(changedexample)
print(add(strexlen, chexlen))
print(sub(strexlen, chexlen))
print(add(stringexample, changedexample))
# print(sub(stringexample, changedexample)) use this to test the assertion error


# An example of comparisons of integers using the greater than/less than etc.
intvar = 10

if intvar < 10:
  print(True)
elif intvar > 10:
  print(False)
else:
  print("nothing")
'''

# for i in range(5):
# print(i)

list = []
list2 = []

j = 1

while(len(list2) < 10):
  list2.append(j)
  j = j + 1
  
print(list2[0])
list2.insert(0, 0)
print(list2[0])


for i in range(len(userInput)):
  list.append(userInput[i])
# the difference between append and insert is that append adds an element at the end of the list while insert needs a specified index to add at (it then shifts all elements to the right when adding to a location)  
print(list)

for i in range(len(list)):
  if i < len(list) - 1:
    print(userInput[i], end = "")
  else:
    print(userInput[i])

for i in range(20):
  pass
