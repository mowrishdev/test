def find_and_save_differences(file1_path, file2_path, output_file):
    # Read lines from both files
    with open(file1_path, 'r') as f1:
        file1_lines = set(f1.read().splitlines())
    
    with open(file2_path, 'r') as f2:
        file2_lines = set(f2.read().splitlines())
    
    # Find unique values in each file
    unique_file1 = file1_lines - file2_lines  # In file1 but not in file2
    unique_file2 = file2_lines - file1_lines  # In file2 but not in file1
    
    # Save to output file
    with open(output_file, 'w') as f_out:
        f_out.write("Unique in File1:\n")
        for line in unique_file1:
            f_out.write(line + '\n')
        
        f_out.write("\nUnique in File2:\n")
        for line in unique_file2:
            f_out.write(line + '\n')
    
    print(f"Non-intersecting results saved to: {output_file}")
    return unique_file1, unique_file2

# Usage
file1_path = "file1.txt"
file2_path = "file2.txt"
output_file = "differences.txt"
unique1, unique2 = find_and_save_differences(file1_path, file2_path, output_file)
