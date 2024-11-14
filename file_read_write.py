def read_and_modify_file(input_filename, output_filename):
    """
    Reads the content of the input file, modifies it (converts to uppercase),
    and writes the modified content to the output file.
    """
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File has been successfully modified and saved to {output_filename}")
    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading or writing the file: {e}")

def ask_for_filename_and_handle_errors():
    """
    Asks the user for a filename and handles errors if the file doesn't exist,
    can't be read, or there are any other issues.
    """
    input_filename = input("Enter the filename to read: ")

    try:
        # Open the file and read its content
        with open(input_filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Select an option:")
    print("1. Read and modify a file")
    print("2. Handle file errors")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        input_filename = input("Enter the input filename: ")
        output_filename = input("Enter the output filename: ")
        read_and_modify_file(input_filename, output_filename)
    elif choice == '2':
        ask_for_filename_and_handle_errors()
    else:
        print("Invalid choice. Please enter 1 or 2.")
