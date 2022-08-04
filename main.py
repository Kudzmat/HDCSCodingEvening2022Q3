"""
Create a function that, given a string with at least three characters, returns an array of its:

Length.
First character.
Last character.
Middle character, if the string has an odd number of characters. Middle TWO characters, if the string has an even number of characters.
Index of the second occurrence of the second character in the format "@ index #" and "not found" if the second character
doesn't occur again.


Examples
allAboutStrings("LASA") ➞ [4, "L", "A", "AS", "@ index 3"]

allAboutStrings("Computer") ➞ [8, "C", "r", "pu", "not found"]

allAboutStrings("Science") ➞ [7, "S", "e", "e", "@ index 5"]
"""


def all_about_strings(my_string):
    string_list = []  # function will return this list

    # length of string
    string_len = len(my_string)
    string_list.append(string_len)

    # first character
    first_char = my_string[0]
    string_list.append(first_char)

    # last character
    last_char = my_string[-1]
    string_list.append(last_char)

    # middle character
    mid_char = ""

    # if string is an even number in length
    if string_len % 2 == 0:
        mid = string_len // 2  # // so we don't get the remainder
        mid_char = my_string[mid - 1] + my_string[mid]  # concatenating the two characters
        string_list.append(mid_char)

    # if string is an odd number
    else:
        mid = string_len // 2  # // so we don't get the remainder
        mid_char = my_string[mid]
        string_list.append(mid_char)

    # index of the second occurrence of the second character
    occurrence = ""
    char = my_string[1]  # the character we are looking for
    word = my_string[2:]  # creating a new word from my_string which excludes the first 2 characters

    if char in word:
        index1 = word.index(char)  # using .index() to get the index of char
        # adding 2 ( derived from the first 2 characters I excluded) to the index that I get from index1
        index = index1 + 2
        occurrence += f"@ index {index}"
        string_list.append(occurrence)

    else:
        occurrence += "not found"
        string_list.append(occurrence)

    return string_list


# test cases
tests = ["LASA", "Computer", "Science"]

for test in tests:
    print(all_about_strings(test))
