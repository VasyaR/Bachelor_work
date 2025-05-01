import os
import shutil
from collections import defaultdict
from tqdm import tqdm

# Paths
main_folder = "/mnt/d/Bachelor_work/data_for_model/kkanji2"
output_folder = "/mnt/d/Bachelor_work/data_for_model/kkanji2_known_unknown"
known_folder = os.path.join(output_folder, "known")
unknown_folder = os.path.join(output_folder, "unknown")

#Count number of files in known and unknown folders
known_files = 0
unknown_files = 0
for root, dirs, files in os.walk(known_folder):
    known_files += len(files)

for root, dirs, files in os.walk(unknown_folder):
    unknown_files += len(files)

print(f"Number of files in known folder: {known_files}")
print(f"Number of files in unknown folder: {unknown_files}")