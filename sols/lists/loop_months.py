#!/usr/bin/env python3

def is_prime(n):
    # prime numbers are greater than 1
    if n > 1:
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True
    return False

months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]

for mon in months:
    print(mon)

print("---")

for i in range(len(months)):
    print(i, months[len(months)-i-1])

print("---")

for i in range(0, len(months)-1, 3):
    print(months[i])

print("---")

for i in range(len(months)):
    if is_prime(i+1):
        print(i+1, months[i])
