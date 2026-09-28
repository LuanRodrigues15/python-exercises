with open("python-exercises/python_100_days_of_code/my_solutions/day_24/class_practice/my_file.txt") as file:
    contents = file.read()
    print(contents)


# with open("python-exercises/python_100_days_of_code/my_solutions/day_24/class_practice/my_file.txt", mode="w") as file:
#     file.write("New text.")

# with open("python-exercises/python_100_days_of_code/my_solutions/day_24/class_practice/my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# Creating a new file that does not exist
with open("python-exercises/python_100_days_of_code/my_solutions/day_24/class_practice/new_file.txt", mode="w") as file:
    file.write("New text.")

