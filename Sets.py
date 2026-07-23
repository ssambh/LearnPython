#Sets are the data structure similar to sets in java which cannot store duplicate elements
#Sets are a unordered collection, meaning a set doesn't maintain the insertion order unlike a list or a tuple
#We cannot access a specific item in a set as it is not ordered.
user_set = {1, 1, 2, 3, 3, 4, 5, 5, 6}
print(user_set)
#A set in python can store multiple data structures unlike Java
user_set = {1, 3, "sarang", 3.22, "sarang", 3.22, 99}
print(user_set)

#Although we cannot access specific elements in a set, we can access all the elements using a loop
for ele in user_set:
    print(ele)

#To add or remove elements in a set
user_set.add(123)
user_set.remove("sarang")
print(user_set)
#we can convert another data structure to set using set keyword
user_list = [1,3,2,4,5,62,1,4]
user_tuple = (3,2,4,1,5,3,6,4)
dictionary = {"name":"Sarang", "Age":30}

#While an output in set would seem like the elements are sorted, but it is not to rely upon.
print(set(user_list))
print(set(user_tuple))
print(set(dictionary))

#To cast back a set into a list, we can use the list method to do so.
print(list(set(user_list)))