#!/usr/bin/python3
num = 0
while num < 90:
    if num % 10 == 0:
        num += 1 + num // 10
    print(f"{num:02d}", end=" ")
    if num != 89:
        print(",", end=" ")
    num = num + 1
print()
