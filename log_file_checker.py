import os

def find_files(filename, search_path):
    result = []
    filename_lower = filename.lower()
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == filename_lower:
                full_path = os.path.join(root, file)

                result.append(full_path)
                return result
    return 'Error'

def reading_file(filename):
    counter = 0
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line_lower = line.lower()
                if "failed" in line_lower or "error" in line_lower:
                    counter += 1
        return f'This log has a total of {counter} failed/error lines.'
    except Exception as e:
        return f"Could not read file {filename}: {e}"


search_dir = r'D:\\'
file_to_find = input("Please enter the file name with the extension (Ex. filename.txt): ").strip()

found_files = find_files(file_to_find, search_dir)

if found_files:
    for file_path in found_files:
        print(f'This file is located at: "{file_path}"\n')
        print(reading_file(file_path))
else:
    print("Error: File not found.")
