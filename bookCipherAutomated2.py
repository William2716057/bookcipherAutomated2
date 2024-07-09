
def find_a(text):
    results = []
    lines = text.split('\n')
    
    for line_number, line in enumerate(lines, start=1):
        for index, char in enumerate(line):
            if char == 'a':
                results.append((line_number, index))
                
    return results

text = """fasdfgadfdga
sdfgsfdghsaaafg"""

positions = find_a(text)

for line_number, index in positions:
    print(f"{line_number}: {index}")