def decode_results(encoded_file, original_text_file):
    # Read contents of original text file
    with open(original_text_file, "r") as file:
        text = file.read()

    # Read encoded results from the results file
    with open(encoded_file, "r") as file:
        encoded_results = file.readlines()

    # Split original text into lines
    lines = text.split('\n')

    # Initialise decoded output
    decoded_output = ""

    # Process each line in encoded results
    for line in encoded_results:
        line = line.strip()  # Remove any surrounding whitespace or newline characters
        if ':' in line:
            # Extract line number and index from the encoded result
            line_number, index = map(int, line.split(':'))
            # Append the character found at the specified line and index
            decoded_output += lines[line_number - 1][index]
        else:
            # Append the encoded character directly (it was not found in the text)
            decoded_output += line

    return decoded_output

# Specify file names
encoded_file = "results.txt"
original_text_file = "sample.txt"

# Decode results
decoded_text = decode_results(encoded_file, original_text_file)

# Output decoded text
print("Decoded Text:", decoded_text)