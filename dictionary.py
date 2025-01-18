import requests
import sys
import os

# Function to fetch the definition of a word using the WordAPI
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        return definition
    else:
        return "Definition not found."

# Function to append word and definition to the definitions.md file
def append_to_markdown(word, definition):
    file_name = "definitions.md"
    
    # If the file doesn't exist, create it and add a header
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write("# Definitions\n\n")
    
    # Append the word and its definition to the file
    with open(file_name, 'a') as file:
        file.write(f"**{word}**: {definition}\n\n")

# Main function to get the word from the command line argument, fetch definition, and append to markdown
def main():
    if len(sys.argv) < 2:
        print("Please provide a word as an argument.")
        sys.exit(1)
    
    word = sys.argv[1]  # Get the word from the command line argument
    definition = get_definition(word)
    append_to_markdown(word, definition)
    print(f"Definition of '{word}' has been added to definitions.md")

if __name__ == "__main__":
    main()

