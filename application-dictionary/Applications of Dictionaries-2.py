#22.	Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
dictionary={"a":10,"b":12,"c":14,"d":16}

#a built-in function that allows you to access the value of an item associated with the specified key.
print(f"The dictionary is {dictionary}")
max_num=max(dictionary,key=dictionary.get)

print(f"\n\t\t\tThe  value of {max_num} is maximum in your dictionary  ")


