'''nums = []
for i in range(0,10):
    print("Please enter integer", i + 1, ": ")
    nums.append(int(input()))

x = 0
f = 0
for i in range(0,len(nums)):
    if (nums[i] % 2) != 0:
        f = nums[i] 
    if (f > x):
        x = nums[i]
if (x != 0):
    print("The hightest odd number entered was: ", x)

else:
    print("No odd numbers were entered")
'''

# Initialize a variable to store the largest odd number
max_odd = None

# Loop to ask the user for 10 integers
for i in range(10):
    num = int(input("Enter an integer: "))
    
    # Check if the entered number is odd and greater than the current maximum odd number
    if num % 2 != 0 and (max_odd is None or num > max_odd):
        max_odd = num

# Check if any odd numbers were entered and output the result accordingly
if max_odd is not None:
    print("The largest odd number entered is:", max_odd)
else:
    print("No odd numbers were entered.")
