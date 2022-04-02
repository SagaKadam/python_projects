var1 = 5
var2 = 6

print("Enter the number")
var3 = int(input())

if var3 > var2:
    print("greater")
elif var3 == var2:
    print("equal")
else:
    print("lesser")

list = [1, 2, 3, 4]
print(2 in list)
if 2 in list:
    print("It's in the list.")

print(7 not in list)
if 7 not in list:
    print("It's not in the list")