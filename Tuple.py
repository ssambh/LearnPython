#Tuple is similar to a list, but it is immutable.
#Tuples are an ordered collection, meaning they maintain the insertion order of the elements

user_tuple = ("Sarang","Sambharia")
print(user_tuple)

#Below line will throw an error as assignment is not allowed in a tuple.
#this also prevents for the tuple to be accidentally modified.
user_tuple[0] = "Sambharia"

#We can cast a tuple into list like below
user_list = list(user_tuple)
print(user_list)