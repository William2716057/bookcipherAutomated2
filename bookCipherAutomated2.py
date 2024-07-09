
import random

plaintext = input("Enter text: ")

def find_char(text):
    results = []
    lines = text.split('\n')
    
    for line_number, line in enumerate(lines, start=1):
        for index, char in enumerate(line):
            if char == plaintext:
                results.append((line_number, index))
                
    return results

text = """fasdfgadfdga
sdfgsfdghsaaafg"""

positions = find_char(text)

if positions:
    random_position = random.choice(positions)
    line_number, index = random_position
    print(f"{line_number}: {index}")
else:
    print("Not found in the text.")