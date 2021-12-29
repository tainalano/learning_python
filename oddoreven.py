Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
num= int(input("Enter a number: "))
mod = int(num % 2)
if mod > 0:
    print ("You picked an odd number")
else :
    print ("You picked an even number")

## for decimals numbers also ##
num= float(input("Enter a number: "))
mod = float(num % 2)
if mod > 0:
    print ("you picked an odd number")
else :
    print ("You picked an even number")
