"""
Question 1: -

Write a program that takes a string as input, and counts the frequency of each word in the string, there might be repeated characters in the string. Your task is to find the highest frequency and returns the length of the highest-frequency word.

Note - You have to write at least 2 additional test cases in which your program will run successfully and provide an explanation for the same.

Example input - string = “write write write all the number from from from 1 to 100”

Example output - 5

Explaination - From the given string we can note that the most frequent words are “write” and “from” and the maximum value of both the values is “write” and its corresponding length is 5
"""


# Ans:

def highest_frequency_word_length(string):
    words = string.split()

    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    max_freq = 0
    max_length = 0
    for word, freq in word_freq.items():
        if freq > max_freq or (freq == max_freq and len(word) > max_length):
            max_freq = freq
            max_length = len(word)

    return max_length

#Example test case

string = "hello hello hello hello i am python"
result = highest_frequency_word_length(string)
print(result)

# Example output - 5


# Explaination: In the given example, the word "hello" appears three times, making it the most frequent word. Its length is 5 characters, so the program returns 5.


# Additional Test Cases:

# Test case with a single word repeated multiple times:

string = "fight fight till you win win win win win"
result = find_highest_frequency_word_length(string)
print(result)


# Explaination: In this case, the word "win" appears five times, which is the highest frequency. Its length is 3 characters, so the program returns 3.




