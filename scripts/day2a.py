input_file = "../data/input2.txt"

def to_tuple(string):
  s = string.split(" ")
  t = (s[0], int(s[1]))

  return t

with open(input_file, "r") as f:
  input2 = filter(str, f.read().split("\n"))
  input2 = list(map(to_tuple, input2))

def navigate(inp):
  horizontal_position = 0
  depth = 0

  for (command, unit) in inp:
    if command == "forward":
      horizontal_position += unit
    if command == "down":
      depth += unit
    if command == "up":
      depth -= unit

  return horizontal_position * depth

if __name__ == "__main__":
  navigate(input2)


