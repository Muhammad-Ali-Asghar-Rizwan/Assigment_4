def in_range(n, low, high):
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.
  """
  if n >= low and n <= high:
      return True

    # we could have also included an else statement, but since we are returning, it's fine without!
      return False
  
  
  
  
  
if __name__ == "__main__":
  # Test cases
  print(in_range(5, 1, 10)) # True
  print(in_range(0, 1, 10)) # False
  print(in_range(10, 1, 10)) # True
  print(in_range(11, 1, 10)) # False  
  
  
  
  
  