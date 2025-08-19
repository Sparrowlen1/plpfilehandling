def read_and_write_file():
    try:
        input_file = input("Enter the name of the file to read: ")

        with open(input_file, "r") as f:
            content = f.read()
        print("Successfully read the file.")
        modified_content = content.upper()

        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Successfully wrote modified content to {output_file}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_and_write_file()
