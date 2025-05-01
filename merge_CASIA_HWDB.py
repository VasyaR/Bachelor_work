import os
import shutil

def merge_directories(source_dirs, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for source_dir in source_dirs:
        for root, dirs, files in os.walk(source_dir):
            # Determine the relative path from the source directory
            rel_path = os.path.relpath(root, source_dir)
            dest_subdir = os.path.join(dest_dir, rel_path)

            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)

            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_subdir, file)

                # If the file already exists in the destination, rename it
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    new_dest_file = os.path.join(dest_subdir, f"{base}_{counter}{ext}")
                    while os.path.exists(new_dest_file):
                        counter += 1
                        new_dest_file = os.path.join(dest_subdir, f"{base}_{counter}{ext}")
                    dest_file = new_dest_file

                shutil.copy2(src_file, dest_file)

# Define source directories and destination directory
# source_dirs = ['/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.0Test', 
#                '/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.1Test',
#                 '/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.2Test']
# dest_dir = '/mnt/d/Bachelor_work/data_for_model/CASIA_HWDB/test'

# Define source directories and destination directory
# source_dirs = ['/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.0Train', 
#                '/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.1Train',
#                 '/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.2Train']
# dest_dir = '/mnt/d/Bachelor_work/data_for_model/CASIA_HWDB/train'

# Merge directories
# merge_directories(source_dirs, dest_dir)

# print(f"Directories {source_dirs} have been merged into {dest_dir}")