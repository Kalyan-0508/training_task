def even_number(num):
    even_list = [num for num in num if num % 2== 0]
    even_list.sort(reverse=True)
    return even_list
nums = [1,2,3,4,5,6,7,8,9,10,12,11,13,14,15,16,17,18,19,20]
print(even_number(nums))

