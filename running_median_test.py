from runningMedian import runningMedian

def print_colored(text, color):
    """Terminalde renkli çıktı vermek için."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def test_running_median(a, expected_medians, test_number):
    """Test fonksiyonu."""
    print(f"\n{print_colored(f'Test Case {test_number}:', 'cyan')}")
    print(f"Input Array: {a}")
    actual_medians = runningMedian(a)
    print(f"Expected Medians: {expected_medians}")
    print(f"Actual Medians:   {actual_medians}")
    
    if actual_medians == expected_medians:
      print(print_colored(f"Test Passed", "green"))
    else:
        print(print_colored(f"Test Failed", "red"))


# Test Verileri
test_cases = [
    ([12, 4, 5, 3, 8, 7], [12.0, 8.0, 5.0, 4.5, 5.0, 6.0]),
    ([1, 2, 3, 4, 5, 6], [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]),
    ([5, 4, 3, 2, 1], [5.0, 4.5, 4.0, 3.5, 3.0]),
    ([1], [1.0]),
    ([3, 1, 2], [3.0, 2.0, 2.0]),
    ([7, 3, 5, 2], [7.0, 5.0, 5.0, 4.0]),
    ([10, 5, 20, 3, 15], [10.0, 7.5, 10.0, 7.5, 10.0])
]


for i, (a, expected) in enumerate(test_cases, 1):
    test_running_median(a, expected, i)