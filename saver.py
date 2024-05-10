import json

def save_to_json(file_path, data):
    # Save dictionary to JSON file
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)