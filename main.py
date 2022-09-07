A = 25
B = 50
C = False
D = True

print(isinstance(A, int) and A == 25) # True

print(not isinstance(B, int) or B == 50) # True

print(isinstance(C, bool) and B != True) # True

print(not isinstance(D, bool) or D == False) # False