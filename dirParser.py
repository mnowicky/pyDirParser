import os

def list_subdirectories(base_path):
    # A list to store subdirectories
    subdirectories = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(base_path):
        for dir in dirs:
            # Construct the full path of the subdirectory
            full_path = os.path.join(root, dir)
            # Add to the list
            subdirectories.append(full_path)
    
    # Return the list of subdirectories
    return subdirectories

def write_to_file(path_list, file_path):
    # Write the list of paths to a text file
    with open(file_path, 'w') as file:
        for path in path_list:
            print(path)
            file.write(path + '\n')

def main():
    # Path to the directory you want to scan
    base_directory = input("Enter the path to the directory: ")
    
    # Path for the output text file
    #output_file = input("Enter the path for the output file: ")
    output_file = 'output.txt'
    
    # Get list of all subdirectories
    subdirectories = list_subdirectories(base_directory)
    
    # Write the subdirectories to the output file
    write_to_file(subdirectories, output_file)
    
    print(f"Subdirectories have been written to {output_file}")

if __name__ == "__main__":
    main()
