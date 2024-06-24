import sys
import math

input = sys.stdin.readline

A, B = map(int, input().strip().split())
C, D = map(int, input().strip().split())

son = A*D + B*C
mom = B*D

gcd = math.gcd(son, mom)

son //= gcd
mom //= gcd

print(son, mom)