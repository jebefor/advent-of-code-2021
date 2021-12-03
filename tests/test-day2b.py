input_data = [
  ('forward', 5),
  ('down', 5),
  ('forward', 8),
  ('up', 3),
  ('down', 8),
  ('forward', 2)
]

import sys
sys.path.append("../scripts")
from day2b import navigate

def test_calculations(inp):
  func_output = navigate(inp)
  expected_output = 900

  if func_output == expected_output:
    print("Passed Test calculations")
  else:
    print("Failed Test calculations!")

if __name__ == "__main__":
  test_calculations(input_data)


