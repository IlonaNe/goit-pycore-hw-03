import re

def normalize_phone(phone_number):
    phone_number_without_spaces = phone_number.strip()
    phone_number_with_only_digits = re.sub(r'[^\d+]', '', phone_number_without_spaces)
    
    if phone_number_with_only_digits.startswith('+380'):
        number = phone_number_with_only_digits
    elif phone_number_with_only_digits.startswith('380'):
        number = '+' + phone_number_with_only_digits
    elif phone_number_with_only_digits.startswith('80'):
        number = '+3' + phone_number_with_only_digits
    else:
        number = '+38' + phone_number_with_only_digits[-10:]
