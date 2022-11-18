#question 3 ieee (COMPLETE)
dict1 = {}
x = int(input("enter number of entries you want : "))
for i in range(x):
    keys_inp = input("enter key : ")
    values_inp = input("enter value : ")
    dict1[keys_inp] = values_inp
asc_dict_keys = sorted(dict1)
asc_dict_values = sorted(dict1.values())

print(dict1)
print(asc_dict_keys)
print(asc_dict_values)