from day1a import num_larger_measurements

input_file = "../data/input1.txt"

with open(input_file, "r") as f:
  input2 = filter(str, f.read().split("\n"))
  input2 = list(map(int, input2))

def num_increased_window_sum(inp):
  new_list = []
  for idx, i in enumerate(inp):
    if idx <= len(inp) - 2:
      new_list.append(inp[idx:idx+3])
    else:
      new_list.append(inp[idx:])

  sum_list = list(map(sum, new_list))
  num_increased = num_larger_measurements(sum_list)

  return num_increased

if __name__ == "__main__":
  num_increased_window_sum(input2)
