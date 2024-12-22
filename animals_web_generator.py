import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Load the animals data
animals_data = load_data('animals_data.json')

# Iterate through the animals and print the required fields
for animal in animals_data:
    if "name" in animal:
        print(f"Name: {animal['name']}")
    if "diet" in animal:
        print(f"Diet: {animal['diet']}")
    if "locations" in animal and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")
    if "type" in animal:
        print(f"Type: {animal['type']}")
    print()  # Print a blank line for better readability
