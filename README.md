# sanskrit-splitter

This project provides a simple command-line tool for splitting Sanskrit words/compounds using a Python script. The script utilizes an API hosted on [splitter-server-tylergneill.pythonanywhere.com](https://splitter-server-tylergneill.pythonanywhere.com/).

## Installation & Dependencies

Ensure you have Python 3 installed on your system.

This project requires the following Python packages:

- `argparse`: For parsing command-line arguments.
- `requests`: For making HTTP requests to the splitter server.

You can install these dependencies using pip.

## Usage

1. Clone this repository.

2. Use the following command format:

    ```
    python sanskrit-splitter.py input [-o OUTPUT_FILE]
    ```

    - `input`: The Sanskrit words or file to split. Ensure it is in valid IAST.
    - `-o, --output_file`: (Optional) Specify the output file to save the results.

    Example:

    ```
    python sanskrit-splitter.py example_word.txt -o output.txt
	python sanskrit-splitter.py "pudgaladharmanairātmyapratipādanaṃ punaḥ kleśajñeyāvaraṇaprahāṇārtham"
    ```

## Credits

- This project utilizes the splitter server developed by Tyler Neill. You can find the server code [here](https://github.com/tylergneill/splitter_server).

