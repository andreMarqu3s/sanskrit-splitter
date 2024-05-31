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
#response = requests.post('https://splitter-server-tylergneill.pythonanywhere.com/', json={'input_text': input_text}, stream=True)
response = requests.post(
"https://www.skrutable.info/api/split",
data={
"input_text": input_text,
"from_scheme": "IAST",
"to_scheme": "IAST"
},
stream=True)

# Check if the output file argument was specified
if args.output_file:
    # Open the output file with the utf-8 encoding
    with open(args.output_file, 'w', encoding='utf-8') as output_file:
        # Read the response in chunks and write to the output file
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                output_file.write(chunk.decode('utf-8'))

    # Print a success message
    print('Results saved to', args.output_file)
else:
    # Read the response in chunks and print to the terminal
    result = ''
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            result += chunk.decode('utf-8')
    print(result)