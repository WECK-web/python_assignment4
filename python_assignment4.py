def file_read_write():
    # Step 1: Ask user for input file
    filename = input("Enter the name of the file to read: ")

    try:
        # Step 2: Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify the content (example: uppercase)
        modified_content = content.upper()

        # Step 4: Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified file has been saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
file_read_write()
