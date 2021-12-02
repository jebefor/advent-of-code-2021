input_file = "../data/input1.txt"

with open(input_file, "r") as f:
  input1 = filter(str, f.read().split("\n"))
  input1 = list(map(int, input1))

def num_larger_measurements(inp):
  total_num = 0

  for idx, i in enumerate(inp):
    if i > inp[idx-1]:
      total_num += 1

  print(total_num)
  return total_num

if __name__ == "__main__":
  num_larger_measurements(input1)
