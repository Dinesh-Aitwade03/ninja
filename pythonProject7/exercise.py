
#  webside-------   https://www.w3resource.com/python-exercises/

# 2. Write a Python program to find out what version of Python you are using.
# import sys
# print(sys.version)

# 3. Write a Python program to display the current date and time.
# import datetime
# print(datetime.datetime.now())

# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# from math import pi
#
# redius = int(input('enter the redius :'))
# print('area of circle is :',pi*redius**2)

# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order
# with a space between them.

# sname = 'Dinesh Aitwade'
# name = sname.split(' ')
# revname = name[::-1]
# print(' '.join(revname))
#---------------------
# fname = 'Dinesh'
# lname = 'Aitwade'
# print(lname+' '+fname)

# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and
# generates a list and a tuple of those numbers.

# inpt = list(input('enter the number: '))
# lst = list(inpt)
# tupl = tuple(inpt)
# print(lst,tupl)
# --------------------------------------------------------
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.

# flname = input('Enter file name:')
# pos_of_dot = flname.find('.')
# print(flname[pos_of_dot+1:])
# -------------------------------------------------------------
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print("The extension of the file is : " + repr(f_extns[-1]))


# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0])
# print((color_list[-1]))

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# exam_st_date = (11,12,2014)
# print("The examination will start from : %i / %i / %i"%exam_st_date)


# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# n = int(input('enter value: '))
# n2 =int('%s%s'%(n,n))
# n3 = int('%s%s%s'%(n,n,n))
# print(n+n2+n3)

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s)
# print(abs.__doc__)
# print('--------------------')
# print(any.__doc__)
# print('--------------------')
# print(ascii.__doc__)
# print('--------------------')
# print(bytearray.__doc__)
# print('--------------------')
# print(len.__doc__)
# print('--------------------')
# print(open.__doc__)


# 12. Write a Python program that prints the calendar for a given month and year.
# import calendar
# m = int(input('enter month: '))
# y = int(input('enter year : '))
# print(calendar.month(y,m))

# 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# from datetime import date
# f_date = date(2023,2,3)
# pre_date = date(1993,12,3)
# diff = f_date-pre_date
# print(diff.days)
# print(diff.days/365)

# 15. Write a Python program to get the volume of a sphere with radius six.
# from math import pi
#
# r=6.0
# print(4.0/3.0*pi*r**3)

# 16. Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference

# f_number = int(input('enter number: '))
# s_num = 17
#
# if f_number>17:
#     print((f_number-s_num)*2)
# else:
#     print(s_num-f_number)


# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000
# numm = int(input('enter number: '))
# if (1000-numm)<=100  or (2000-numm)<=100:
#     print(True)
# else:
#     print(False)
# ---------------------------------
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#
#
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))

# 18. Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.

# num1 = int(input('  :'))
# num2 = int(input('  :'))
# num3 = int(input('  :'))
# if num3==num2==num1:
#     print((num3+num2+num1)*3)
# else:
#     print(num3+num2+num1)
#
# ---------------------------------------
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))


# 19. Write a Python program to get a newly-generated string from a given string
# where "Is" has been added to the front.
# Return the string unchanged if the given string already begins with "Is".

# str = 'Is this is code'
# if str.startswith('Is'):
#     print(str)
# else:
#     print('Is'+ str)

# ---------------------------
# def new_string(text):
#   if len(text) >= 2 and text [:2] == "Is":
#     return text
#   return "Is" + text
# print(new_string("Array"))
# print(new_string("IsEmpty"))


# 20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string

# strr = 'Dinesh'
# n = 10
# print(strr*10)
# -----------------------------
# def larger_string(text, n):
#    result = ""
#    for i in range(n):
#       result = result + text
#    return result
# print(larger_string('abc', 2))
#


# 21. Write a Python program that determines whether a given number (accepted from the user)
# is even or odd, and prints an appropriate message to the user.

# numberr = int(input('enter the num : '))
# if numberr%2==0:
#     print('The given number is EVEN')
# else:
#     print('The given number is ODD')

# ------------------------------
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")


# 22. Write a Python program to count the number 4 in a given list.

# ls = [1,2,5,4,6,4,5,8,1,4,2,36,5]
# print(ls.count(4))
# ----------------------------------------------------
# def list_count_4(nums):
#   count = 0
#   for num in nums:
#     if num == 4:
#       count = count + 1
#
#   return count
#
# print(list_count_4([1, 4, 6, 7, 4]))
# print(list_count_4([1, 4, 6, 4, 7, 4]))


# 23. Write a Python program to get n (non-negative integer) copies of
# the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2
# strr = input('enter the string: ')
# n = int(input('n='))
# if len(strr)<=2:
#     print(strr*n)
# else:
#     print(strr[0:2]*n)

# ------------------------------------------------------
# def substring_copy(text, n):
#   flen = 2
#   if flen > len(text):
#     flen = len(text)
#   substr = text[:flen]
#   result = ""
#   for i in range(n):
#     result = result + substr
#   return result
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));


# 24. Write a Python program to test whether a passed letter is a vowel or not
# def ovel(ch):
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#         print('Given character is OVEL')
#     else:
#         print('Given character is NOT OVEL')
#
# ovel('a')
# ovel('z')
# ovel('m')
# --------------------------------------
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))


# 25. Write a Python program that checks whether a specified value is contained within a group of values.

# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# a1 = [1,5,8,3]
# val = int(input('--='))
# if val in a1:
#     print(True)
# else:
#     print(False)
# ---------------------------------------------
# def is_group_member(group_data, n):
#    for value in group_data:
#        if n == value:
#            return True
#    return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))


# 26. Write a Python program to create a histogram from a given list of integers
# def histo(lss):
#     for i in lss:
#         print(i*'*')
#
# histo([2,3,5,6])
# -------------------------------------------
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
#
# histogram([2, 3, 6, 5])


# 27. Write a Python program that concatenates all elements in a list into a string and returns it
# lt = [1,2,'dinesh','Don']
# newstr = ''
# for i in lt:
#     i=str(i)
#     newstr = newstr + i
# print(newstr)
# -----------------------------------------------
# def concatenate_list_data(list):
#     result= ''
#     for element in list:
#         result += str(element)
#     return result
#
# print(concatenate_list_data([1, 5, 12, 2]))


# 28. Write a Python program to print all even numbers from a given list of numbers in the same order and
# stop printing any after 237 in the sequence.
# Sample numbers list :

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#                 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]

# for i in numbers:
#     if i==237:
#         print(i)
#         break
#     if i%2==0:
#         print(i)

# 29. Write a Python program that prints out all colors from color_list_1 that
# are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

# print(color_list_1.difference(color_list_2))
# print(color_list_2.difference(color_list_1))


# 30. Write a Python program that will accept the base and height of a triangle and compute its area.

# def area_trangle(base,hight):
#     result = (base*hight/2)
#     print(result)
#
# area_trangle(2,3)
# area_trangle(6,5)
# area_trangle(5,10)

# 31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
# def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))
# ------------------------------------------------------
# def gcd(x, y):
#
#     z = x % y
#     while z:
#         x = y
#         y = z
#         z = x % y
#     return y
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))
# -----------------------------------------------------------
# num1 = int(input('enter first num: '))
# num2 = int(input('enter second num: '))
# if num1>num2:
#     min = num2
# else:
#     min = num1
#
# for i in range(1,min+1):
#     if num1%i==0 and num2%i==0:
#         gcd = i
# print('gcd=',gcd)

# 32. Write a Python program to find the least common multiple (LCM) of two positive integers.

# def lcm(num1,num2):
#
#     if num1>num2:
#         min = num2
    #     max = num1
    # else:
    #     min = num1
    #     max = num2
    # lst = []
    # for i in range(max,min*max+1):
    #     if i%min==0 and i%max==0:
#             lst.append(i)
#     print(lst[0])
#
# lcm(10,20)
# lcm(6,4)
# lcm(15,17)
# lcm(11,13)
# lcm(12,24)
# ---------------------------------------------------
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))

# 33. Write a Python program to sum three given integers. However, if two values are equal,
# the sum will be zero.#

# int1 = int(input('enter 1st number:= '))
# int2 = int(input('enter 2st number:= '))
# int3 = int(input('enter 3st number:= '))
#
# if int1==int2 or int2==int3 or int1==int3:
#     print('sum is = 0')
# else:
#     print('sum = ',int2+int3+int1)

# 34. Write a Python program to sum two given integers.
# However, if the sum is between 15 and 20 it will return 20.

# int1 = int(input('enter 1st number:= '))
# int2 = int(input('enter 2st number:= '))
#
# sum = int1+int2
# if sum>15 and sum<20:
#     print(20)
# else:
#     print(sum)

#35. Write a Python program that returns true if the two given
# integer values are equal or their
#   sum or difference is 5

# num1 = int(input("enter first value:"))
# num2 = int(input("enter the value2 : "))
# if num1==num2:
#     print("True")
# elif num2+num1==5:
#     print("True")
# elif num2-num1==5 or num1-num2==5:
#     print("True")
# else:
#     print("False")
# ---------------------
# def atest1_number5(x,y):
#    if x == y or abs(x-y) == 5 or (x+y) == 5:
#        return True
#    else:
#        return False
# print(atest1_number5(7, 2))
# print(atest1_number5(3, 2))
# print(atest1_number5(2, 2))
# print(atest1_number5(7, 3))
# print(atest1_number5(27, 53))

# 36. Write a Python program to add two objects if both objects are integers.
# a=10
# b=20
# if type(a)==int and type(b)==int:
#     print(a+b)
# else:
#     print("can not add these values")
# ------------------------------------------
# def add_numbers(a, b):
#    if not (isinstance(a, int) and isinstance(b, int)):
#        return "Inputs must be integers!"
#    return a + b
# print(add_numbers(10, 20))
# print(add_numbers(10, 20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))

# 37. Write a Python program that displays your name, age, and address
# on three different lines
# print("Dinesh  \n age-29\n Bombay")
# -------------------------------
# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#
# personal_details()


# 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

# def solve(x,y):
#     return (x+y)*(x+y)
# print(solve(4,3))

# 39. Write a Python program to compute the future value of a specified principal amount,
# rate of interest, and number of years. Go to the editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

# def r_i(amt,intr,yr):
#     print((amt*(1+intr/100)**yr))
#
# r_i(10000,3.5,7)

# 40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
#
# print(distance)

# 41. Write a Python program to check whether a file exists.
# import os
# print(os.path.isfile(a.py))

# 42. Write a Python program to determine if a Python
#    shell is executing in 32bit or 64bit mode on OS.#

# import struct
# print(struct.calcsize("P") * 8)

# 43. Write a Python program to get OS name, platform and release information.
# import platform
# import os
# print("Name of the operating system:",os.name)
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())

# 44. Write a Python program to locate Python site packages.
# import site;
# print(site.getsitepackages())

# 45. Write a Python program that calls an external command.
# from subprocess import call
# call(["ls", "-l"])

# 46. Write a Python program to retrieve the path and name of the file currently being executed.
# import os
# print("Current File Name : ",os.path.realpath(__file__))

# 47. Write a Python program to find out the number of CPUs used.
# import multiprocessing
# print(multiprocessing.cpu_count())

# 48. Write a Python program to parse a string to float or integer.
# n = "246.2458"
# print(float(n))
# print(int(float(n)))

# 49. Write a Python program to list all files in a directory.
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list);

# 50. Write a Python program to print without a newline or space.
# for i in range(0, 10):
#     print('*', end="")
# print("\n")

