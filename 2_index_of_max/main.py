"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        index_max = (0, numbers[0])  # (index, max value)
        len_numbers = len(numbers)
        for i in range(1, len_numbers):
            if numbers[i] > index_max[1]:
                index_max = (i, numbers[i])
        
        return index_max[0]



if __name__ == '__main__':
    solution = Solution()
    input_str = input('Enter list of numbers: ')
    input_str = input_str.strip('[]')
    if not input_str:
        print('List can not blank')
        exit()
    try:
        list_str = [number.strip() for number in input_str.split(',') if number.strip()] # removes empty string and add the numbers to list
        list_numbers = [int(number) if '.' not in number else float(number) for number in list_str] # convert string to int or float
        print(solution.find_max_index(list_numbers))
    except ValueError:
        print('Input must be a list of integers or floats')

