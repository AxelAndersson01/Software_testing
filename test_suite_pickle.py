import pickle
import hashlib
import os
import platform
import sys

# Function to compute SHA-256 hash of the pickled data
def compute_hash(obj):
    pickled_data = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    return hashlib.sha256(pickled_data).hexdigest()

# Define test cases
test_cases = {
    "int": 42,
    "float": 3.141592653589793,
    "string": "Hello, world!",
    "boolean": True,
    "list": [1, 2, 3, 4, 5],
    "dict": {"key1": "value1", "key2": 2},
    "tuple": (1, 2, 3),
    "set": {1, 2, 3},
    "nested": {"a": [1, 2, 3], "b": {"c": 3.14}},
    "custom_obj": type("TestClass", (object,), {"attr": 42})(),
    "recursive_list": lambda: None,
    "random_string": "\n",
    "bytes": bytes(15),
    "complex": complex(1j)
}

# Create recursive data structure
recursive_list = []
recursive_list.append(recursive_list)
test_cases["recursive_list"] = recursive_list

# Function to run the test suite
def run_tests():
    results = {}
    for name, obj in test_cases.items():
        try:
            hash_value = compute_hash(obj)
            results[name] = hash_value
        except Exception as e:
            results[name] = f"Error: {str(e)}"
    return results

# Function to print system information
def system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": sys.version,
    }

# Function to write results to a file
def write_results_to_file(system_info, test_results, filename="pickle_test_results.txt"):
    with open(filename, "a") as file:
        file.write("\nSystem Information:\n")
        for key, value in system_info.items():
            file.write(f"{key}: {value}\n")
        
        file.write("\nTest Results:\n")
        for name, hash_value in test_results.items():
            file.write(f"{name}: {hash_value}\n")

# Main function to run tests and gather results
def main():
    results = run_tests()
    sys_info = system_info()
    
    # Write results to file
    write_results_to_file(sys_info, results)

    # Optionally, print the results to the console as well
    print("Results written to pickle_test_results.txt")

if __name__ == "__main__":
    main()
