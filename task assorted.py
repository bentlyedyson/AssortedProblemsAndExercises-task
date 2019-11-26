#1
def max0(x,y):
    if x > y:
        print(x)
    else:
        print(y)        

max0(5,6)

#2
def max1(x,y,z):
    if x > y and z:
        print(x)
        if y > x and z:
            print(y)
    else:
        print(z)

max1(1,2,3)
#3 
def length_of_string(arrayName):
    x = 0 
    for i in arrayName:
        x = x + 1 
    print("The length of this string is " + str(x) + ".")
    return x

length_of_string("bently")

#4 
def character(x):

    vowels = ["a","i","u","e","o"]
    for i in vowels:
        if i == x: 
            return True
    return False

print(character('a'))

#5

def reverse(s):
    s = s [::-1]
    return s

s = " I am something"

print("The reversed result is", end="")
print(reverse(s))

#6

def reverse(a):
    return a[::-1]

def is_palindrome(a):
    rev = reverse(a)
    if (a == rev):
        return True
    return False

a = "sugus"
ans = is_palindrome(a)
if ans == 1:
    print("True")
else:
    print("False")




