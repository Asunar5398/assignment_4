user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

more_data = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(more_data + "\n")

print("\nFinal contents of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
