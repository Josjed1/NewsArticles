# Replace "your_binary_file.bin" with the actual path to your binary file
file_path = "test2.bin"

try:
    with open(file_path, "rb") as binary_file:
        # Read the entire content of the binary file
        binary_data = binary_file.read()

        # Iterate over each byte and print its decimal value
        for byte_value in binary_data:
            print(byte_value, end=' ')
            
            # If you want to output the byte value as a hexadecimal string, you can use the following line instead
            # print(hex(byte_value)[2:], end=' ')
except FileNotFoundError:
    print(f"File not found: {file_path}")
except IOError as e:
    print(f"Error reading the file: {e}")
