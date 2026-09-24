with open("input.txt", "r") as file:
    
    lines = file.readlines()

line_count = len(lines)

first_two_lines = lines[:2]

print("Total number of lines:", line_count)

print("\nFirst two lines:")
for line in first_two_lines:
    print(line.strip())

with open("output.txt", "w") as file:
    
    file.writelines(first_two_lines)

print("\nFirst two lines have been written to output.txt")
