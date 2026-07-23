#List collection is ordered, meaning a list of elements maintain the insertion order of the elements
#Lists are mutable, meaning we can add or remove elements of a list after declaration
a = 10
b = "Sarang"
c = "Sambharia"
d = True

#Creating a list
list = ["sarang", "santosh","mahima","himani"]
print(list)

#Updating a value at a specific index in a list
list[0] = "sambharia"
print(list)

#inserting a value at a specific index in a list
list.insert(0,"suresh")
print(list)

#inserting a value at the end of the list
list.append("Family")
print(list)

#deleting a specific index in a list
del list[0]
print(list)