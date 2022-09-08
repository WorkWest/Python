# Labs

## 1

## 2

## 3

### **Lab 3.1: Equality Operators**

```python

4 == 5 # False

5 != 6 # True

4 > 5 # False

4 < 5 # True

2 >= 2 # True

5 <= 2 # False
```
### **Lab 3.2: Membership Operators**

```Python
list1 = ["may", "june", "july", "aug"]
list2 = ["mon", "tue", "wed", "thurs", "fri"]

print("mon" in list2) # True
print("sept" in list1) # False
print("mon" not in list1) # True
print("tue" not in list1) # True
```

### **Lab 3.3: Identity Operators**

```Python
X = 5
Y = 5.5
Z = "string"
A = True

print(isinstance(X, int)) # True

print(not isinstance(Y, float)) # False

print(not isinstance(Z, str)) # False

print(not isinstance(A, bool)) # True
```

### **Lab 3.4: Boolean Operators**

```Python
A = 25
B = 50
C = False
D = True

print(isinstance(A, int) and A == 25) # True

print(not isinstance(B, int) or B == 50) # True

print(isinstance(C, bool) and B != True) # True

print(not isinstance(D, bool) or D == False) # False
```

### **Lab 3.5: Operators**

```python

print(True == False) # False

print(2 != 5) # True

print(5 > 5) # False

print((4*7) < 51) # True

print(2 >= 2.5) # False

print(5 <= 5.0) # True

print("A" in "Apple") # True

print("B" not in "Quebec") # True

print("C" == "c") # False

print("2" != 2) # True

print(2 != "A" and 5 == 5) # True

print("G" != "g" or 5 == "5") # True
```

### **Lab 3.6: Operators**

```python
import pyinputplus as pyip # Import input validation

base_num = pyip.inputNum("Input a number: ") # Take input from a user 

exponent_num = pyip.inputNum("Input another number: ")  # Take input from a user 

# Check if base number input value is between 0-50 and if the exponent number is less than 50 then print the multiplication
if (float(base_num) > 50 or float(base_num) < 0) and (float(exponent_num) > 50):
  print("Your numbers should be between 0-50")
else: 
  print(base_num ** exponent_num)
```

**or** 

```python
base_num = input("Input a number: ") # Take input from a user 

try: 
  base_num = float(base_num)
except:
  print("Number not provided")
  quit()

if base_num <= 50 and base_num < 0:
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
```

### **Lab 3.7/8: While Guessing**

```python
import random

import pyinputplus as pyip

user_guess = pyip.inputNum("Guess a number between 1 and 100: ")

machine_number = random.randrange(1,100)

guesses = 0

while user_guess != machine_number:
  while user_guess < machine_number:
    print("Too low!")
    user_guess = pyip.inputNum("Guess again: ")
    guesses += 1
  while user_guess > machine_number:
    print("Too High!")
    user_guess = pyip.inputNum("Guess again: ")
    guesses += 1

print(f"You did it in {guesses} tries!")
```

### **Lab 3.9: For What?**

```python
# Using range(), write a simple loop to print the values 0-10
for x in range(0,11):
  print(x)
```

```python
# Modify the loop ot only print the odd numbers in the range
for x in range(0,11):
  if x % 2 != 0:
    print(x)
```

```python
# What would you change to print even numbers? 
for x in range(0,11):
  if x % 2 == 0:
    print(x)
```
```python
 # Use conditional statements to break out of the loop when a designated number is encountered
for x in range(0,11):
  if x % 2 == 0:
    print(x)
    if x == 6:
      break
```

### **Lab 3.10: For-Ever -----INPROGRESS-----**

```python
# Write a script that accepts two user inputs: an IP address and subnet mask

ip_addr = input("Please input an IP Address: ")

subnet_mask = input("Please input a Subnet Mask: ")

broken_ip = ip_addr.split('.')
broken_subnet = subnet_mask.split('.')
loopthis = 256 - int(broken_subnet[3])

print(broken_ip)
print(broken_subnet)
print(loopthis)

for x in range(0,loopthis):
  print(x)
```

### **Lab 3.11: Fizzy Lifting Drink**

```python

```