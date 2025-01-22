from rich.console import Console
from rich.theme import Theme
from rich.traceback import install
import numpy as np

# Install rich traceback for better debugging
install()

# Custom theme for better console output
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "bold yellow",
    "success": "bold green",
    "error": "bold red"
})
console = Console(theme=custom_theme)

def maxElement(n, maxSum, k):
    def calculateSum(peak):
        sum = peak
        console.log(f"[info]Calculating sum with peak = {peak}[/info]")

        # Calculate left side
        left = peak - 1
        count = k
        console.log(f"[info]-- Calculating left side:[/info]")
        while count > 0 and left > 0:
            sum += left
            console.log(f"   Adding {left} to sum. Current sum = {sum}")
            left -= 1
            count -= 1
        sum += count  # Add remaining elements as 1
        console.log(f"   Adding remaining {count} elements as 1. Current sum = {sum}")

        # Calculate right side
        left = peak - 1
        count = n - k - 1
        console.log(f"[info]-- Calculating right side:[/info]")
        while count > 0 and left > 0:
            sum += left
            console.log(f"   Adding {left} to sum. Current sum = {sum}")
            left -= 1
            count -= 1
        sum += count  # Add remaining elements as 1
        console.log(f"   Adding remaining {count} elements as 1. Current sum = {sum}")

        return sum

    left, right = 1, maxSum
    result = 0

    console.log(f"\n[info]Initial binary search range: left = {left}, right = {right}[/info]")

    while left <= right:
        mid = (left + right) // 2
        sum = calculateSum(mid)

        console.log(f"\n[info]Trying mid = {mid}, sum = {sum}[/info]")

        if sum <= maxSum:
            result = mid
            console.log(f"[success]Sum is within maxSum. Updating result = {result}[/success]")
            left = mid + 1
            console.log(f"[info]Updating binary search range: left = {left}, right = {right}[/info]")
        else:
            right = mid - 1
            console.log(f"[warning]Sum exceeds maxSum. Updating binary search range: left = {left}, right = {right}[/warning]")

    console.log(f"\n[success]Final result = {result}[/success]")
    return result

# Test cases with numpy arrays for better performance and integration
console.log("[bold cyan]Starting Test Cases[/bold cyan]")
test_cases = np.array([
    (3, 7, 1),
    (4, 4, 3),
    (3, 6, 1),
    (4, 10, 2),
    (5, 15, 3)
])

for i, (n, maxSum, k) in enumerate(test_cases):
    console.log(f"\n[bold yellow]Running Test Case {i + 1}: (n={n}, maxSum={maxSum}, k={k})[/bold yellow]")
    result = maxElement(n, maxSum, k)
    console.log(f"[bold green]Result for Test Case {i + 1}: {result}[/bold green]")
