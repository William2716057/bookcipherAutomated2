import random

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) > 0:
            return user_input
        print("Please enter at least one character.")

def find_char(text, characters):
    results = {char: [] for char in characters}
    lines = text.split('\n')
    
    for line_number, line in enumerate(lines, start=1):
        for index, char in enumerate(line):
            if char in characters:
                results[char].append((line_number, index))
                
    return results

plaintext = get_valid_input("Enter one or more characters: ")


with open("sample.txt", "r") as file:
    text = file.read()
    
#text = """fasdfgadfdga
#sdfgsfdghsaaafg"""

positions = find_char(text, plaintext)

for char, pos_list in positions.items():
    if pos_list:
        random_position = random.choice(pos_list)
        line_number, index = random_position
        print(f"{line_number}:{index}")
    else:
        print(f"'{char}' not found in the text.")