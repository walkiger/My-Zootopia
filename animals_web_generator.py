import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Serializes a single animal object to HTML format."""
    output = '<li class="cards__item">\n'
    if "name" in animal:
        output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += "<p class='card__text'>\n"
    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    if "locations" in animal and animal["locations"]:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    output += "</p></li>\n"
    return output


def generate_animal_info(animals_data):
    """Generates a string with the animal information in HTML format."""
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    # Load the animals data
    animals_data = load_data('animals_data.json')

    # Generate the animal information string
    animals_info = generate_animal_info(animals_data)

    # Read the template content
    with open('animals_template.html', 'r') as file:
        template_content = file.read()

    # Replace the placeholder with the animal information
    html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as file:
        file.write(html_content)

    print("HTML file generated successfully.")


if __name__ == "__main__":
    main()
