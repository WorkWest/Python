base_num = input("Input a number: ") # Take input from a user 

try: 
  base_num = float(base_num)
except:
  print("Number not provided")
  quit()

if base_num < 50 and base_num < 0:
  print("Number must be less than 50 and greater than zero.")
  quit()
  
exponent_num = input("Input another number: ")  # Take input from a user 

try: 
  exponent_num = float(exponent_num)
except:
  print("Number not provided")
  quit()

if base_num > 50:
  print("Number must be less than 50.")
  quit()

print(base_num ** exponent_num)