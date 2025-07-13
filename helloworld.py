a = False
b = "Str"
c = 3.1234
print(type(a))

a_list = [3, 5, 6, 12]
new_list = [x * 3 for x in a_list]
print(new_list) 
print(a_list)
new_list2 = [False if x%2 else True for x in a_list]
print(new_list2) 

look = "Look at me!" 
now = " NOW" 
print(look[4])
print("\n\n")
x = 10
print(x)
print("Hello World!")