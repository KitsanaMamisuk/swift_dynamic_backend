"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def number_to_thai(self, number: int) -> str:
        if number == 0:
            return 'ศูนย์'
        elif number == 1:
            return 'หนึ่ง'

        units = {
            '1': 'หนึ่ง',
            '2': 'สอง',
            '3': 'สาม',
            '4': 'สี่',
            '5': 'ห้า',
            '6': 'หก',
            '7': 'เจ็ด',
            '8': 'แปด',
            '9': 'เก้า',
        }
        positions = {
            2: 'สิบ',
            3: 'ร้อย',
            4: 'พัน',
            5: 'หมื่น',
            6: 'แสน',
            7: 'ล้าน',
            8: 'สิบล้าน',
        }
        list_numbers = str(number)
        len_str = len(list_numbers)
        list_text = []

        reverse_number = reversed(list_numbers)
        for index, value in enumerate(reverse_number, start=1):
            if len_str > 1 and index == 1:
                if value == '0':
                    continue
                elif value == '1':
                    list_text.append('เอ็ด')
                    continue
                else:
                    list_text.append(units.get(value))
                    continue

            elif len_str > 1 and index == 2:
                if value == '0':
                    continue
                elif value == '1':
                    list_text.append('สิบ')
                    continue
                elif value == '2':
                    list_text.append(f'ยี่{positions.get(index)}')
                    continue
                else:
                    list_text.append(f'{units.get(value)}{positions.get(index)}')
                    continue

            else:
                if units.get(value) and index < 8:
                    list_text.append(f'{units.get(value)}{positions.get(index)}')
                elif units.get(value) and index == 8:
                    list_text.append(f'{positions.get(index)}')

        return ''.join(reversed(list_text))


if __name__ == '__main__':
    solution = Solution()
    try:
        number = int(input('Enter number: '))
        if number < 0 or number > 10_000_000:
            print('Number must be in range 0 to 10_000_000')
            exit()

        print(solution.number_to_thai(number))
    except ValueError:
        print('Input must be an integer')