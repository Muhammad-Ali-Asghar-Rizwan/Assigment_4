def compute(values): 
   return [v ** 2 for v in values if v % 2 == 0]    
print(compute(range(6)))  
