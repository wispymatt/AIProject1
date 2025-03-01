def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x.lower() <= pivot.lower()]
        greater = [x for x in arr[1:] if x.lower() > pivot.lower()]
        return quicksort(less) + [pivot] + quicksort(greater)

def read_and_sort_file(input_file, output_file):
    try:
        # Read input file
        with open(input_file, 'r') as f:
            # Read lines and remove whitespace
            strings = [line.strip() for line in f.readlines()]
        
        # Sort the strings
        sorted_strings = quicksort(strings)
        
        # Write to output file
        with open(output_file, 'w') as f:
            for string in sorted_strings:
                f.write(string + '\n')
                
        print(f"Successfully sorted {len(strings)} strings.")
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the input file '{input_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "sorted_output.txt"
    read_and_sort_file(input_file, output_file) 