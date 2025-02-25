X = {'a', 'g', 'b', 'c', 'd', 'f'}
Y = {'b', 'c', 'h', 'l', 'm', 'o'}
Z = {'c', 'd', 'f', 'j', 'k'}

result_1 = len(X | Y)
print(f"1. Total elements in X or Y: {result_1}")

result_2 = Y - (X | Z)
print(f"2. Elements in Y but not in X or Z: {result_2} (Count: {len(result_2)})")

set_1 = {'h', 'i', 'j', 'k'}
set_2 = X & Z
set_3 = (X & Y) | {'h'}
set_4 = X & Z - Y
set_5 = X & Y & Z
set_6 = Y - (X | Z)

print(f"s1: {set_1}")
print(f"s2: {set_2}")
print(f"s3: {set_3}")
print(f"s4: {set_4}")
print(f"s5: {set_5}")
print(f"s6: {set_6}")
