"""
This module calculates the factorial of numbers from 0 to 49,
stores the results in a list, and computes the sum of these factorials.
"""
import time
final_list = []
def factorial(n):
    """
    Calculate the factorial of a given number n.
    """
    time.sleep(0.1)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def sum_factorial():
    """
    Calculate the sum of the factorials of numbers from 0 to 49
    and print the final sum.
    """
    for i in range(50):
        final_list.append(factorial(i))
    result = sum(final_list)
    print(f"Final SUM = {result}")
    return result
if __name__ == "_main_":
    sum_factorial()
    