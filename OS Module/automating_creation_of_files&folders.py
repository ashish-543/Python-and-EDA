import os

number_of_folders = 5
number_of_files_per_folder = 10
extension = 'txt'

# First create a root folder then create the above mentioned folders and files inside root folder
os.makedirs('root', exist_ok = True)

base_directory = 'root'

for folder in range(1, number_of_folders + 1): # Range starts from 0 so for 5, the range is 0-4 i.e [)
    folder_name = f'folder_{folder}'
    folder_path = os.path.join(base_directory, folder_name) # root\folder_1
    os.makedirs(folder_path, exist_ok = True)

    # Now creating files
    for file in range(1, number_of_files_per_folder + 1):
        file_name = f'file_{file}'
        file_path = os.path.join(folder_path, file_name) # root\folder_1\file_1

        with open(f'{file_path}.{extension}', 'w'): # This creates the required files
            pass


# Now in the same , add a text folder_name -> file_name in each file

for folder in range(1, number_of_folders + 1):
    folder_name = f'folder_{folder}'
    folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(folder_path, exist_ok = True)

    for file in range(1, number_of_files_per_folder + 1):
        file_name = f'file_{file}'
        file_path  = os.path.join(folder_path, file_name)

        with open(f'{file_path}.{extension}', 'w') as f:
            f.write(f'{folder_name} -> {file_name}')

