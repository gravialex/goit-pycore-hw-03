import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number string to a standard international format: '+380XXXXXXXXX'.
    It strips away all non-digit characters (except an initial '+') and prepends
    the Ukrainian country code '+38' or '+' as needed.
    
    Parameters:
    phone_number (str): The raw phone number string in any format.
    
    Returns:
    str: The fully normalized phone number starting with '+'.
    """
    # 1. Clean the string: remove all characters except digits and the '+' symbol.
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)
    
    # 2. Adjust prefixes to ensure the number starts with the standard '+38' country code:
    if cleaned_number.startswith("+380"):
        return cleaned_number
        
    # Case B: If the number starts with '380' (missing the '+'), prepend '+'
    elif cleaned_number.startswith("380"):
        return "+" + cleaned_number
        
    # Case C: If the number starts with '+' but is missing '38' (e.g. '+050123...'),
    elif cleaned_number.startswith("+"):
        # replace the leading '+' with '+38'
        return "+38" + cleaned_number[1:]
        
    # Case D: If there is no country code at all (e.g., starts with '050' or '067'),
    # add the full '+38' code.
    else:
        return "+38" + cleaned_number
    
# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
