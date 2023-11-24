def findMaxLength(nums):
    count = 0
    max_length = 0
    count_dict = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length


input_str = input()
num = input_str.split(" ")
nums = [int(bit) for bit in num]
result = findMaxLength(nums)
print(result)


'''
Exercise-1

Input : 
0 0 0 1 1 1 1 0

Output :
8

Exercise-2

Input:
1 0 0 1 1 1 1 0

Output:
4
'''