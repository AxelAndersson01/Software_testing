def read_file_line_by_line(file_path):
    data_types = ['int', 'float', 'string', 'boolean', 'list', 'dict', 'tuple', 'set', 'nested', 'custom_obj', 'recursive_list','random_string', 'bytes', 'complex', 'unicode','none_value', 'utf-8_string', 'special_characters']
    hash_lists = {data_type: [] for data_type in data_types}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if 'recursive_list' in line:
                    hash_value = line.split(': ')[1]
                    hash_lists['recursive_list'].append(hash_value)
                else:
                    for data_type in data_types:
                        if line.startswith(data_type + ': '):
                            hash_value = line.split(': ')[1]
                            hash_lists[data_type].append(hash_value)
                            break
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    return hash_lists

# Usage
file_path = "pickle_test_results.txt"  
hash_lists = read_file_line_by_line(file_path)

def comparer(hash_lists):
    for data_type, hashes in hash_lists.items():
        if data_type in ['int', 'float', 'string', 'boolean', 'list', 'dict', 'tuple', 'set', 'nested', 'custom_obj', 'recursive_list','random_string', 'bytes', 'complex', 'unicode', 'none_value', 'utf-8_string', 'special_characters']:
            if len(hashes) > 1:
                first_list = hashes[0]
                if all(hash_list == first_list for hash_list in hashes[1:]):
                    print(f"All {data_type} lists are the same.")
                else:
                    print(f"Not all {data_type} lists are the same.")
            else:
                print(f"There is only one {data_type} list.")
        else:
            print(f"Ignoring {data_type}.")

if hash_lists:
    comparer(hash_lists)
