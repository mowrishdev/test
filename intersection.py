def find_intersection(file1_path, file2_path):
    # Read lines from both files
    with open(file1_path, 'r') as f1:
        file1_lines = set(f1.read().splitlines())
    
    with open(file2_path, 'r') as f2:
        file2_lines = set(f2.read().splitlines())
    
    # Find intersection
    common_lines = file1_lines.intersection(file2_lines)
    
    # Print common lines
    print("Common lines in both files:")
    for line in common_lines:
        print(line)
    
    return common_lines

# Usage
file1_path = "file1.txt"
file2_path = "file2.txt"
common = find_intersection(file1_path, file2_path)
