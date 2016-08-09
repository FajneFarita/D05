#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
import os


# Body
def print_long_words(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) > 20:
                    print(word)


##############################################################################
def main():
    print_long_words('words.txt')

if __name__ == '__main__':
    main()
