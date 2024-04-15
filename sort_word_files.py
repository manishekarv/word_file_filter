import os
import shutil

location = r"C:\Users\manv0219\Documents\Projects\vfhu\Designs\Phase 1"
import os

def print_docx_files(folder):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.docx'):
                print(os.path.join(root, file))
                count +=1
    print(count)

def move_docx_files(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.docx'):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_folder, file)
                try:
                    shutil.move(source_file_path, destination_file_path)
                except Exception as e:
                    print(e)
                print(f"Moved: {source_file_path} to {destination_file_path}")

source_folder_path = r"C:\Users\manv0219\Documents\Projects\vfhu\Designs\Phase 2.1"
destination_folder_path = r'C:\Users\manv0219\Documents\Projects\vfhu\Designs\Phase_2.1'

move_docx_files(source_folder_path, destination_folder_path)
