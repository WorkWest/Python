import pyinputplus as pyip

base_num = pyip.inputNum("Input a number: ")

exponent_num = pyip.inputNum("Input another number: ")   

if (float(base_num) > 50 or float(base_num) < 0) and (float(exponent_num) > 50 or float(exponent_num) < 0):
  print("Your numbers should be between 0-50")
else: 
  print(base_num ** exponent_num)