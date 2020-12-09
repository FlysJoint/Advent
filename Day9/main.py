#!/bin/python3

def read_input_file(input_file):
  with open(input_file, "r") as f:
    contents = f.readlines()
    return contents
    # above stolen from Charles otherwise I'd be writing it out by hand again

def find_nonsum(input_file):

  nums = []

  for line in input_file:
    nums.append(int(line))
  else:
    return nums

def find_answer1(p, arr):
  # print(arr)

  n = p
  while n < len(arr):
    # print('checking...', arr[n])

    for num in range(n - p, n, 1):
      # print(arr[n - p:n:1])
      # print(arr[n] - arr[num])
      # print(arr[n] - arr[num] in arr[n - p:n:1])

      if arr[n] - arr[num] in arr[n - p:n:1]:
        break
    else:
        return arr[n]

    n = n + 1
  
def find_answer2(n, arr):
  # print(n, arr)
  start = 0
  stop = 1
  while stop < len(arr):
    # print(sum(arr[start: stop]))
    if sum(arr[start: stop]) < n:
      stop = stop + 1
    elif sum(arr[start: stop])== n:
      return max(arr[start: stop]) + min(arr[start: stop]) 
    else:
      start = start + 1
    
# print(find_answer1(5, find_nonsum(read_input_file("test.txt"))))
print('Part 1: ', find_answer1(25, find_nonsum(read_input_file("input.txt"))))


# print( find_answer2(find_answer1(5, find_nonsum(read_input_file("test.txt"))), find_nonsum(read_input_file("test.txt"))) )
print('Part 2: ', find_answer2(find_answer1(25, find_nonsum(read_input_file("input.txt"))), find_nonsum(read_input_file("input.txt"))) )
