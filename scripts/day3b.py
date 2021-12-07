from day3a import prepare_data
from collections import Counter
import numpy as np

with open("../data/input3.txt", "r") as f:
  input_3 = prepare_data(f.read())

def get_oxygen_generator_rating(inp):
  to_array = np.array(inp)
  final = to_array.copy()

  for i in range(len(inp[0])):
    if len(final) == 1:
      break
    counts = Counter(final[:,i])
    if (counts[1] > counts[0]) or (counts[1] == counts[0]):
      final = final[np.where(final[:,i] == 1)[0]]
    if counts[1] < counts[0]:
      final = final[np.where(final[:,i] == 0)[0]]

  oxygen_generator_rating = final.tolist()[0]
  oxygen_generator_rating = "".join([str(n) for n in oxygen_generator_rating])

  return int(oxygen_generator_rating, 2)

def get_co2_scrubber_rating(inp):
  to_array = np.array(inp)
  final = to_array.copy()

  for i in range(len(inp[0])):
    if len(final) == 1:
      break
    counts = Counter(final[:,i])
    if (counts[1] > counts[0]) or (counts[1] == counts[0]):
      final = final[np.where(final[:,i] == 0)[0]]
    if counts[1] < counts[0]:
      final = final[np.where(final[:,i] == 1)[0]]

  co2_scrubber_rating = final.tolist()[0]
  co2_scrubber_rating = "".join([str(n) for n in co2_scrubber_rating])

  return int(co2_scrubber_rating, 2)

def get_life_support_rating(inp):

  return get_oxygen_generator_rating(inp) * get_co2_scrubber_rating(inp)


if __name__ == "__main__":
  get_life_support_rating(input_3)






