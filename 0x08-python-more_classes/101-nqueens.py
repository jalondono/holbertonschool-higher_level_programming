#!/usr/bin/python3
from sys import argv
"""
print all posibile solution of queens
"""
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
digit = int(argv[1])
if digit < 4:
    print("N must be at least 4")
    exit(1)
