# n=int(input('ENter upto which number you want to find the sum of even numbers: '))
# sum_even = 0
# for i in range(2,n+1,2):
#     sum_even += i
# print("The sum of even numbers from 1 to", n, "is:", sum_even)  # Print the sum of even numbers


#Second Method
n = int(input('Enter the number up to which you want to find the sum of even numbers: '))
sum_even = 0
for i in range(2,n+1):
    if i % 2 == 0:  # Check if the number is even
        sum_even += i
print("The sum of even numbers from 1 to", n, "is:", sum_even)  # Print the sum of even numbers


