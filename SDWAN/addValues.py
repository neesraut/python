# from add import Add


# p1 = Add('anx', 'bp')
# print(p1.greeting())

#comment here
#print("Hello , World")
#x, y, z = 2, 3, 4
#print(x)

from DataTypes import DataTypes
listA = ["Apple", "Orange", "Mango"]

dt = DataTypes(listA)
print("First element is: "+ dt.list[0])

print(dt.list[0:2])
dt.list[0]="Watermelon"
print(dt.list)

for eachFruit in dt.list:
    print("The elements in dt list= " + eachFruit)

if "apple" in dt.list:
    print("yes the apple in list")
else:
    print("No apple")
#using index in for loop

