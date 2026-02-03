"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers) == 0:
        return 0

    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    else:
        return count_even(numbers[1:])


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings) == 0:
        return []

    rest = find_strings_with(strings[1:], target)

    if target in strings[0]:
        return [strings[0]] + rest
    else:
        return rest


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """
    # Base case: if it's a file, count it
    if os.path.isfile(directory_path):
        return 1

    # If it's not a directory (edge case)
    if not os.path.isdir(directory_path):
        return 0

    total = 0
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        total += count_files(full_path)

    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """
    # Base case: if it's a file, check extension
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    # If it's not a directory (edge case)
    if not os.path.isdir(directory_path):
        return []

    infected = []
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        infected += find_infected_files(full_path, extension)

    return infected


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE\n")

    # Warm-up tests
    print("sum_list tests:")
    print(sum_list([1, 2, 3, 4]))  # 10
    print(sum_list([]))            # 0

    print("\ncount_even tests:")
    print(count_even([1, 2, 3, 4, 5, 6]))  # 3
    print(count_even([1, 3, 5]))           # 0

    print("\nfind_strings_with tests:")
    print(find_strings_with(["hello", "world", "help", "test"], "hel"))  # ['hello', 'help']

    # File counting tests
    print("\nFile count tests:")
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat"))     # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested"))   # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    # Breach file count
    print("\nTotal files (breached files):", count_files("breach_data"))

    # Infected file tests
    print("\nInfected file tests:")
    print("Test Case 1:", len(find_infected_files("test_cases/case1_flat")))     # 0
    print("Test Case 2:", len(find_infected_files("test_cases/case2_nested")))   # 0
    print("Test Case 3:", len(find_infected_files("test_cases/case3_infected"))) # 3

    # Breach infected files
    print("\nTotal infected files (breach):", len(find_infected_files("breach_data")))

    # Department analysis
    finance = find_infected_files("breach_data/Finance")
    hr = find_infected_files("breach_data/HR")
    sales = find_infected_files("breach_data/Sales")

    print("\nInfected by department:")
    print("Finance:", len(finance))
    print("HR:", len(hr))
    print("Sales:", len(sales))
