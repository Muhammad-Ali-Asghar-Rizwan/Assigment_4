import random

# Generate a random integer between 1 and 10
def generate_random_integer(): 
  for i in range(10):
    random_integer = random.randint(1, 100)
    print(f"Random integer {i+1}: {random_integer}")
    


if __name__ == "__main__":
    generate_random_integer()    