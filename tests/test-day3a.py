import sys
sys.path.append("../scripts")
from day3a import *

input_data = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

input_data = prepare_data(input_data)

def test_group_same_bit(inp):
  func_output = group_same_bit(inp)
  if len(func_output[0]) == len(inp):
    print("Passed Test 1 group_same_bit")
  else:
    print("Failed Test 1 group_same_bit!")
  if len(func_output) == len(inp[0]):
    print("Passed Test 2 group_same_bit")
  else:
    print("Failed Test 2 group_same_bit!")

def test_get_power_consumption(inp):
  func_output = get_power_consumption(input_data)
  if func_output == 198:
    print("Passed Test get_power_consumption")
  else:
    print("Failed Test get_power_consumption!")

if __name__ == "__main__":
  test_group_same_bit(input_data)
  test_get_power_consumption(input_data)

