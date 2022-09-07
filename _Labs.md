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