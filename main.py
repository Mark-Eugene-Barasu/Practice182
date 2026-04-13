
# list
my_list = [1, 2, 3, 4, 5]
print(my_list)

print(my_list[0])  # Accessing the first element
print(my_list[2])  # Accessing the third element
print(my_list[-1])  # Accessing the last element
print(my_list[-3])  # Accessing the third element from the end


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())  # Accessing the first element
print(bicycles[1].title())  # Accessing the second element
print(bicycles[2].title())  # Accessing the third element
print(bicycles[3].title())  # Accessing the fourth element
print(bicycles[-1].title())  # Accessing the last element
print(bicycles[-2].title())  # Accessing the second to last element

bicycles[3] = "mountain"
print(bicycles)

# Checking if the fourth element is equal to the last element
print(bicycles[3].title() == bicycles[-1].title())
print(bicycles[3].title() is bicycles[-1].title())
