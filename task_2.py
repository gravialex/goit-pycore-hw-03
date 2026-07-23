import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:
    """
    Generates a sorted list of unique random numbers.
    
    Parameters:
    min_val (int): The minimum possible number (must be >= 1).
    max_val (int): The maximum possible number (must be <= 1000).
    quantity (int): The number of unique values to select.
    
    Returns:
    list: A sorted list of unique integers. Returns an empty list if parameters are invalid.
    """

    if (min_val < 1 or 
        max_val > 1000 or 
        min_val > max_val or 
        quantity <= 0 or 
        quantity > (max_val - min_val + 1)):
        return []
    
    try:
        # Generate a list of unique random numbers within the specified range
        unique_numbers = random.sample(range(min_val, max_val + 1), quantity)
        
        # Sort the generated numbers in ascending order and return the list
        return sorted(unique_numbers)
        
    except Exception as e:
        # Fallback safeguard for any unexpected runtime errors
        print(f"An unexpected error occurred: {e}")
        return []
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
