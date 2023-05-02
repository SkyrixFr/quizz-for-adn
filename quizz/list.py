import json
from os import path

# Define the range of file numbers
start_number = 1
end_number = 280  # Update this to the last file number in your sequence

# Iterate over the range of file numbers using a for loop
for file_number in range(start_number, end_number + 1):
    # Generate the file name using the file number
    file_name = f"{path.realpath(path.dirname(__file__))}\openquizzdb_{file_number}.json"
    try:
        with open(file_name, 'rb') as file:
            # Load the JSON data from the file
            json_data = json.load(file)
            # Do something with the JSON data
            # For example, you can access the data using dictionary-like syntax
            print(file_name, str(json_data["catégorie-nom-slogan"]["fr"]["nom"]))
    except FileNotFoundError:
        pass

