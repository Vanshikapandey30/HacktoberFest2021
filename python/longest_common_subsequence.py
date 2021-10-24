"""
Dynamic Programming (DP) : Algorithm for finding Longest Common subsequence in python

LONGEST COMMON SUBSEQUENCE PROBLEM:  Given two strings, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order and NOT necessarily continuous.

Name: Atharva Patil
Github Profile link:  https://github.com/atharvapatil123 
"""
"""
Parameters

string1: 1st string
string2: 2nd string
n: length of string1 
m: length of string2
"""

from typing import Tuple

def longest_common_subsequence(
    string1: str, string2: str, len_of_string1: int, len_of_string2: int
) -> Tuple[str, int]: 


    """
    >>> longest_common_subsequence("coding", "code", 6, 4)
    (3, 'cod')

    >>> longest_common_subsequence("roadies", "moodies", 7, 7)
    (5, 'odies')

    >>> longest_common_subsequence("no", "yes", 2, 3)
    (0, '')

    """

    res = (
        0  # res variable is used to store the result: Maximum length of common subtring
    )
    string = ""  # string is used to store the longest common subsequence

    """
    Create a table to store Longest Common suffixes 
    Initially, all cells are initialized with -1
    """
    table = [[-1 for i in range(len_of_string2 + 1)] for j in range(len_of_string1 + 1)]

    # Making first row and column entirely 0
    for i in range(len_of_string1 + 1):
        for j in range(len_of_string2 + 1):
            if i == 0 or j == 0: 
                table[i][j] = 0


    for i in range(1, len_of_string1 + 1):
        for j in range(1, len_of_string2 + 1):

            if(string1[i - 1] == string2[j - 1]):

                table[i][j] = 1 + table[i - 1][j - 1]
                if(table[i][j] > res):
                    res = table[i][j]

            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

    i = len_of_string1
    j = len_of_string2

    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            string = string + string1[i - 1]  # Use to store longest common subsequence
            i = i - 1
            j = j - 1
        else:
            if table[i][j-1] > table[i-1][j]:
                j = j - 1
            else:
                i = i - 1
            

    string = "".join(reversed(string))

    return res, string


# Driver Code

if __name__ == "__main__":

    import doctest

    doctest.testmod()

    string1 = "fishing"
    string2 = "fighting"
    
    """
    string1 and string2 represent 2 strings whose longest common subsequence is to be found
    That is here, string1=fishing and string2=fighting
    Thus, longest common subsequence possible is fihing
    """

    """
    len_of_string1 represent length of string string1
    len_of_string1 represent length of string string2
    """
    len_of_string1 = len(string1)
    len_of_string2 = len(string2) 

    
    length, string = longest_common_subsequence(
        string1, string2, len_of_string1, len_of_string2
    )
    """
    The function returns 2 things
    1. length: This is the length of longest common subsequence of the 2 strings
    2. string: This is the actual string (longest common subsequence)
    """

    """
    If length=0, then no common subsequence is present between the two strings
    """
    if length == 0:
        print("\nThere is no longest common subsequence possible")

    else:        
        print("\nLength of Longest Common subsequence is", length)
        print("Longest Common subsequence is", string)
    
    # doctest.testmod(name ='longest_common_subsequence', verbose = True)


