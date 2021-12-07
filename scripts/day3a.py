input_file = "../data/input3.txt"

def separate_bits(num_string):
  """
  Transforms a string of numbers into a list of integers.

  Example:
  --------
    input: "12345"
    output: [1, 2, 3, 4, 5]
  """
  ns = [int(n) for n in list(num_string)]

  return ns

def prepare_data(input_file):
  """
  Load a txt file as a list of lists of integers.

  Example:
  --------
    input:
      ""
      12345
      45678
      56789
      ""
    output:
     [[1, 2, 3, 4, 5],
      [4, 5, 6, 7, 8],
      [5, 6, 7, 8, 9]]
  """
  inp = filter(str, input_file.split("\n"))
  inp = list(map(separate_bits, inp))

  return inp

# Read file and call "prepare_data"
with open(input_file, "r") as f:
  input3 = prepare_data(f.read())

def group_same_bit(inp):
  """
  Group elements in the same position on the lists.

  Parameters:
  -----------
    inp: List (output of "prepare_data")

  Example:
  --------
    input:
      [[1, 2, 3, 4, 5],
       [4, 5, 6, 7, 8],
       [5, 6, 7, 8, 9]]
    output:
      [[1, 4, 5],
       [2, 5, 6],
       [3, 6, 7],
       [4, 7, 8],
       [5, 8, 9]]
  """
  zipped = [i for i in zip(*inp)]

  return zipped

def get_most_common_bit(lst):
  """
  Get most common number in a list of integers
  and number of times it is repeated.

  Example:
  --------
  input: [1, 1, 0, 1, 0, 1]
  output: 4, 1 (times, most common integer in list)
  """
  max_times = 0
  most_common_bit = None
  for num in set(lst):
    count = lst.count(num)
    if count > max_times:
      max_times = count
      most_common_bit = num

  return max_times, most_common_bit

def get_least_common_bit(lst):
  """
  Get least common number in a list of integers
  and number of times it is repeated.

  Example:
  --------
  input: [1, 1, 0, 1, 0, 1]
  output: 2, 0 (times, least common integer in list)
  """
  min_times = 1000000000000
  least_commmon_bit = None
  for num in set(lst):
    count = lst.count(num)
    if count < min_times:
      min_times = count
      least_common_bit = num

  return min_times, least_common_bit

def get_gamma_rate(zipped):
  """
  Get most common integer in each list of a list of lists.
  Append all most common integers together and transform the resulting binary number
  into a decimal number.

  Parameters:
  -----------
    zipped: List (output of "group_same_bit")

  Example:
  --------
    input:
      [[1, 0, 1],
       [0, 1, 1],
       [1, 1, 1],
       [0, 0, 1]]
    output: 14 (because we get 1110 as the resulting binary number
                under the variable "gamma_rate")
  """
  gamma_rate = []
  for lst in zipped:
    max_times, most_common_bit = get_most_common_bit(lst)
    gamma_rate.append(str(most_common_bit))

  gamma_rate = int("".join(gamma_rate))

  return int(str(gamma_rate), 2)

def get_epsilon_rate(zipped):
  """
  Get least common integer in each list of a list of lists.
  Append all least common integers together and transform the resulting binary number
  into a decimal number.

  Parameters:
  -----------
    zipped: List (output of "group_same_bit")

  Example:
  --------
    input:
      [[1, 0, 1],
       [0, 1, 1],
       [1, 1, 1],
       [0, 0, 1]]
    output: 3 (because we get 0011 as the resulting binary number
               under the variable "epsilon_rate")
  """
  epsilon_rate = []
  for lst in zipped:
    min_times, least_common_bit = get_least_common_bit(lst)
    epsilon_rate.append(str(least_common_bit))

  epsilon_rate = int("".join(epsilon_rate))

  return int(str(epsilon_rate), 2)

def get_power_consumption(inp):
  """
  Multiply the gamma_rate by the epsilon_rate.

  Parameters:
  -----------
    inp: List (output of "prepare_data")

  Example:
  --------
    input:
      [[1, 0, 1, 0],
       [0, 1, 1, 0],
       [1, 1, 1, 1]]
    output: 42 (gamma_rate is 14, epsilon_rate is 3: 14*3 = 42)
  """
  zipped = group_same_bit(inp)
  gamma_rate_decimal = get_gamma_rate(zipped)
  epsilon_rate_decimal = get_epsilon_rate(zipped)

  return gamma_rate_decimal * epsilon_rate_decimal

if __name__ == "__main__":
  get_power_consumption(input3)
