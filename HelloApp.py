from typing import Literal

print("Hello Python from Visual Studio!")

def multiply(*args: int | float) -> int | float:
    """_summary_

    multiply all numbers

    Args:
        *args (int | float)

    Raises:
        ValueError: _all_ arguments must be numbers

    Returns:
        int | float: result of multiplication all numbers
    """
    
    multiplier = 1
    for number in args:
        if isinstance(number, (int, float)):
            multiplier *= number
        else:
            raise ValueError("All arguments must be numbers")
        
    return multiplier


mult = multiply(1, 2, 3, 4, 5, .4)
print(mult)
    
    