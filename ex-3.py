#establishing the list numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
#slicing the list
print("first five elements of the list is :",numbers[0,5])
#using for loop to print the elements of the list
for i in numbers :
  print(i)
#List comprehension
squares = [x**2 for x in numbers]
print(squares)
