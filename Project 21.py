test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:", test_dict)

val = int(input("Enter the value you want to check the frequency of: "))

freq = list(test_dict.values()).count(val)

print("The frequency of", val, "is:", freq)
