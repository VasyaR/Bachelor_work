import os
import shutil
from collections import defaultdict
from tqdm import tqdm

# Paths
main_folder = "/mnt/d/Bachelor_work/data_for_model/kkanji2"
output_folder = "/mnt/d/Bachelor_work/data_for_model/kkanji2_known_unknown"
known_folder = os.path.join(output_folder, "known")
unknown_folder = os.path.join(output_folder, "unknown")

# Ensure output directories exist
os.makedirs(known_folder, exist_ok=True)
os.makedirs(unknown_folder, exist_ok=True)

# I need 49000 samples for the known classes. 49000 / 300 = 163.33333333333334. 163 * 300 = 48900.
# 122 classes have less than 163 samples, and I will take only 100 from them. So 122 * 63 = 7686 sample. To get 49000 samples I need 100 more, so 7786.
# I will take 163 samples from the remaining 178 classes. If class has more than 163 samples, I will take the first 163 samples
# and the rest of them substracting remaining from 7786. If 7786 becomes 0, I will take 163 samples from the remaining classes
# that has 163 samples or more, otherwise I will take the first 100 samples from the remaining classes.

top_178_of_top_300_classes = defaultdict(int)
bottom_122_of_top_300_classes = defaultdict(int)
unknown_classes = defaultdict(int)

# Open the file and read its content
with open("kkanji_classes_distribution_sorted.txt", "r") as file:
    lines = file.readlines()

# Iterate through the lines
for idx, line in enumerate(lines):
    # Split the line into class name and sample amount
    class_name, sample_amount = line.split()
    sample_amount = int(sample_amount)

    if idx < 178:
        top_178_of_top_300_classes[class_name] = sample_amount
    
    elif idx >= 178 and idx < 300:
        bottom_122_of_top_300_classes[class_name] = sample_amount

    # There are 3832 classes in total. I don't need last 31 classes so I will take 3801 classes.
    elif idx >= 300 and idx < 3801:
        unknown_classes[class_name] = sample_amount

remaining_samples = 7786

"""
# Copy the samples to known and unknown folders
for class_name, sample_amount in tqdm(top_178_of_top_300_classes.items(), desc="Copying samples to the known folder1"):
    # Copy the samples to the known folder
    class_folder = os.path.join(main_folder, class_name)
    samples = os.listdir(class_folder)
    sapmle_amount = len(samples) - 163
    if remaining_samples == 0:
        for sample in samples[:163]:
            shutil.copy(os.path.join(class_folder, sample), os.path.join(known_folder, sample))
    elif remaining_samples - sample_amount >= 0:
        for sample in samples:
            shutil.copy(os.path.join(class_folder, sample), os.path.join(known_folder, sample))
        remaining_samples -= sample_amount
    else:
        for sample in samples[:163 + remaining_samples]:
            shutil.copy(os.path.join(class_folder, sample), os.path.join(known_folder, sample))
        remaining_samples = 0

for class_name, sample_amount in tqdm(bottom_122_of_top_300_classes.items(), desc="Copying samples to the known folder2"):
    # Copy the samples to the known folder
    class_folder = os.path.join(main_folder, class_name)
    samples = os.listdir(class_folder)
    for sample in samples[:100]:
        shutil.copy(os.path.join(class_folder, sample), os.path.join(known_folder, sample))

for class_name, sample_amount in tqdm(unknown_classes.items(), desc="Copying samples to the unknown folder"):
    # Copy the samples to the unknown folder
    class_folder = os.path.join(main_folder, class_name)
    samples = os.listdir(class_folder)
    for sample in samples:
        shutil.copy(os.path.join(class_folder, sample), os.path.join(unknown_folder, sample))
"""
remaining_samples = 652
for class_name, sample_amount in tqdm(top_178_of_top_300_classes.items(), desc="Copying samples to the known folder1"):
    # Copy the samples to the known folder
    class_folder = os.path.join(main_folder, class_name)
    samples = os.listdir(class_folder)
    if remaining_samples == 0:
        break
    else:
        for sample in samples:
            if os.path.exists(os.path.join(known_folder, sample)):
                continue
            shutil.copy(os.path.join(class_folder, sample), os.path.join(known_folder, sample))
            remaining_samples -= 1
            if remaining_samples == 0:
                break