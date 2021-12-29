##### Write a program that prints out all the elements of the list that are less than 5
a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
c = []
for i in range(len(a)):
    if a[i] < 5:
        c.append(a[i])
print(c)
##### Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
number= int(input("Enter a number: "))
for i in range(len(a)):
    if a[i] < number:
        b.append(a[i])
print(b)


