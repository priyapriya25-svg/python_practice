# arr = [1,9,7,4]
# largest = arr[0]

# for ch in arr:
#     if ch > largest:
#         largest = ch
# print (largest)

# arr = [1,2,3,4,5]
# rev = []
# for i in arr:
#     rev = [i] + rev
# print(rev)

# n = 100
# for i in range(1, n+ 1):
#     print(i)


# (2 DSA question basic and 1 medium)
# find the largest element in the array 

# arr = [1,34,5,328,67,0]
# largest = arr[0]
# for i in arr:
#     if i > largest:
#         largest = i
# print("largest element:", largest)

# # count even and odd numbers

# arr = [2,3,4,5,6,7,8,9,10]
# even = 0
# odd = 0

# for i in arr:
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even count:", even)
# print("Odd count:", odd)

# find the second largest element in an array (medium)

# arr = [12,475,7,89,23]
# largest = arr[0]
# for i in arr:
#     if i > largest:
#         largest = i

# second_largest = arr[0]
# for i in arr:
#     if i != largest:
#         if i > second_largest:
#             second_largest = i
# print("second largest:", second_largest)

# 3 DSA question intermediate 

# Move all zeros to the end

# arr = [0,1,0,3,12]
# arr1 = []
# zeros = arr.count(0)
# for i in arr:
#     if i == 0:
#         continue
#     else:
#         arr1.append(i)
# for i in range(zeros):
#     arr1.append(0)

# print(arr1)

# Check positive, negative or zero

# num = int(input())
# if num == 0:
#     print("Zero")
# elif num > 0:
#     print("postive")
# else:
#     print("negative")

# Perform operations on numbers from 1 to n

# n = int(input())
# total = 0 
# for i in range(1,n+1):
#   if i %2==0:
#     total = total - 10
#   else:
#     total = total + 20
# print("total", total)

# Count positive , negative and zero 

# arr = [5, 10, 15, 20]

# positivecount = 0
# negativecount = 0
# zeroscount = 0

# for i in arr:
#     if i == 0:
#         zeroscount = zeroscount + 1
#     elif i > 0:
#         positivecount = positivecount + 1
#     else:
#         negativecount = negativecount + 1
# print("Positive:", positivecount,"Negative:", negativecount,"Zeros:", zeroscount)
        
# Print number divisible by 3 and 7 in a range

# m = int(input("Enter starting number: "))
# n = int(input("Enter ending number: "))

# for i in range(m, n + 1):

#     if i % 3 == 0:
#         if i % 7 == 0:
#             print(i, "-> Divisible by both")
#         else:
#             print(i, "-> Divisible by 3")

#     elif i % 7 == 0:
#         print(i, "-> Divisible by 7")

# Filter array elements 

# arr = list(map(int, input("Enter numbers: ").split()))

# found = False

# for i in arr:

#     if i % 3 == 0:
#         if i % 7 == 0:
#             pass        
#         else:
#             print(i)
#             found = True

#     else:
#         if i % 7 == 0:
#             print(i)
#             found = True

# if found == False:
#     print("No valid numbers found.")

# Write a JavaScript program that takes an integer as 
# input from the user. Determine whether the given number is divisible by 3.

# n = int(input())
# if n % 3==0:
#     print("Divisible by 3")
# else:
#     print("Not divisible by 3")

# Check Divisibility by 3 and 7
# Problem Statement

# n = int(input())

# if n % 3 == 0:
#     if n % 7 == 0:
#         print("Both")
#     else:
#         print("Three")
# else:
#     if n % 7 == 0:
#         print("Seven")
#     else:
#         print("Not divisible


# PSA question 

# Write a program that asks the user to input a single integer. 
# Use an if-else statement to check if the last digit of the number is equal to 9.
 
# n = int(input())
# last_digit = n % 10
# if last_digit == 9:
#     print("End with 9")
# else:
#     print("Does not end with 9")

# Write a program that takes an integer input from the user. 
# The user might enter a negative number (e.g., -149).

# n = int(input("Enter a number: "))

# if n < 0:
#     n = -n

# if n % 10 == 9:
#     print("Valid 9-ender")
# else:
#     print("Invalid")

#Write a program that uses a while loop to continuously ask the user
#  to enter a number.

# while True:
#     n = int(input("Enter a number: "))

#     if n < 0:
#         n = -n

#     if n % 10 == 9:
#         print("You found the magic number!")
#         break
#     else:
#         print("Try again!")

# Write a program that uses a for loop to ask the user 
# to input exactly 5 different integers, one by one.

# count = 0

# for i in range(5):
#     n = int(input("Enter a number: "))

#     if n < 0:
#         n = -n

#     if n % 10 == 9:
#         count += 1

# if count > 0:
#     print("You entered", count, "numbers ending in 9.")
# else:
#     print("No numbers ended in 9.")


# Write a program that asks the user to input 10
#  integers and stores them in an array (or list).

# arr = []
# new_arr = []

# for i in range(10):
#     n = int(input())

#     if n < 0:
#         n = -n

#     arr.append(n)

# for num in arr:
#     if num % 10 == 9:
#         new_arr.append(num)

# print(arr)

# if len(new_arr) == 0:
#     print("No numbers ending in 9 were found.")
# else:
#     print(new_arr)

# PSA Question 

# Write a program that takes the MRP and Discount Percentage from the user.
# If the discount is between 0% and 100%, calculate the selling price.

# mrp = int(input("Enter MRP: "))
# discount = int(input("Enter Discount: "))

# if discount >= 0:
#     if discount <= 100:
#         discount_amount = mrp * discount / 100
#         selling_price = mrp - discount_amount
#         print("Selling Price = ₹", selling_price)
#     else:
#         print("Invalid Discount")
# else:
#     print("Invalid Discount")

# A shop has 5 products.
# Using a loop:
# Take MRP and Discount for each product.

# for i in range(5):

#     print("Product", i + 1)

#     mrp = int(input("Enter MRP: "))
#     discount = int(input("Enter Discount: "))

#     if discount >= 0:
#         if discount <= 100:
#             discount_amount = mrp * discount / 100
#             selling_price = mrp - discount_amount
#             print("Selling Price =", selling_price)

# A supermarket has 3 categories, and each category contains 4 products.
# Using nested loops:
# Take MRP and Discount for every product.

# for category in range(3):
#     print("category", category + 1)
# for product in range(4):
#     print("Product", product + 1)
#     mrp = int(input("Enter MRP: "))
#     discount = int(input("Enter Discount: "))
    
#     if discount >= 0:
#      if discount <= 100:
#             discount_amount = mrp * discount / 100
#             selling_price = mrp - discount_amount
#             print("Selling Price =", selling_price)


# PSA question 

# *A company has N employees. Each employee has 
# completed a certain number of tasks.*

# n = int(input("enter numbers of employes"))
# tasks = []

# for i in range(n):
#     x = int(input("enter number of task completed"))
#     tasks.append(x)

# eligible = []
# for x in tasks:
#     if x >= 50:
#      if x % 2 == 0:
#             eligible.append(x)

# print("Eligible employees:", len(eligible))


# print("task counts:", eligible)

# if len(eligible) > 0:
#     highest = max(eligible)
#     print("Highest:", highest)

#     second = 0

#     for x in eligible:
#         if x < highest:
#             if x > second:
#                 second = x

#     if second > 0:
#         print("Second highest:", second)
#     else:
#         print("Second highest: Not available")

#         promoted = []

#     for x in eligible:
#         if x * 100 >= highest * 90:
#             promoted.append(x)

#     print("Promoted employees:", promoted)

# else:
#     print("No eligible employees")

# PSA question

# There are 5 products.
# Create two arrays:
# One array stores the MRP.

# mrp = [100, 200, 150, 80, 300]
# discount = [10, 15, 20, 5, 25]

# for i in range(5):
#     d = mrp[i] * discount[i] / 100
#     p = mrp[i] - d
#     print("Selling Price =", p)
 
# Store the MRP and Discount of 6 products in arrays.
# For every product:
# If the discount is between 0 and 100, calculate the selling price.
# Otherwise print "Invalid Discount".

# mrp = [100, 200, 150, 80, 300,350]
# discount = [10, 15, 20, 101, 25,30]

# for i in range(6):
#     if discount[i] >= 0:
#         if discount[i] <= 100:
#             discount_amount = mrp[i] * discount[i] / 100
#             selling_price = mrp[i] - discount_amount
#             print("Selling price :", selling_price)
#         else:
#             print("Invalid discount")

# A supermarket has 3 rows and 4 products in each row.
# Store the MRP in a 2D array.
# Take the discount for each product and calculate the selling price.
# Display the selling price in matrix format.

# mrp = [
#     [100, 200, 150, 80],
#     [300, 250, 400, 500],
#     [120, 180, 220, 350]
# ]

# for i in range(3):
#     for j in range(4):
#             discount = list(map(int, input("Enter discounts: ").split()))        
#             if discount[j] >= 0:
#              if discount[j] <= 100:
#                 discount_amount = mrp[i][j] * discount[j] / 100
#                 selling_price = mrp[i][j] - discount_amount
#                 print(selling_price, end="")

# mrp = [
#     [100, 200, 150, 80],
#     [300, 250, 400, 500],
#     [120, 180, 220, 350]
# ]

# for i in range(3):

#     discount = list(map(int, input("Enter discounts: ").split()))

#     for j in range(4):

#         if discount[j] >= 0:
#             if discount[j] <= 100:

#                 discount_amount = mrp[i][j] * discount[j] / 100
#                 selling_price = mrp[i][j] - discount_amount

#                 print(selling_price, end=" ")

#             else:
#                 print("Invalid", end=" ")

#         else:
#             print("Invalid", end=" ")

#     print()

# PSA question
# Write a Python program that takes a
# number as input and prints its square.

# n = int(input("Enter a number"))
# print(n * n)

# Write a Python program that takes a 
# number as input and calculates and prints its square root.

# n = int(input())

# for i in range(1, n + 1):
#     if i * i == n:
#         print(i)
#         break


# Write a Python program that takes a list of integers and 
# prints the sum of squares of all even numbers in the list.

# numbers = [1, 2, 3, 4, 5, 6]

# sum = 0

# for i in numbers:
#     if i % 2 == 0:
#         sum = sum + i * i

# print(sum)

# Write a Python program that takes a list of positive integers and prints
# the square root of the largest perfect square present in the list. Ignore numbers that are not perfect squares.

# numbers = [16, 25, 10, 49, 30, 81, 17]

# largest = 0

# for i in numbers:
#     for j in range(1, i + 1):
#         if j * j == i:
#             if i > largest:
#                 largest = i


# Question1 18 Aug 2026
# Age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")
# working_days = int(input("Enter your working days: "))

# if Age >= 18:
#     if Age <= 40:

#         if gender == "male":
#             wages = 700
#         else:
#             wages = 750

#         total_wages = wages * working_days
#         print(total_wages)

#     else:
#         print("Enter appropriate age")

# Question 2
# Age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")
# working_days = int(input("Enter your working days: "))

# for i in range(1, 5 + 1):
#     if Age >= 18:
#         if Age <= 40:

#             if gender == "male":
#                 wages = 700
#             else:
#                 wages = 750

#             total_wages = wages * working_days
#             print(total_wages)

#         else:
#             print("Enter appropriate age")

# PSA Question 20 Aug 2026

# Rockwell_hardness = int(input("Enter your Rockwell hardness: "))
# Carbon_content = float(input("Enter your Carbon content: "))
# Tensile_strength = int(input("Enter your Tensile strength: "))

# if Rockwell_hardness > 50 and Carbon_content > 0.7 and Tensile_strength > 5600:
#     print("Grade 10")

# elif Rockwell_hardness > 50 and Carbon_content > 0.7:
#     print("Grade 9")

# elif Carbon_content > 0.7 and Tensile_strength > 5600:
#     print("Grade 8")

# elif Rockwell_hardness > 50 and Tensile_strength > 5600:
#     print("Grade 7")

# else:
#     print("Grade 0")

# Question 2

# for steel in range(1, 6):
#     print("Steel : " , steel)
# Rockwell_hardness = int(input("Enter your Rockwell hardness: "))
# Carbon_content = float(input("Enter your Carbon content: "))
# Tensile_strength = int(input("Enter your Tensile strength: "))

# if Rockwell_hardness > 50 and Carbon_content > 0.7 and Tensile_strength > 5600:
#     print("Grade 10")

# elif Rockwell_hardness > 50 and Carbon_content > 0.7:
#     print("Grade 9")

# elif Carbon_content > 0.7 and Tensile_strength > 5600:
#     print("Grade 8")

# elif Rockwell_hardness > 50 and Tensile_strength > 5600:
#     print("Grade 7")

# else:
#     print("Grade 0")

# Question 3

# for production in range(1, 4):
#     print("Production : ", production)
#     for steel in range(1, 4):
#         print("Steel : ", steel)
# Rockwell_hardness = int(input("Enter your Rockwell hardness: "))
# Carbon_content = float(input("Enter your Carbon content: "))
# Tensile_strength = int(input("Enter your Tensile strength: "))

# if Rockwell_hardness > 50 and Carbon_content > 0.7 and Tensile_strength > 5600:
#     print("Grade 10")

# elif Rockwell_hardness > 50 and Carbon_content > 0.7:
#     print("Grade 9")

# elif Carbon_content > 0.7 and Tensile_strength > 5600:
#     print("Grade 8")

# elif Rockwell_hardness > 50 and Tensile_strength > 5600:
#     print("Grade 7")

# else:
#     print("Grade 0")


# PSA Question 21 Aug 2026
# Question 1

# n = int(input("Enter your number : "))
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# Question 2 
# n = int(input("Enter your number : "))
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# Question 3
# n = int(input("Enter your number : "))
# for i in range(n):
#     for j in range(i+1):
#         print(j + 1, end="")
#     print()

# Question 1 24 August 2026

# def ticket_price(age, is_weekend, has_student_card):

#     if age < 5:
#         price = 0

#     elif age <= 11:
#         price = 150

#     elif age >= 60:
#         price = 100

#     else:
#         price = 250

#     if is_weekend:
#         price = price + 50

#     if has_student_card:
#         if age >= 12:
#             if age < 60:
#                 price = price - 50

#     return price


# print(ticket_price(2, False, False))

# Question 2 

# usernames = ["riya","rinkinisha","amit","john"]
# longest_username = usernames[0]
# for user in usernames:
#     if len(user) > len(longest_username):
#         longest_username = user
#         print(longest_username)

# Question 3

# def check_palindrome(plate):

#     rev = ""

#     for i in range(len(plate) - 1, -1, -1):
#         rev = rev + plate[i]

#     return plate == rev


# print(check_palindrome("RACECAR"))
# print(check_palindrome("DL8CAF9"))


# PSA Question 26 August 2026

# arr = list(map(int,input().split()))
# freq = {}
# for num in arr:
#    if num in freq:
#     freq[num] = freq[num] + 1
#    else:
#      freq[num] = 1
# for num in freq:
#    print(num , ":" , freq[num])


# Question 2 

# arr = list(map(int,input().split()))
# target = int(input("Enter your Target: "))

# for i in arr:
#   sum = 0
#   for j in arr:
#     if i < j:
#         sum = i + j
#         if sum == target:
#             print(i, j)

# Question 3 

# arr = list(map(int,input().split()))
# target_arr = int(input("Enter your Target: "))
# max = 0
# for i in  range(1, len(arr)):
#     sum = 0
#     for j in range(i, len(arr)):
#         sum += arr[j]
#         if sum == target_arr:
#             length = j - 1 + i
#             if length > max:
#               max = length
# print(max)

# Question 31 Aug 2026

# Question 1

# n = list(map(int, input().split()))

# arr = []
# arr1 = []

# for i in n:
#     if i == 0:
#         arr = arr + [i]
#     else:
#         arr1 = arr1 + [i]

# array = arr + arr1

# print(array)

# Question 2

# n = int(input())

# a = 1
# b = 2

# if n == 1:
#     print(a)
# elif n == 2:
#     print(b)
# else:
#     for i in range(3, n + 1):
#         c = a + b
#         a = b
#         b = c

#     print(b)

# PSA Question 7 Sep 2026

# Question 1

# n = 5

# for i in range(n, 0, -1):

#     for j in range(i):
#         print("*", end="")

#     print()

# Question 2

# n = 5

# for i in range(1, n + 1):

#     for j in range(n - i):
#         print(" ", end=" ")

#     for j in range(i):
#         print("*", end=" ")

#     print()


# Question 3

# n = 5

# for i in range(n):
#     for j in range(n):

#         if i == 0:
#             print("*", end=" ")
#         elif i == n - 1:
#             print("*", end=" ")
#         elif j == 0:
#             print("*", end=" ")
#         elif j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()


# PSA Question 5 Sep 2026

# Question 1

# n = int(input())
# k = int(input())

# arr = list(map(int, input().split()))

# longest = 0

# for i in range(n):
#     total = 0

#     for j in range(i, n):
#         total = total + arr[j]

#         if total == k:
#             length = j - i + 1

#             if length > longest:
#                 longest = length

# print(longest)

# PSA Question 8 sep 2026

# Question 1

# key = {"apple": 30, "banana": 50, "mango": 45}

# largest = 0

# for value in key.values():
#     if value > largest:
#         largest = value

# print(largest)

# Question 2

# def find_max_min(num):
#     maximum = max(num)
#     minimum = min(num)
#     return maximum, minimum
# num = [4,2,9,1,7]
# result = find_max_min(num)
# print(result)


# Question 3

# arr = [1,2,3,1]
# k = 3
# seen = {}
# differ = 0
# for i in range(len(arr)):
#     if arr[i] in seen:
#         differ = i - seen[arr[i]]
#         if differ <= k:
#             print("true")
#         else:
#             print("false")
#     seen[arr[i]] = i


# PSA Question 14 Sep 2026

# Question 1

# runs = [6, 12, 8, 15, 9, 4]
# i = 0
# largest = runs[0]
# over = 0

# for i in range(len(runs)):
#     if runs[i] > largest:
#         largest = runs[i]
#         over = i 
#         i += 1
# print(over, largest)

# Question 2

# arr = [1, 2, -3, -1, 4, -5]

# positive = [0] * len(arr)
# negative = [0] * len(arr)

# p = 0
# n = 0

# for i in range(len(arr)):
#     if arr[i] >= 0:
#         positive[p] = arr[i]
#         p += 1
#     else:
#         negative[n] = arr[i]
#         n += 1

# result = [0] * len(arr)

# r = 0
# i = 0

# while i < p:
#     result[r] = positive[i]
#     r += 1

#     if i < n:
#         result[r] = negative[i]
#         r += 1

#     i += 1

# print(result)


# Question 3

# arr = [1, 2, 3, 4]

# result = [0] * len(arr)

# for i in range(len(arr)):

#     product = 1

#     for j in range(len(arr)):

#         if i != j:
#             product = product * arr[j]

#     result[i] = product

# print(result)

# PSA Question 15 Sep 2026

# Question 2

# sentence = "the quick brown fox"

# result = [0] * 4

# word = ""
# vowels = 0
# index = 0

# for i in range(len(sentence)):

#     if sentence[i] == " ":

#         result[index] = (word, vowels)
#         index += 1

#         word = ""
#         vowels = 0

#     else:

#         word = word + sentence[i]

#         if sentence[i] in "aeiouAEIOU":
#             vowels += 1

# result[index] = (word, vowels)

# print(result)

# Question 3

# n = 5

# for i in range(n):

#     for j in range(n):

#         if (i + j) % 2 == 0:
#             print("#", end="")
#         else:
#             print(".", end="")

#     print()


# PSA Question 17 Sep 2026

# Question 2

# num = 1234

# total = 0

# while num > 0:

#     digit = num % 10
#     total = total + digit

#     num = num // 10

# print(total)

# Question 3

# arr = [2, 7, 11, 15, 5, 9]
# target = 9

# result = [0] * len(arr)

# count = 0

# for i in range(len(arr)):

#     for j in range(i + 1, len(arr)):

#         if arr[i] + arr[j] == target:

#             result[count] = (i, j)
#             count = count + 1

# print(result[:count])


# Question 1

# runs = [1,4,0,2,6,1,0,4]
# total_score = 0
# boundaries = 0
# dot_balls = 0

# for run in runs:
#     total_score = total_score + run
#     if run == 4:
#         boundaries = boundaries + 1
#     if run == 6:
#         boundaries = boundaries + 1
#     if run == 0:
#         dot_balls = dot_balls + 1

# print("total_score: " ,total_score)
# print("Boundaries: ", boundaries)
# print("Dot_balls: ", dot_balls)


# PSA Question 18 Sep 2026

# Question 1

# arr = [1, -2, 0, 3, -4, 0 , 5]
# count_positive = 0
# count_negative = 0
# count_zero = 0

# for i in range(len(arr)):
#     if arr[i] == 0:
#         count_zero = count_zero + 1
#     elif arr[i] > 0:
#         count_positive = count_positive + 1
#     else:
#         count_negative = count_negative + 1
# print("Positive: ", count_positive)
# print("Negative: ", count_negative)
# print("Zero: ", count_zero)

# Question 2

# data = {"a": 1, "b": 2, "c": 3}
# result = {}

# for key in data:
#     value = data[key]
#     result[value] = key
# print(result)

# Questionn 3 

# sentence = "the quick brown fox and the lazy dog"

# small = ["the", "in", "on", "and", "but", "or"]

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# result = ""
# word = ""
# count = 0

# for ch in sentence:

#     if ch == " ":

#         count = count + 1

#         if count == 1:
#             result = result + upper[lower.index(word[0])]

#             for letter in word:
#                 if letter != word[0]:
#                     result = result + letter

#         elif word == "the":
#             result = result + word

#         elif word == "in":
#             result = result + word

#         elif word == "on":
#             result = result + word

#         elif word == "and":
#             result = result + word

#         elif word == "but":
#             result = result + word

#         elif word == "or":
#             result = result + word

#         else:
#             result = result + upper[lower.index(word[0])]

#             for letter in word:
#                 if letter != word[0]:
#                     result = result + letter

#         result = result + " "
#         word = ""

#     else:
#         word = word + ch

# print(result)

# PSA Question 21 Sep 2026

# Question 1

# speeds = [45, 52, 48, 61, 55, 72, 49]
# highest = speeds[0]
# lowest = speeds[0]
# total = 0
# count = 0
# above_60 = 0

# for speed in speeds:
#     if speed > highest:
#         highest = speed
#     if speed < lowest:
#         lowest = speed
#     if speed > 60:
#         above_60 = above_60 + 1

#     total = total + speed
#     count = count + 1

# average = total/count

# print("HIghest speed: ", highest)
# print("Lowest speed: ", lowest)
# print("Above_60: ", above_60)
# print("Average speed: ", average)

# Question 2

# message = "meet me at the old bridge at midnight"

# word = ""
# count_e = 0
# longest = ""
# long_words = 0
# two_e = ""

# for ch in message:

#     if ch == " ":

#         has_e = 0
#         e_count = 0

#         for letter in word:
#             if letter == "e":
#                 has_e = 1
#                 e_count = e_count + 1

#         if has_e == 1:
#             count_e = count_e + 1

#         if len(word) > len(longest):
#             longest = word

#         if len(word) > 4:
#             long_words = long_words + 1

#         if e_count >= 2:
#             two_e = two_e + word + " "

#         word = ""

#     else:
#         word = word + ch


# print("Words containing e:", count_e)
# print("Longest word:", longest)
# print("Words longer than 4:", long_words)
# print("Words with 2+ e:", two_e)

# Question 3
# battery_usage = [12, 8, 15, 20, 7, 18, 10]

# battery = 100
# highest = 0
# location = 0
# step = 0

# for usage in battery_usage:

#     step = step + 1
#     battery = battery - usage

#     if usage > highest:
#         highest = usage
#         location = step

#     if battery <= 20:
#         print("LOW BATTERY")

#     if battery <= 0:
#         break

# print("Final Battery:", battery, "%")
# print("Highest Consumption:", highest, "%")
# print("At Location:", location)


# PSA Question 22 Sep 2026

# arr = [14, 7, 22, 9, 31, 16, 5, 28]
# sum_even = 0
# sum_odd = 0
# difference = 0

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         sum_even = sum_even + arr[i]
#     else:
#         sum_odd = sum_odd + arr[i]

# difference = sum_even - sum_odd

# if sum_even > sum_odd:
#     print("Larger Total: ","Even", sum_even)
# else:
#     print("Larger Total: ", "Odd", sum_odd)

# print("Even Total: ",sum_even)
# print("Odd Total: ", sum_odd)
# print("Difference: ", difference)

# Question 3


# balance = 5000

# transactions = [1200, -500, 800, -2000, 1500, -700]

# largest_deposit = 0
# largest_withdrawal = 0
# count = 0

# for transaction in transactions:

#     count = count + 1
#     balance = balance + transaction

#     print("After transaction", count, ":", balance)

#     if transaction > 0:

#         if transaction > largest_deposit:
#             largest_deposit = transaction

#     else:

#         withdrawal = -transaction

#         if withdrawal > largest_withdrawal:
#             largest_withdrawal = withdrawal

#     if balance < 1000:
#         print("Warning: Low Balance")

# print("Largest Deposit:", largest_deposit)
# print("Largest Withdrawal:", largest_withdrawal)
# print("Final Balance:", balance)


# usernames = ["  Nitin ", "RAHUL  ", "  priya", "Amit ", "  Kiran  "]

# count = 0

# for username in usernames:

#     word = ""

#     for ch in username:
#         if ch != " ":
#             word = word + ch

#     first = word[0]
#     result = ""

#     if first == "n" or first == "N":
#         result = "N"
#     elif first == "r" or first == "R":
#         result = "R"
#     elif first == "p" or first == "P":
#         result = "P"
#     elif first == "a" or first == "A":
#         result = "A"
#     elif first == "k" or first == "K":
#         result = "K"

#     for i in range(1, len(word)):
#         ch = word[i]

#         if ch == "I":
#             ch = "i"

#         result = result + ch

#     print(result)

#     for ch in word:
#         if ch == "i" or ch == "I":
#             count = count + 1
#             break

# print("Users containing i:", count)


# PSA Question 24 Sep 2026

# Question 1

# seats = ["A12", "B07", "C15", "A03", "D09", "B14"]

# row_a = 0
# total = 0

# for seat in seats:

#     row = seat[0]
#     number = int(seat[1] + seat[2])

#     print(row, "->", number)

#     if row == "A":
#         row_a = row_a + 1

#     total = total + number

# print("Row A Seats:", row_a)
# print("Total Seat Numbers:", total)

# Question 2

# passwords = ["cat123", "HELLO", "robot42", "sun", "Python99"]

# strong = 0
# digits = "0123456789"

# for password in passwords:

#     count = 0
#     digit = 0

#     for ch in password:
#         count = count + 1

#         if ch in digits:
#             digit = 1

#     if count >= 6:
#         if digit == 1:
#             print(password, "-> Strong")
#             strong = strong + 1
#         else:
#             print(password, "-> Weak")
#     else:
#         print(password, "-> Weak")

# print("Strong Passwords:", strong)

# Question 3

# distances = [5, 8, 3, 12, 7, 10, 4]

# energy = 100
# total = 0
# longest = 0
# location = 0
# count = 0

# for distance in distances:

#     count = count + 1

#     used = distance * 2
#     energy = energy - used

#     print("Checkpoint", count, ":", energy)

#     if energy <= 20:
#         print("Energy Critical")

#     total = total + distance

#     if distance > longest:
#         longest = distance
#         location = count

# print("Total Distance:", total, "km")
# print("Longest Distance:", longest, "km")
# print("Longest Distance At Checkpoint:", location)
# print("Final Energy:", energy)

# PSA question 25 Sep 2026

# Question 1


# word = "python"

# score = 0
# vowels = "aeiou"

# for ch in word:

#     if ch in vowels:
#         points = 2
#     else:
#         points = 1

#     print(ch, "->", points)
#     score = score + points

# print("Total Score:", score)

# Question 2

# temperatures = [28, 31, 29, 29, 33, 30, 35]

# previous = temperatures[0]
# day = 1

# for temp in temperatures:
    
#     if day > 1:
        
#         change = temp - previous

#         if change > 0:
#             print("Day", day, ": Increased by", change)

#         elif change < 0:
#             print("Day", day, ": Decreased by", -change)

#         else:
#             print("Day", day, ": No Change")

#     previous = temp
#     day = day + 1

# PSA Question 28 Sep 2026

# Question 1

# N = 5

# for i in range(2):
#     for j in range(1, N + 1):
#         print(j, end=" ")

#     for j in range(N, 0, -1):
#         print(j, end=" ")

#     print()

# Question 2

# N = 5

# for i in range(1, N + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Question 3

# amount = int(input("Enter your amount: "))

# if amount < 1000:
#     discount = 0

# elif amount < 5000:
#     discount = 5

# elif amount < 10000:
#     discount = 10

# else:
#     discount = 15

# final_amount = amount - (amount * discount / 100)

# print("Final Amount:", final_amount)


# s = "MCMXCIV"

# values = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# total = 0
# previous = 0

# for i in range(len(s) - 1, -1, -1):
#     current = values[s[i]]

#     if current < previous:
#         total = total - current
#     else:
#         total = total + current

#     previous = current

# print(total)

# columnNumber = int(input("Enter number: "))

# result = ""

# while columnNumber > 0:
#     columnNumber = columnNumber - 1
#     remainder = columnNumber % 26
#     letter = chr(65 + remainder)
#     result = letter + result
#     columnNumber = columnNumber // 26

# print(result)

# PSA Question 19 Oct 2026
#  Question 1 

n = 1234
total = 0

while n > 0:
    last_digit = n % 10
    total = total + last_digit
    n = n // 10

print(total)


