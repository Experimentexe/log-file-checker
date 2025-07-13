import os
import json
import sys

def create_hierarchy(root_dir):
    hierarchy = {}
    hierarchy[root_dir] = traverse_directory(root_dir)
    return hierarchy

def traverse_directory(directory):
    contents = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            contents.append({"type": "File", "name": item})
        elif os.path.isdir(item_path):
            contents.append({"type": "Dir", "name": item, "contents": traverse_directory(item_path)})
        else:
            contents.append({"type": "Unknown", "name": item})
    return contents

def save_to_json(data):
    with open('struct.dat', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_directory = sys.argv[1]
    
    if not os.path.isdir(root_directory):
        print("Error: Root directory does not exist.")
        sys.exit(1)
    
    hierarchy = create_hierarchy(root_directory)
    save_to_json(hierarchy)
    print("Hierarchy saved to struct.dat")
