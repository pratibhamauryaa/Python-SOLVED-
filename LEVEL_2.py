# ^^^^^^^^^^^^^^^^^^^^^^^^^^^ LEVEL 2 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Q FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(*num):
    # DEFINE A RANGE 0 TO N-1
    for x in range(0,len(num)-1):
        if num[x]==3 and num[x+1]==3:
            return True
    return False

print(has_33(3, 1, 3))

# Q PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result = " "            # is to declare an empty string
    for x in text:
        result += x * 3     # get the hang of it.
    return result


text = 'Hello'
print(paper_doll(text))


# Q BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


# DEFINE FUNC BLACKJACK
def balckjack(a,b,c):
    # CHECK IF SUM<=21
    sum = a+b+c   # could hav eused build in sum func-- sum([a,b,c])
    if sum <=21:
        return sum
    # CHECK IS SUM >21 AMD 11 IS THERE?
    elif 11 in [a,b,c] and sum -10 <= 21:  # ??????????
        return sum - 10
    else:
        return "bust"

print(balckjack(5,6,7))
print(balckjack(9,9,9))
print(balckjack(9,9,11))


# Q SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# DEF SUMMER69
def summer_69(arr):
    output = 0 # initially --->Return 0 for no numbers given in ques.
    add = True
    for x in arr:
        # CHECK IF 6 IS NOT THERE
        while add:
            if x!=6:
                output += arr
                break             # GOING BACK  TO FOR LOOP
            else:
                add = False
        while not add:           # add is false
            if x!=9:
                break
            else:
                add = True
                break
    return output
arr = (1,6,8,7,9,5)

print(summer_69(arr))

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^CHALLENGE PROBLEM^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Q- SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False



num = [1,3,4,0,0,7,8,9,6]
print(spy_game(num))

# Q = COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to
# and including a given number
