T = int(input())
N = [0] * 1000

for i in range(100):
    N[i] = i % T
    print(f'N[{i}] = {N[i]}')
