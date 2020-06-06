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
