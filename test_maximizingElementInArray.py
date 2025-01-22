import maximizingElementInArray  # maxElement fonksiyonunun olduğu Python file
import logging

# Logging ayarları
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def test_maxElement():
    logger.info("Starting tests for maxElement function...")

    # Test case 1
    n, maxSum, k = 3, 7, 1
    expected = 3
    result = maximizingElementInArray.maxElement(n, maxSum, k)
    assert result == expected, f"Test case 1 failed: Expected {expected}, got {result}"
    logger.debug(f"Test case 1 passed. Input: (n={n}, maxSum={maxSum}, k={k}), Output: {result}")

    # Test case 2
    n, maxSum, k = 4, 4, 3
    expected = 1
    result = maximizingElementInArray.maxElement(n, maxSum, k)
    assert result == expected, f"Test case 2 failed: Expected {expected}, got {result}"
    logger.debug(f"Test case 2 passed. Input: (n={n}, maxSum={maxSum}, k={k}), Output: {result}")

    # Test case 3
    n, maxSum, k = 3, 6, 1
    expected = 2
    result = maximizingElementInArray.maxElement(n, maxSum, k)
    assert result == expected, f"Test case 3 failed: Expected {expected}, got {result}"
    logger.debug(f"Test case 3 passed. Input: (n={n}, maxSum={maxSum}, k={k}), Output: {result}")

    # Test case 4
    n, maxSum, k = 4, 10, 2
    expected = 3
    result = maximizingElementInArray.maxElement(n, maxSum, k)
    assert result == expected, f"Test case 4 failed: Expected {expected}, got {result}"
    logger.debug(f"Test case 4 passed. Input: (n={n}, maxSum={maxSum}, k={k}), Output: {result}")

    # Test case 5
    n, maxSum, k = 5, 15, 3
    expected = 4
    result = maximizingElementInArray.maxElement(n, maxSum, k)
    assert result == expected, f"Test case 5 failed: Expected {expected}, got {result}"
    logger.debug(f"Test case 5 passed. Input: (n={n}, maxSum={maxSum}, k={k}), Output: {result}")

    logger.info("All test cases passed successfully!")

if __name__ == "__main__":
    test_maxElement()
