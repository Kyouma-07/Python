squares = [x**2 for x in range(1, 6)]
print("List of Squares:", squares)

squares_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of Squares:", squares_dict)

squares_set = {x**2 for x in range(1, 6)}
print("Set of Squares:", squares_set)