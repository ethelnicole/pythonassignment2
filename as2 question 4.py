import random

# Generate a list of 5 random floating-point numbers between 0 and 10
# random.uniform(a, b) yields a random floating-point number between a and b
random_numbers = [random.uniform(0, 10) for _ in range(5)]

# Print the generated list
print("Generated List:", random_numbers)

# Calculate minimum and maximum values using built-in functions
min_value = min(random_numbers)
max_value = max(random_numbers)

# Print the results
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
