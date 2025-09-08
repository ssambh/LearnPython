#dictionary is like a hashmap in java
#Dictionary elements are defined in {} with a : between the key and the value
#Only the String value/key is defined in double quotes("")
dict = {"name":"sarang","age":30,"goodguy":True}
#Value will be displayed if we provide the key
print(dict["age"])

#Creating an empty dictionary
dic = {}

#inserting values in a dictionary
dic["Name"] = "Sarang"
dic[30] = "Age"
print(dic)

#For printing all the key-value pairs
for a,b in dict.items():
    print(a,b)
