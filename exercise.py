# # 1
# for i in range(1500, 2701):
#     if i % 7== 0 and i % 5 ==0:
#         print(i, end=",")
#
# # 2 Celsius to Fehrenheit
# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]
#
# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")
#----------------------------------------------------------------
# guess game
# import random
# while True:
#     guess = int(input("Guess the the number between 1 - 9"))
#     if guess in range(1,10):
#         break
#         print("Guess must be between 1-9")
# random_number = int(random.randint(1,10))
# counter = 1
# while random_number != guess or counter >3:
#     counter = counter + 1
#     guess = int(input("Try again"))
#     if counter > 2:
#         print("Too many guesses")
#         quit()
# print("great job")
# ----------------------------------------------------------------
# loop exercise
# for line in range(5):
#     for column in range(line):
#             print('X ', end=" ")
#     print()
# for line in range(5, 0, -1):
#     for column in range(line):
#             print('X ', end=" ")
#     print()
# ----------------------------------------------------------------
#reverse the word
# word = input("Enter a word")
# #if i print range(len(word) the output will be [0,X] i want print allways the last letter of the word. so i need start with word[-1] and remove allways 1 from word.
#
# for letter in range(len(word)-1, -1, -1):
#     print(word[letter], end="")
# print()
# ----------------------------------------------------------------
# how many numbers even or odd
# list = range(1, 10)
# even = 0
# odd = 0
# for i in list:
#     if i % 2 == 0:
#         even =even + 1
#     else:
#         odd = odd + 1
# print(f'number of even numbers: {even}')
# print(f'number of odd numbers: {odd}')
#----------------------------------------------------------------
# variavles = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],{"class":'V', "section":'A'}]
# for item in variavles:
#     print((f'type of"  {item} is {type(item)}'))
# ----------------------------------------------------------------
# for i in range(0,7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i, end=' ')
# ----------------------------------------------------------------
# # fibonacci
# num1, num2 = 0, 1
# while num2 < 50:
#     print(num2, end=' ')
#     num1, num2 = num2, num1+num2
# # FizzBuzz game
# # for number in range(0,50):
# #     if number % 3==0 and number % 5 == 0:
# #         print('FizzBuzz')
# #     elif number % 5==0:
# #         print('Buzz')
# #     elif number % 3 ==0:
# #         print('Fizz')
# #     else:
# #         print(number)
import random
def unique_random_range_no_lib_no_module_no_shuffle(start, end, n):
    if n > (end - start + 1):
        raise ValueError("n should be less than or equal to end-start+1")
    numbers = list(range(start, end + 1))
    for i in range(len(numbers) - 1, 0, -1):
        j = int(i * float(random.randint(0, 0x7fff)) / (0x7fff + 1))
        numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers[:n]
print(unique_random_range_no_lib_no_module_no_shuffle(1, 10,6))
