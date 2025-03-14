import sys

colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def resistance(c1, c2, c3):
    return (colors.index(c1) * 10 + colors.index(c2)) * (10**colors.index(c3))

c1, c2,  c3 = [sys.stdin.readline().strip() for _ in range(3)]

print(resistance(c1, c2, c3))