input_file = "../data/input3.txt"

def separate_bits(num_string):
  ns = [int(n) for n in list(num_string)]
  return ns

def prepare_data(input_file):
  inp = filter(str, input_file.split("\n"))
  inp = list(map(separate_bits, inp))

  return inp

with open(input_file, "r") as f:
  input3 = prepare_data(f.read())

def group_same_bit(inp):
  zipped = [i for i in zip(*inp)]

  return zipped

def get_most_common_bit(lst):
  max_times = 0
  most_common_bit = None
  for num in set(lst):
    count = lst.count(num)
    if count > max_times:
      max_times = count
      most_common_bit = num

  return max_times, most_common_bit

def get_less_common_bit(lst):
  min_times = 1000000000000
  less_commmon_bit = None
  for num in set(lst):
    count = lst.count(num)
    if count < min_times:
      min_times = count
      less_common_bit = num

  return min_times, less_common_bit

def get_gamma_rate(zipped):
  gamma_rate = []
  for l in zipped:
    max_times, most_common_bit = get_most_common_bit(l)
    gamma_rate.append(str(most_common_bit))

  gamma_rate = int("".join(gamma_rate))

  return int(str(gamma_rate), 2)

def get_epsilon_rate(zipped):
  epsilon_rate = []
  for l in zipped:
    min_times, less_common_bit = get_less_common_bit(l)
    epsilon_rate.append(str(less_common_bit))

  epsilon_rate = int("".join(epsilon_rate))

  return int(str(epsilon_rate), 2)

def get_power_consumption(inp):
  zipped = group_same_bit(inp)
  gamma_rate_decimal = get_gamma_rate(zipped)
  epsilon_rate_decimal = get_epsilon_rate(zipped)

  return gamma_rate_decimal * epsilon_rate_decimal

if __name__ == "__main__":
  get_power_consumption(input3)
