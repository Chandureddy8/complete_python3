file_name = "my_first_file.txt"

with open(file_name, "w") as file_object:
    file_object.write("Hello file!\n")
    file_object.write("You're my favorite file!")