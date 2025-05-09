"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def number_to_roman(self, number: int) -> str:
        if number == 0:
            return 'There is no zero in the Roman numeral system.'

        elif number < 0:
            return 'number can not less than 0'

        symbols = {
            # Special Numbers
            1_000_000: 'M̅',
            900_000: 'C̅M̅',
            500_000: 'D̅',
            400_000: 'C̅D̅',
            100_000: 'C̅',
            90_000: 'X̅C̅',
            50_000: 'L̅',
            40_000: 'X̅L̅',
            10_000: 'X̅',
            9_000: 'MX̅',
            5_000: 'V̅',
            4_000: 'MV̅',
            
            # Normal Numbers
            1_000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        text_numbers = ''
        for key, value in symbols.items():
            while number >= key:
                text_numbers += value
                number -= key

        return text_numbers


if __name__ == '__main__':
    solution = Solution()

    try:
        number = int(input('Enter number: '))
        print(solution.number_to_roman(number))
    except ValueError:
        print('Input must be an integer')
