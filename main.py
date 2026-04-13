# creating a list of car brands
cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"]

# Accessing the first element using index position 0
first_car = cars[0]
print(
    f"The first car brand is: {first_car}")

cars.append("Audi")
print(f"Updated list of car brands: {cars}")

# Removing the last element from the list
removed_car = cars.pop()  # Removing the last car brand (Audi)
print(f"Updated list of car brands: {cars}")
print(f"Removed car brand: {removed_car}")
removed_car = cars.pop(2)  # Removing the car brand at index position 2 (Ford)
print(f"Updated list of car brands: {cars}")
print(f"Removed car brand: {removed_car}")
