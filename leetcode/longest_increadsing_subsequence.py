nums =[0,1,0,3,2,3]

first_pointer = 0
second_pointer = 1
last_number = -1000000
new_ans_list = []

for i in range(len(nums)):
    temp_num = nums[i]
    temp_res = [temp_num]
    for j in range(i+1 , len(nums)):
        if nums[j] > temp_num:
            print(temp_num, nums[j], "=====")
            temp_res.append(nums[j])
            temp_num = nums[j]
    print("================================================================")
    print(temp_res)
    new_ans_list.append(len(temp_res))
    print("********************************")
print(new_ans_list)


# while second_pointer < len(nums):
#     if nums[first_pointer] < nums[second_pointer] and last_number < nums[second_pointer]:
#         print(nums[first_pointer], nums[second_pointer], "=====", last_number)

#         last_number = nums[first_pointer]
#         new_ans_list.append(nums[first_pointer])
#     first_pointer += 1
#     second_pointer += 1
# if nums[first_pointer] > last_number:
#     new_ans_list.append(nums[first_pointer])

# print(new_ans_list)
