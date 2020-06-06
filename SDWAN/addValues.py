"""

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
print(len(dt.list))

dt.list.append("Pineapple")
print(dt.list)

dt.list.insert(1, "AddedFruit")
print(dt.list)

#copiedList = dt.list.copy()
copiedList = dt.list
#dt.list.clear()
print(copiedList)
del dt.list

print(copiedList)
#using index
"""
"""
from DataTypes import DataTypes

tupleA = ("Me", "You", "US")
dt1 = DataTypes.tuple(tupleA)
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
thisdict["year"] = 2018
print(thisdict)

for x in thisdict.values():
    #print(thisdict[x])
    print(x)


for k,v in thisdict.items():
    print(k,v)

print(len(thisdict))