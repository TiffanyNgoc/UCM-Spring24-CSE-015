'''nums = []
for i in range(0, 10):
    print("Please enter integer", i + 1, ": ")
    nums.append(int(input()))

x = 0
for i in range(0,len(nums)):
    if x < nums[i]:
        x = nums[i]
            
print("the highest number entered was: ", x) '''


max_number = None

# Loop to ask the user for 10 integers
for i in range(10):
    num = int(input("Enter an integer: "))
    
    # Compare the entered number with the current maximum
    if max_number is None or num > max_number:
        max_number = num

# Output the largest number
print("The largest number entered is:", max_number)
