# Create a program that can randomly generate a series of math problems that can be imported into a Learning Management System (LMS) 
# for the purpose of creating online math tests. 
# The goal is to reduce the manual effort required to create these online math tests by having a program generate the test questions, 
# along with varying the questions and answers, instead of a human having to do this task by hand.

# Project Breakdown
# This project will be broken down into multiple parts, each one building on the other, 
# to reach the goal stated above: each part will cover one or more programming concepts, 
# and what is done in one part may be reworked and improved upon in subsequent parts.

# Part 1: Generate Randomized Addition Problems

# Synopsis
# Write a program that can generate a set of randomized addition problems, 
# such as “What is 27 + 3?” or “What is 8 + 51?”. The program will ask the user how many addition problems to generate, 
# and the program will output that many addition problems, each with randomly-generated terms.


import random

num_of_problems = int(input("How many addition problems would you like to generate?: "))


for i in range(num_of_problems):
    first_num = random.choice(range(101))
    second_num = random.choice(range(101))
    print(f"What is {first_num} + {second_num}")
else:
    print("Done")

