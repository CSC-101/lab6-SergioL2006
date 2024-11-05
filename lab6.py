from pickle import PROTO

import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> list:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp
    return values


# Part 1
from data import Book
#Sorts the books in alphabetical order
def selection_sort_books(books:list[Book]) -> list[Book]:
    #Created a list of letters to assign numbers in terms of index and empty list for index
    alphabetList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    titleNumbered = []
    holder = books
    #Begin by turning the beginning letters of each title into a number to compare
    for y in books:
        i = 0
        while i < len(alphabetList):
            if list(y.title)[0] == alphabetList[i]:
                titleNumbered.append(i)
                break
            i += 1
    #Use selection sort to sort the list based on their first letters idx
    for x in range(len(books)-1):
        smallidx = x
        for j in range(x+1, len(books)):
            if titleNumbered[j] <= titleNumbered[smallidx]:
                smallidx = j

            if smallidx != x:
                temp = books[x]
                books[x] = books[smallidx]
                books[smallidx] = temp
                break
    return books

# Part 2
#Swaps the uppercases for lowercases
def swap_case(string:str) -> str:
    #Create an ew string value
    newstring = ''
    #Each if statement is a check if it is upper or lower going down the letters
    for x in string:
        if x.isupper():
            newstring += x.lower()
        elif x.islower():
            newstring += x.upper()
        else:
            newstring += x
    #Each iteration adds the new value and if it is not an upper or lower just adds the symbol

    return newstring

# Part 3
#translates the old letters into new letters
def str_translate(string:str, old:str, new:str) -> str:
    #begin with the list of the word
    newstring = list(string)
    #checks if the letter in the list is equal to old then switches to new
    for x in range(len(newstring)):
        if string[x] == old:
            newstring[x] = new
    #In the end joins the list together
    return ''.join(newstring)

# Part 4
#Creats a dictionary of how many times a word appears in a list
def histogram(string:str) -> dict:
    #Create two new var's one for a list of the words split and the histogram
    splitstr = string.split()
    histo = {}
    #Checks if the word is in the histogram, if not adds it with a count of 1
    for x in splitstr:
        if x not in histo:
            histo[x] = 1
        #If it is in the histogram adds +1 to the count in how many times it appears
        elif x in histo:
            histo[x] += 1

    return histo
