# print('' ****"Program 1",  ******)

# print("Get Odd Numbers")

# print("1.a. List Comprehension")
start, stop = 0, 100
odd_numbers = [i for i in range(start, stop + 1) if i % 2]
print(f"The list of odd numbers using list comprehension are: {odd_numbers}")

# print( "1.b. Normal Loop")


def odd_gen(start, end):
    for i in range(start, end + 1):
        if i % 2:
            yield i
        else:
            ...


print(f"The list of odd numbers using normal loop are: {list(odd_gen(0, 100))}")

# print( "1.c. Generator Mechanism")


def odd_gen(start, end):
    for i in range(start, end + 1):
        if i % 2:
            yield i
        else:
            ...


print(f"The list of odd numbers using generator mechanism are: {list(odd_gen(0, 100))}")

# print("****************QUESTION 1**************************")

# print(" Implement palindrome using iterator(for loop) and generator mechanism.")


def is_palindrome(pal):
    for i in range(0, int(len(pal) / 2)):
        if pal[i] != pal[len(pal) - i - 1]:
            return False
        else:
            return True


print(is_palindrome("nitin"))
print()
print("2. Sum of 2 digits into output")
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num1 = list(str(num1))
num2 = list(str(num2))


def sum_of_two_numbers(n1, n2):
    return int(n1) + int(n2)


x = list(map(sum_of_two_numbers, num1, num2))
print(sum(x))
# print( "3. Reverse string considering only alphabets. Symobls should not be reversed")
print()
def reverse_string(st):
    return ' '.join(reverse_word(word) for word in st.split())

def reverse_word(st):
    stack = []
    for el in st:
        if el.isalpha():
            stack.append(el)
    result = ''
    for el in st:
        if el.isalpha():
            result += stack.pop()
        else:
            result += el
    return result

instr = 'fe@#dc!ba'

print(reverse_string(instr))
print()

# print(**************"4. findout elements duplicate count output in  dict format"**********)
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
di = dict()
for val in some_list:
    di.setdefault(val, (some_list.count(val)))
print(f"The count of duplicates are: {di}")
print()

# print( "5. -------QUESTION 5-------------------")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break

print(lis1)
print()

# print( "6. Write a Python program to remove leading zeros from an IP address.")

inp = "216.08.094.196"
x = inp.replace('0', '')
print(f"IP address after removing zeros is: {x}")
print()

# print( "7. -----------QUESTION 7---------------")

lis = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]


def rec(l):
    li = []
    for i in l:
        if isinstance(i, int):
            li.append(i)
        elif isinstance(i, list):
            x = rec(i)
            li.extend(x)
    return li


print(rec(lis))
print()
# # print( "8. Load sample content in text file.")
'''1.No of lines in file '''

with open(r"C:/Users/Dell/Desktop/django commad.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
#
# '''2.No of words in each line '''
#
file = open("C:/Users/Dell/Desktop/django commad.txt", "r")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))
#
# '''3. No of chars in each line '''
#
file = open("C:/Users/Dell/Desktop/django commad.txt" ,"r")
data = file.read()
#get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)

# ''' 4. No of vowels and consonants'''

fileName = input("Enter the file to check: ").strip()
infile = open(fileName, "r")
vowels = set("A E I O U a e i o u")
cons = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")
text = infile.read().split()
countV = 0
for V in text:
    if V in vowels:
        countV += 1
countC = 0
for C in text:
    if C in cons:
        countC += 1
print("The number of Vowels is: ",countV,"\nThe number of consonants is: ",countC)