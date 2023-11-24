V = int(input())

N = []
N.append(V)

for i in range(1, 10):
    N.append(N[i - 1] * 2)

for i in range(10):
    print(f"N[{i}] = {N[i]}")