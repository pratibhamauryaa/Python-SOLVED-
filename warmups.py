# ^^^^^^^^^^^^^^^^^^^^^^^^^^^WARMUP FUNCTION EXERCISE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# LEVEL 1
# Q1 LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd

def less_ofeven(a,b):
    if a%2==0 and b%2 ==0:
        print(min(a,b))
    elif a%2!= 0 or b%2!=0:
        print(max(a,b))
    else:
        pass

print(less_ofeven(2,4))

print(less_ofeven(2,5))


# Q2 ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(string1,string2):
    if string1[0]== string2[0]:
        return True
    else:
        return False


print(animal_crackers(string1="leveheaded",string2="lama"))


print(animal_crackers(string1="crazy",string2="kangaroo"))



# Q3 MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a,b):
    if a+b == 20 or a==20 or b==20:
        return True
    else:
        return False


print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
