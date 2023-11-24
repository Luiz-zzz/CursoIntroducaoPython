X = [int(input()) for _ in range(10)]

for i in range(10):
    if X[i] <= 0:
        X[i] = 1
    print(f'X[{i}] = {X[i]}')
