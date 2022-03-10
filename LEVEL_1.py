#               ++++++++++++++++++++++++++++ LEVEL 1 +++++++++++++++++++++++++++++++++++++

# Q OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
#
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    # INDEXING THE 1ST LETTER

    first_letter = name[0]

    # dividing the program is the like this would be easy
    # INDEXING THE INBETWEEN LETTERS IN name

    letter_inbetween = name[1:3]

    # INDEXING FOURTH LETTER

    fourth_letter = name[3]

    # INDEXING REST OF THE LETTERS

    rest_letter = name[4:]

    for x in name:
        first_letter = first_letter.upper()
        fourth_letter = fourth_letter.upper()
    return first_letter+letter_inbetween+fourth_letter+rest_letter


print(old_macdonald("macdonald"))

# OTHER METHOD. SHORT ONE BY USING .capitalize() method
# Note: 'macdonald'.capitalize() returns 'Macdonald' ie name[0] would be in capital


def old_mac(name):
    first_half= name[:3]
    second_half = name[3:]
    return first_half.capitalize()+second_half.capitalize()

print(old_mac("macdonald"))


# Q MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    # SPLIT THE TEXT
    new_text = text.split()
    # REVERSE THE NEW TEXT
    reverse_text = new_text[::-1]  # [::-1 ] REVERSING THE WHOLE STATEMENT NO MATTER HOW LON IT IS
    return " ".join(reverse_text)

print(master_yoda(text="I AM HOME"))
print(master_yoda(text="WE ARE READY NOE JJ OL EED SFADFF"))


# Q ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# it means weathe rthe difference bw the input no. and 100 or 200 is <=10 ie within 10.
# almost_there(90) --> True  #90-100  10
# almost_there(104) --> True  # 100-104 -1
# almost_there(150) --> False  >> -50  50
# almost_there(209) --> True   >> -9

# since some values are in -ve so we can use abs(num) method in function.

def almost_there(num):
    return (abs(100-num) <=10 ) or (abs(200-num) <= 10)

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
