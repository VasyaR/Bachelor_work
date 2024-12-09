# Open the file and read its content
with open("kkanji_classes_distribution_sorted.txt", "r") as file:
    lines = file.readlines()

# Initialize counters
sum_first_300 = 0
sum_remaining = 0

# Iterate through the lines
for idx, line in enumerate(lines):
    # Split the line into class name and sample amount
    class_name, sample_amount = line.split()
    sample_amount = int(sample_amount)
    
    if idx < 300:
        # Add to the first 300 classes sum
        sum_first_300 += sample_amount
    else:
        # Add to the remaining classes sum
        sum_remaining += sample_amount

# Print the results
print(f"Sum of samples in the first 300 classes: {sum_first_300}")
print(f"Sum of samples in the remaining classes: {sum_remaining}")
