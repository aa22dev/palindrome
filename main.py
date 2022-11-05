# stack is used to implement this program because stack outputs the last element added into the stack first and first element added into the stack at last

from collections import deque # import double ended queue from collections library
string = input("Enter any string: ") # take string as input from user
rev = "" # variable for storing reverse of entered string
stack = deque() # intializing stack using double ended queue
for ch in string: # loop until end of string is reached
    stack.append(ch) # append first character in stack

for i in range(0, len(stack)): # loop until end of stack is reached
    rev = rev + stack.pop() # pop from stack and store it in variable

if rev.lower() == string.lower(): # if reversed of entered string is equal to entered string
    print("Entered string is palindrome!") # print string is palindrome
else:
    print("Entered string is not palindrome!") # print string is not palindrome
