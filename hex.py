
# Decoder ring for all bases up to 36
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ------------------------------------------------
# Part 1: Convert FROM any base TO decimal
# ------------------------------------------------
def to_decimal(number_string, original_base):
    number_string = number_string.strip().upper()
    total_value = 0
    power = 0

    # Loop through the string backwards
    for char in number_string[::-1]:
        if char not in digits[:original_base]:
            raise ValueError(f"'{char}' is not valid for base {original_base}")
        char_value = digits.index(char)
        total_value += char_value * (original_base ** power)
        power += 1

    return total_value


# ------------------------------------------------
# Part 2: Convert FROM decimal TO any base
# ------------------------------------------------
def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return "0"

    result_string = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string  # prepend
    return result_string


# ------------------------------------------------
# Main Program: The UI
# ------------------------------------------------
def main():
    print("Welcome to The Hexorcist. THE POWER OF MATH COMPELS YOU!\n")

    number_string = input("Enter the number you want to convert: ").strip()
    original_base = int(input("Enter the number's CURRENT base (2-36): ").strip())
    target_base = int(input("Enter the NEW base you want (2-36): ").strip())

    print("\n...calculating with sticks and stones...\n")

    try:
        decimal_value = to_decimal(number_string, original_base)
        converted_value = from_decimal(decimal_value, target_base)
        print(f"'{number_string}' (Base-{original_base}) is '{converted_value}' (Base-{target_base}).")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
