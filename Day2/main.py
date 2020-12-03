#!/bin/python3

import re

def read_password_file(pass_file):
  with open(pass_file, "r") as f:
    contents = f.readlines()
    return contents
    # above stolen from Charles otherwise I'd be writing it out by hand again

def check_policies(policies):

  count = 0

  pattern = '^(\d*)-(\d*) ([a-z]): (.*)$'

  for policy in policies:
    regex = re.search(pattern, policy)
    min = int(regex.group(1))
    max = int(regex.group(2))
    letter = regex.group(3)
    password = regex.group(4)

    # Part 1
    # if password.count(letter) >= min and password.count(letter) <= max:
    #   count = count + 1

    # Part 2
    min = min -1
    max = max -1
    if password[min] == letter and password[max] != letter or password[min] != letter and password[max] == letter:
      count = count + 1
  else:
    return count

print(check_policies(read_password_file("input.txt")))
