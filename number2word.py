from fractions import Fraction

def num_to_words(number):
    # Define words for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

    if number == 0:
        return "zero"

    if number < 0:
        return "minus " + num_to_words(-number)

    words = ""
    scale_index = 0

    while number > 0:
        # Extract the last three digits
        chunk = number % 1000
        number //= 1000

        if chunk > 0:
            chunk_words = ""
            if chunk // 100 > 0:
                chunk_words += ones[chunk // 100] + " hundred "
                chunk %= 100

            if chunk > 0:
                if chunk < 10:
                    chunk_words += ones[chunk]
                elif chunk < 20:
                    chunk_words += teens[chunk % 10]
                else:
                    chunk_words += tens[chunk // 10]
                    if chunk % 10 != 0:
                        chunk_words += "-" + ones[chunk % 10]

            # Add scale word (thousand, million, billion, etc.)
            words = chunk_words.strip() + (" " + scales[scale_index] if scales[scale_index] else "") + " " + words

        scale_index += 1

    return words.strip()


def fraction_to_words(fraction):
    numerator_words = num_to_words(fraction.numerator)
    denominator_words = num_to_words(fraction.denominator)
    return f"{numerator_words} over {denominator_words}"


def float_to_words(number):
    integer_part = int(number)
    fractional_part = round(number - integer_part, 10)  # Handle rounding errors
    integer_words = num_to_words(integer_part)
    fractional_words = " ".join([num_to_words(int(digit)) for digit in str(fractional_part)[2:]])
    return f"{integer_words} point {fractional_words}"


def complex_to_words(complex_num):
    real_part = complex_num.real
    imaginary_part = complex_num.imag
    real_words = num_to_words(int(real_part)) if real_part != 0 else ""
    imaginary_words = num_to_words(int(imaginary_part)) if imaginary_part != 0 else ""
    if real_words and imaginary_words:
        return f"{real_words} plus {imaginary_words} i"
    elif real_words:
        return real_words
    elif imaginary_words:
        return f"{imaginary_words} i"
    else:
        return "zero"


# Main Program Loop
if __name__ == "__main__":
    while True:
        try:
            # Ask for user input
            user_input = input("Please input the number you wish: ").strip()
            if "/" in user_input:  # Rational number
                frac = Fraction(user_input)
                print("Converting the rational number into words looks like:", fraction_to_words(frac))
            elif "j" in user_input or "i" in user_input:  # Imaginary number
                complex_num = complex(user_input.replace("i", "j"))
                print("Converting the complex number into words looks like:", complex_to_words(complex_num))
            elif "." in user_input:  # Floating-point number
                float_num = float(user_input)
                print("Converting the floating-point number into words looks like:", float_to_words(float_num))
            else:  # Integer
                num = int(user_input)
                print("Converting the integer into words looks like:", num_to_words(num))
        except ValueError:
            print("Please enter a valid number.")

        # Ask if the user wants to continue
        proceed = input("Would you like to input another number? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Exiting the program. Goodbye!")
            break
