class RomanNumberTextRepresentation:

    @staticmethod
    def of(number):

        roman_number = ""
        units = number % 10
        tens = int((number % 100) / 10)
        hundred = int(number / 100)

        roman_number = RomanNumberTextRepresentation._convert_digit(hundred, roman_number, 'C', 'D', 'M')
        roman_number = RomanNumberTextRepresentation._convert_digit(tens, roman_number, 'X', 'L', 'C')
        roman_number = RomanNumberTextRepresentation._convert_digit(units, roman_number, 'I', 'V', 'X')

        return roman_number

    @staticmethod
    def _convert_digit(a_digit, n, as_one='I', as_five='V', as_ten='X'):
        if 1 <= a_digit <= 3:
            for i in range(a_digit):
                n += as_one
        if a_digit == 4:
            n += as_one + as_five
        if 5 <= a_digit <= 8:
            n += as_five
            for i in range(0, a_digit - 5):
                n += as_one
        if a_digit == 9:
            n += as_one + as_ten
        return n
