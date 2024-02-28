import argparse
import requests

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Split Sanskrit words')

# Add an argument to accept the input text or file
parser.add_argument('input', help='The Sanskrit word or file to split [input must already be in valid IAST]')

# Add an optional argument to accept the output file
parser.add_argument('-o', '--output_file', help='The output file to save the results to')

# Parse the command-line arguments
args = parser.parse_args()

# Check if the input is a file or text
if args.input.endswith('.txt'):
    # Open the input file with the utf-8 encoding
    with open(args.input, 'r', encoding='utf-8') as input_file:
        # Read the contents of the input file
        input_text = input_file.read()
else:
    # The input is text, so use it as the input text
    input_text = args.input

# Send a POST request to the splitter server with the input text
result = requests.post('https://splitter-server-tylergneill.pythonanywhere.com/', json={'input_text': input_text})

# Check if the output file argument was specified
if args.output_file:
    # Open the output file with the utf-8 encoding
    with open(args.output_file, 'w', encoding='utf-8') as output_file:
        # Write the result string to the output file
        output_file.write(result.text)

    # Print a success message
    print('Results saved to', args.output_file)
else:
    # Print the result string to the terminal
    print(result.text)
