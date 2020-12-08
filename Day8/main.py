#!/bin/python3

def read_input_file(input_file):
  with open(input_file, "r") as f:
    contents = f.readlines()
    return contents
    # above stolen from Charles otherwise I'd be writing it out by hand again

def get_acc(input_file):
  global loop
  loop = []
  loop.append(['tst', '*', '0'])

  for line in input_file:
    loop.append([line[0:3], line[4:5], line[5:]])
  else:
    return loop

def find_loop(loop):
  acc = 0
  cmd_line = 1

  done = []

  while cmd_line not in done:
    done.append(cmd_line)
    # print(cmd_line, loop[cmd_line][0], loop[cmd_line][1], loop[cmd_line][2])
    if loop[cmd_line][0] == 'nop':
      cmd_line = cmd_line + 1
    elif loop[cmd_line][0] == 'acc':
      if loop[cmd_line][1] == '+':
        acc = acc + int(loop[cmd_line][2])
      else:
        acc = acc - int(loop[cmd_line][2])
      cmd_line = cmd_line + 1
    elif loop[cmd_line][0] == 'jmp':
      if loop[cmd_line][1] == '+':
        cmd_line = cmd_line + int(loop[cmd_line][2]) 
      else:
        cmd_line = cmd_line - int(loop[cmd_line][2]) 
    # print(acc)
  else:
    return acc

print(find_loop(get_acc(read_input_file("input.txt"))))
# print(find_loop(get_acc(read_input_file("test.txt"))))
